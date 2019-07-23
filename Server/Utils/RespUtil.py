from flask import Response
import json

def handleJsonRet(dict, code):
	'''
	处理响应内容及状态码
	'''
	resp = Response(
		json.dumps(obj=dict, indent=4, ensure_ascii=False).encode("utf-8"), 
		mimetype='application/json'
	)

	resp.headers['Access-Control-Allow-Origin'] = '*'
	resp.status_code = code
	return resp