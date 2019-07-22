import math, cv2
import numpy as np

def rotate_img(image, angle):
    '''
    图片顺时针旋转 angle 弧度
    '''
    angle = angle * 180 / math.pi
    # print(image.shape, angle)
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    
    return cv2.warpAffine(image, M, (nW, nH))

def rotate_pnt(img, rimg, angle, pnt):
    '''
    点随图片顺时针旋转 angle 弧度
    '''
    h0, w0 = img.shape[0], img.shape[1]
    [x0, y0] = pnt
    
    vec0 = [x0 - w0 / 2, y0 - h0 / 2]
    cos, sin = math.cos(angle), math.sin(angle)
    vec1 = [cos * vec0[0] - sin * vec0[1], sin * vec0[0] + cos * vec0[1]]
    
    h1, w1 = rimg.shape[0], rimg.shape[1]
    [x1, y1] = [w1 / 2 + vec1[0], h1 / 2 + vec1[1]]
    if x1 < 0: x1 = 0
    if y1 < 0: y1 = 0
    return [math.floor(x1), math.floor(y1)]

def cut_img(img, pnt1, pnt2, pnt3, pnt4):
    [x1, y1], [x2, y2], [x3, y3], [x4, y4] = pnt1, pnt2, pnt3, pnt4
   
    if y1 > y2:
        isClockwize = True
        angle = math.atan((y1 - y2) / (x2 - x1))
    else:
        isClockwize = False
        angle = math.atan((y2 - y1) / (x2 - x1))
    
    # print(isClockwize, angle)
    rimg = rotate_img(img, angle)
    [xx1, yy1], [xx2, yy2], [xx3, yy3], [xx4, yy4] = \
        rotate_pnt(img, rimg, angle, pnt1), rotate_pnt(img, rimg, angle, pnt2), rotate_pnt(img, rimg, angle, pnt3), rotate_pnt(img, rimg, angle, pnt4)
    
    if yy1 > yy3:
        if xx3 > xx1:
            rcutimg = rimg[yy3:yy1, xx3:xx1, :]
        else:
            rcutimg = rimg[yy3:yy1, xx1:xx3, :]
    else:
        if xx1 > xx3:
            rcutimg = rimg[yy1:yy3, xx3:xx1, :]
        else:
            rcutimg = rimg[yy1:yy3, xx1:xx3, :]
    cutimg = rotate_img(rcutimg, -angle)
    return cutimg

# cutimg = cut_img(img, [342, 150], [664, 115], [679, 270], [358, 305])
# plt.imshow(cutimg)
# plt.show()