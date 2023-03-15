import time
from flask import Flask,request
import json


import sys
import datetime
# app = Flask(__name__)
from db_config import app
from utils.debug import Logger

sys.stdout = Logger('/tmp/garbage.log', sys.stdout)
print('Server Begins...{}'.format(datetime.datetime.now()))

# user模块
from routes.user import user
from routes.manager import manager
app.register_blueprint(user,url_prefix="/user")
app.register_blueprint(manager,url_prefix="/manager")


@app.route('/')
def ping():
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)