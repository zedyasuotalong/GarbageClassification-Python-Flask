import time
from flask import Flask,request
import json


import sys
import datetime
# app = Flask(__name__)
from db_config import app
from utils.debug import Logger
from utils.parse import config

sys.stdout = Logger(config['log_path'], sys.stdout)
print('Server Begins...{}'.format(datetime.datetime.now()))

# user模块
from routes.user import user
from routes.manager import manager
from routes.test import test
app.register_blueprint(user,url_prefix="/user")
app.register_blueprint(manager,url_prefix="/manager")
app.register_blueprint(test,url_prefix="/test")


@app.route('/')
def ping():
    return "ok"

if __name__ == '__main__':
    # context = ('ssl_cert/server.crt', 'ssl_cert/server.key')
    # app.run(host='0.0.0.0',port=5000,debug=True, ssl_context=context)
    app.run(host=config['server_ip'],port=config['server_port'],debug=True)