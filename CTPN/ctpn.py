# coding=utf-8

# Ref from eragonruan/text-detection-ctpn
# https://github.com/eragonruan/text-detection-ctpn/blob/banjin-dev/main/demo.py
# Modified some code by Aoihosizora

import os
import shutil
import sys
import time

import cv2
import numpy as np
import tensorflow as tf

sys.path.append(os.getcwd())
sys.path.append('./ctpn_repo/')

# TF_CPP_MIN_LOG_LEVEL 0: 输出所有信息
# TF_CPP_MIN_LOG_LEVEL 1: 屏蔽通知信息
# TF_CPP_MIN_LOG_LEVEL 2: 屏蔽通知信息和警告信息
# TF_CPP_MIN_LOG_LEVEL 3: 屏蔽通知信息、警告信息和报错信息

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from nets import model_train as model
from utils.rpn_msr.proposal_layer import proposal_layer
from utils.text_connector.detectors import TextDetector

tf.app.flags.DEFINE_string('gpu', '0', '')

# TODO
tf.app.flags.DEFINE_string('checkpoint_path', 'ctpn_repo/checkpoints_mlt/', '')

FLAGS = tf.app.flags.FLAGS

def resize_image(img):
    img_size = img.shape
    im_size_min = np.min(img_size[0:2])
    im_size_max = np.max(img_size[0:2])

    im_scale = float(600) / float(im_size_min)
    if np.round(im_scale * im_size_max) > 1200:
        im_scale = float(1200) / float(im_size_max)
    new_h = int(img_size[0] * im_scale)
    new_w = int(img_size[1] * im_scale)

    new_h = new_h if new_h // 16 == 0 else (new_h // 16 + 1) * 16
    new_w = new_w if new_w // 16 == 0 else (new_w // 16 + 1) * 16

    re_im = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
    return re_im, (new_h / img_size[0], new_w / img_size[1])

def ctpnParse(image_path):
    '''
    转换获取图片文字区域组
    '''
    os.environ['CUDA_VISIBLE_DEVICES'] = FLAGS.gpu

    with tf.get_default_graph().as_default():
        input_image = tf.placeholder(tf.float32, shape=[None, None, None, 3], name='input_image')
        input_im_info = tf.placeholder(tf.float32, shape=[None, 3], name='input_im_info')

        global_step = tf.get_variable('global_step', [], initializer=tf.constant_initializer(0), trainable=False)

        bbox_pred, cls_pred, cls_prob = model.model(input_image)

        variable_averages = tf.train.ExponentialMovingAverage(0.997, global_step)
        saver = tf.train.Saver(variable_averages.variables_to_restore())

        with tf.Session(config=tf.ConfigProto(allow_soft_placement=True)) as sess:
            ckpt_state = tf.train.get_checkpoint_state(FLAGS.checkpoint_path)
            model_path = os.path.join(FLAGS.checkpoint_path, os.path.basename(ckpt_state.model_checkpoint_path))
            print('Restore from {}'.format(model_path))
            saver.restore(sess, model_path)

            ####################################################################################
            # read img

            print(image_path)
            start = time.time()
            try:
                im = cv2.imread(image_path)[:, :, ::-1]
            except:
                print("Error reading image {}!".format(image_path))
                exit(1)

            ####################################################################################
            # resize

            img, (rh, rw) = resize_image(im)
            print("Ritu ", rh, rw)
            print("Mae: ", im.shape[0], im.shape[1])
            print("Ushiro: ", img.shape[0], img.shape[1])

            # Ritu: 0.6375 0.6333333333333333
            # Mae:  1280 960
            # Ushiro:  816 608

            h, w, c = img.shape
            im_info = np.array([h, w, c]).reshape([1, 3])
            bbox_pred_val, cls_prob_val = sess.run([bbox_pred, cls_prob],
                                                    feed_dict={input_image: [img],
                                                                input_im_info: im_info})

            ####################################################################################
            # parse

            textsegs, _ = proposal_layer(cls_prob_val, bbox_pred_val, im_info)
            scores = textsegs[:, 0]
            textsegs = textsegs[:, 1:5]

            # textdetector = TextDetector(DETECT_MODE='H')
            textdetector = TextDetector(DETECT_MODE='O')
            boxes = textdetector.detect(textsegs, scores[:, np.newaxis], img.shape[:2])
            boxes = np.array(boxes, dtype=np.int)

            ####################################################################################
            # data

            cost_time = (time.time() - start)
            print("cost time: {:.2f}s".format(cost_time))

            # frames

            frames = []
            
            for i, box in enumerate(boxes):
                pnts = []
                # i = 01, 23, 45, 67
                pnts.extend({
                    "x": int(box[i * 2] / rh),
                    "y": int(box[i * 2 + 1] / rw)
                } for i in range(4))
                frames.append({
                    "points": pnts,
                    "score": scores[i]
                })

            return {
                "size": {
                    "x": im.shape[0],
                    "y": im.shape[1]
                },
                "cnt": len(boxes),
                "frames": frames
            }

            '''
            {
                size: {
                    x: 1280,
                    y: 960
                },
                cnt: 8,
                frames: [
                    {
                        points: [
                            { x: 160, y: 507 },
                            { x: 593, y: 518 },
                            { x: 592, y: 577 },
                            { x: 158, y: 566 }
                        ],
                        score: 0.9996464
                    }, ...                    
                ]
            }
            '''

image_path = './ctpn_repo/data/demo/007.jpg'

if __name__ == '__main__':
    print(ctpnParse(image_path))