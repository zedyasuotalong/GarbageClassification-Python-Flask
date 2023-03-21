from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from error_code import *
from flask import Blueprint,request
import json

manager = Blueprint('manager',__name__)

from api.user      import  User_list,User_info,User_change_info,User_delete_info,User_added_by_time
from api.manager   import  Manager_login,Manager_change_password
from api.question  import  Question_list,Question_info,Question_change_info,Question_delete_info,Question_add
from api.garbage   import Garbage_list,Garbage_showOneCategory,Garbage_change_info,Garbage_delete_info,Garbage_add_info
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

#####################for manager###########################
@manager.route('/login',methods=['POST'])
def login():
    ret_code,data = parse_json_data(request.data, ['username', 'password'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    ans = Manager_login(data['username'], data['password'])
    resp = make_resp(ans)

    return resp

@manager.route('/change_password',methods=['POST'])
def change_password():
    ret_code,data = parse_json_data(request.data, ['username', 'password', 'newPassword'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    ans = Manager_change_password(data['username'], data['password'], data['newPassword'])
    resp = make_resp(ans)
    
    return resp

#####################for user management###########################
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

@manager.route('/change_user',methods=['POST'])
def change_user():
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

@manager.route('/delete_user',methods=['POST'])
def delete_user():
    ret_code,data = parse_json_data(request.data, ['id'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    id = data['id']

    ans = User_delete_info(id)
    resp = make_resp(ans)

    return resp

@manager.route('/getAddUser_byDay',methods=['GET'])
def getAddUser_byDay():

    ans,data = User_added_by_time()
    resp = make_resp(ans,data)

    return resp

#####################for question management###########################
@manager.route('/question_list',methods=['GET'])
def question_list():
    ans,data = Question_list()
    resp = make_resp(ans,data)
    return resp

@manager.route('/question_info',methods=['GET','POST'])
def question_info():
    ret_code,data = parse_json_data(request.data, ['id'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    ans,data = Question_info(data['id'])
    DEBUG(ans=ans)
    DEBUG(data=data)
    resp = make_resp(ans,data)

    return resp

@manager.route('/change_question',methods=['POST'])
def change_question():
    ret_code,data = parse_json_data(request.data, ['id','picture','answer','explains'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    id = data['id']
    data.pop('id')

    ans = Question_change_info(id, data)
    resp = make_resp(ans)

    return resp

@manager.route('/add_question',methods=['POST'])
def add_question():

    ret_code,data = parse_json_data(request.data, ['picture','answer','explains'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    picture = data['picture']
    answer = data['answer']
    explains = data['explains']

    # 添加题目
    ans = Question_add(picture, answer, explains)
    resp = make_resp(ans)

    return resp

@manager.route('/delete_question',methods=['POST'])
def delete_question():
    print('request.data:{}'.format(request.data))
    ret_code,data = parse_json_data(request.data, ['id'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    id = data['id']

    ans = Question_delete_info(id)
    resp = make_resp(ans)

    return resp

########################################################################################################################
# Garbage相关的管理员操作
########################################################################################################################


@manager.route('/garbage_list', methods=['POST','GET'])
def garbage_list():
    ans, data = Garbage_list()
    resp = make_resp(ans, data)
    return resp

@manager.route('/garbage_change', methods=['POST'])
def change_garbage_info():
    ret_code, data = parse_json_data(request.data, ['id', 'name', 'category_id', 'info', 'count'])

    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp

    id = data['id']
    data.pop('id')
    print(data)

    ans = Garbage_change_info(id, data)
    resp = make_resp(ans)

    return resp

@manager.route('/delete_garbage', methods=['POST'])
def delete_garbage_info():
    ret_code, data = parse_json_data(request.data, ['id'])

    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp

    id = data['id']

    ans = Garbage_delete_info(id)
    resp = make_resp(ans)

    return resp

@manager.route('/add_garbage', methods=['POST'])
def add_garbage_info():
    ret_code, data = parse_json_data(request.data, ['name', 'category_id', 'info'])

    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp

    print(data)

    ans = Garbage_add_info(data)
    resp = make_resp(ans)

    return resp


# 如需查询某一类别（category_id)下的所有garbage信息，请调用routes/garbage.py下的show_one_category接口
