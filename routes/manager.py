from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from error_code import *
from flask import Blueprint,request
import json

manager = Blueprint('manager',__name__)

from api.user import User_list,User_info,User_change_info,User_delete_info

def parse_json_data(data, params):
    try:
        data = json.loads(request.data) # data is json
    except: # data is not json
        print()
        return REQUEST_DATA_FORMAT_ERROR,None
    INFO(request_data=data)
    for key in params:
        if key not in data:
            return MISSING_REQUIRED_PARAMS,None
    return OK,data

@manager.route('/user_list',methods=['GET'])
def user_list():
    ans,data = User_list()
    resp = make_resp(ans,data)
    return resp

@manager.route('/user_info',methods=['GET','POST'])
def info():
    ret_code,data = parse_json_data(request.data, ['id'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    ans,data = User_info(data['id'], isMana=1)
    DEBUG(ans=ans)
    DEBUG(data=data)
    resp = make_resp(ans,data)

    return resp

@manager.route('/change_user_info',methods=['POST'])
def change_user_info():
    ret_code,data = parse_json_data(request.data, ['id','name','phone','password','email','age','sex', 'job'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    id = data['id']
    data.pop('id')
    print(data)

    ans = User_change_info(id, data)
    resp = make_resp(ans)

    return resp

@manager.route('/delete_user_info',methods=['POST'])
def delete_user_info():
    ret_code,data = parse_json_data(request.data, ['id'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    id = data['id']

    ans = User_delete_info(id)
    resp = make_resp(ans)

    return resp

# @user.route('/reg',methods=['POST'])
# def reg():
#     data = json.loads(request.data)

#     data = User_reg({
#         "sername":data['username']


        
#     }})
#     return "123"
