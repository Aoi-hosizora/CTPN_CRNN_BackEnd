from flask import Flask, app
from flask_cors import CORS

from Server.Middleware import CorsMw
from Server.Routes import GetRegionsBlue, ErrorHandle

FlaskApp = Flask(__name__)
host = '0.0.0.0'
port = 1627

def setup(app: app.Flask):
    '''
    设置 中间件 蓝图 编码
    '''
    CorsMw.setupCors(app)
    GetRegionsBlue.registerBlueRegions(app)
    ErrorHandle.errorHandle(app)
    
    app.config['JSON_AS_ASCII'] = False

if __name__ == "__main__":
    setup(FlaskApp)

    FlaskApp.run(host=host, port=port)
