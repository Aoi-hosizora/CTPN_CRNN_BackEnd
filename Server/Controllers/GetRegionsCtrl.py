import sys, os
import cv2, numpy

from Server.Models.Apis import Point, Frame, Regions
from Server.Utils.Exception.ImgNotFoundException import ImgNotFoundException

from CRNN import crnn # torch ..
from CTPN import ctpn # tf

def getRegionsOCR(img_path):
    '''
    根据相对路径 切割区域并OCR，返回 Regions
    img = cv2.imread(img_path)
    '''
    # Data
    # img_path = './data/007.jpg'
    # img_path = './CRNN/data/007.jpg'
    img = cv2.imread(img_path)

    if not isinstance(img, numpy.ndarray):
        remove_img(img_path)
        raise(ImgNotFoundException(img_path))

    # ocr TODO 等服务器部署再加上去
    ret = crnn.crnnRegionsOcr(img, ctpn.ctpnGetRegions(img))    
    
    # ret = crnn.crnnRegionsOcr(img, {
    #     'size': {'x': 682, 'y': 1024},
    #     'cnt': 5,
    #     'frames': [
    #         {'points': [{'x': 342, 'y': 150}, {'x': 664, 'y': 115}, {'x': 679, 'y': 270}, {'x': 358, 'y': 305}], 'score': 0.9998086},
    #         {'points': [{'x': 878, 'y': 653}, {'x': 1021, 'y': 653}, {'x': 1021, 'y': 672}, {'x': 879, 'y': 672}], 'score': 0.99980634},
    #         {'points': [{'x': 0, 'y': 651}, {'x': 251, 'y': 652}, {'x': 251, 'y': 672}, {'x': 0, 'y': 671}], 'score': 0.999803},
    #         {'points': [{'x': 167, 'y': 430}, {'x': 843, 'y': 366}, {'x': 854, 'y': 496}, {'x': 179, 'y': 560}], 'score': 0.9998011},
    #         {'points': [{'x': 426, 'y': 308}, {'x': 556, 'y': 303}, {'x': 559, 'y': 381}, {'x': 430, 'y': 388}], 'score': 0.9997842}
    #     ]
    # })

    # ret
    size = ret['size']
    frames = ret['frames']
    frames = [
        Frame(
            points=[
                Point(x=pnts['x'], y=pnts['y'])
            for pnts in fmr['points']],
            score=fmr['score'],
            ocr=fmr['ocr']
        ) 
    for fmr in frames]

    remove_img(img_path)
    
    return Regions(
        size=Point(x=size['x'], y=size['y']),
        cnt=len(frames),
        frames=frames
    )

def remove_img(img_path):
    '''
    判断存在，并删除
    '''
    if os.path.exists(img_path):
        os.remove(img_path)