from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from error_code import *
from flask import Blueprint,request
import json

user = Blueprint('user',__name__)

from api.user import *

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

@user.route('/login',methods=['POST'])
def login():
    # 键'password'对应的值是密码或者验证码
    # loginType==0，password里存的是密码
    # loginType==1，password里存的是验证码
    ret_code,data = parse_json_data(request.data, ['loginType', 'phone', 'password'])
    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp

    # some check
    if data['loginType'] not in [0,1]:
        resp = make_resp(UNSUPPORTED_LOGIN_TYPE)
        return resp    

    loginType = data['loginType']
    account   = data['phone']
    password  = data['password']
    
    ans = User_login(loginType, account, password)
    resp = make_resp(ans)

    return resp

@user.route('/send_verify_code',methods=['POST'])
def send_verify_code():
    # type==0，是登陆时发送验证码
    # type==1，是注册时发送验证码
    # type==2，是修改敏感信息时发送验证码
    ret_code,data = parse_json_data(request.data, ['type', 'phone'])
    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp

    type = data['type']
    phone = data['phone']

    ans = User_send_verify_code(type, phone)
    resp = make_resp(ans)

    return resp

@user.route('/verify_verify_code',methods=['POST'])
def verify_verify_code():
    # parse json data
    ret_code,data = parse_json_data(request.data, ['phone', 'verify_code'])
    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp

    phone = data['phone']
    verify_code = data['verify_code']
    
    ans = User_verify_verify_code(phone,verify_code)
    resp = make_resp(ans)

    return resp

@user.route('/change_sensitive_info',methods=['POST'])
def change_sensitive_info():
    # type==0，value里存的是电话号码
    # type==1，value里存的是密码
    ret_code,data = parse_json_data(request.data, ['id', 'type', 'value'])
    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    id = data['id']
    type = data['type']
    value = data['value']

    if type not in [0,1]:
        resp = make_resp(UNSUPPORTED_USER_CHANGE_INFO_TYPE)
        return resp

    ans = User_change_sensitive_info(id, type, value)
    resp = make_resp(ans)

    return resp

@user.route('/change_info',methods=['POST'])
def change_info():
    # 除了id，其他值可以为空
    ret_code,data = parse_json_data(request.data, ['id', 'name', 'email', 'age', 'sex', 'job'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    id = data['id']
    data.pop('id')
    print(data)

    ans = User_change_info(id, data)
    resp = make_resp(ans)

    return resp

@user.route('/info',methods=['GET','POST'])
def info():
    ret_code,data = parse_json_data(request.data, ['id'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    ans,data = User_info(data['id'])
    DEBUG(ans=ans)
    DEBUG(data=data)
    resp = make_resp(ans,data)

    return resp

# @user.route('/reg',methods=['POST'])
# def reg():
#     data = json.loads(request.data)

#     data = User_reg({
#         "sername":data['username']


        
#     }})
#     return "123"
