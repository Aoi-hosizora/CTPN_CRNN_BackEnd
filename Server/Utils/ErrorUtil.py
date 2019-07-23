from Server.Models.Message import Message

Success = 200
NotFound = 404
InternalServerError = 500
MethodNotAllowed = 405
Forbidden = 403
ImageNotFound = 406

def handleErrorDetail(error: TypeError) -> str:
    '''
    获取错误提示详情
    '''
    return str(error.__str__())

def getErrorMessageJson(error: TypeError, title: str) -> dict:
    '''
    获取错误 Message Json
    '''
    return Message(message=title, detail=handleErrorDetail(error)).toJson()