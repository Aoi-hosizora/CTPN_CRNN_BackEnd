from flask import Blueprint
from flask.app import Flask
import json

from Server.Controllers import GetRegionsCtrl
from Server.Utils import RespUtil, ErrorUtil
from Server.Models import Apis, Message

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

@blue_regions.route("/ocr", methods=['GET'])
def getRegionsInBlue():
    return RespUtil.handleJsonRet(
        dict=GetRegionsCtrl.getRegions().toJson(),
        code=ErrorUtil.Success
    )