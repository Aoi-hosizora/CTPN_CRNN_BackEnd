from Server.Utils import ErrorUtil, RespUtil
from Server.Models.Message import Message

from flask.app import Flask

def errorHandle(app: Flask):
	'''
	向 FlaskApp 添加错误处理
	'''
	@app.errorhandler(404)
	def error_404(error: TypeError):
		return RespUtil.handleJsonRet(
			dict=ErrorUtil.getErrorMessageJson(error=error, title="Not Found"),
			code=ErrorUtil.NotFound
		)

	@app.errorhandler(500)
	def error_500(error: TypeError):
		return RespUtil.handleJsonRet(
			dict=ErrorUtil.getErrorMessageJson(error=error, title="Internal Server Error"),
			code=ErrorUtil.InternalServerError
		)

	@app.errorhandler(405)
	def error_405(error: TypeError):
		return RespUtil.handleJsonRet(
			dict=ErrorUtil.getErrorMessageJson(error=error, title="Method Not Allowed"),
			code=ErrorUtil.MethodNotAllowed
		)