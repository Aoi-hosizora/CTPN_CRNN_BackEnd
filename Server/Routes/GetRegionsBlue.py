from flask import Blueprint, request
from flask.app import Flask
from werkzeug import secure_filename

import json, os

from Server.Controllers import GetRegionsCtrl
from Server.Utils import RespUtil, ErrorUtil
from Server.Models import Apis, Message
from Server.Utils.Exception.ImgNotFoundException import ImgNotFoundException

blue_regions = Blueprint("blue_regions", __name__, url_prefix="/ocr")

def registerBlueRegions(app: Flask):
    '''
    注册 blue_regions
    '''
    app.register_blueprint(blue_regions)

@blue_regions.route("/", methods=['GET'])
def getMsgInBlue():
    return RespUtil.handleJsonRet(
        dict=Message.Message("CTPN CRNN OCR Api").toJson(), 
        code=ErrorUtil.Success
    )

@blue_regions.route("/upload", methods=['POST'])
def getRegionsInBlue():

    img = request.files.get('img')

    if img == None:
        raise(ImgNotFoundException())

    filename = secure_filename(img.filename)

    # tmp save
    basedir = './tmp/'
    path = basedir + filename
    img.save(path)

    return RespUtil.handleJsonRet(
        dict=GetRegionsCtrl.getRegionsOCR(img_path=path).toJson(),
        code=ErrorUtil.Success
    )