from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from error_code import *
from flask import Blueprint,request
import json
import hashlib

manager = Blueprint('manager',__name__)

from api.user      import  User_list,User_info,User_change_info,User_delete_info,User_added_by_time,User_all_added,User_added_by_sex,User_added_by_job
from api.manager   import  Manager_login,Manager_change_password
from api.question  import  Question_list,Question_info,Question_change_info,Question_delete_info,Question_add
from api.garbage   import Garbage_info,Garbage_list,Garbage_change_info,Garbage_delete_info,Garbage_add_info,Garbage_nums_per_category,Garbage_all_added,Garbage_count_per_category
from api.test      import *
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
    ret_code,data = parse_json_data(request.data, ['username', 'password', 'new_password'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    ans = Manager_change_password(data['username'], data['password'], data['new_password'])
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
    data['password'] = hashlib.sha1(data['password'].encode('utf-8')).hexdigest()

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

@manager.route('/get_added_user_by_day',methods=['POST'])
def get_added_user_by_day():
    ret_code,data = parse_json_data(request.data, ['start_time', 'end_time'])

    if ret_code!= OK:
        resp = make_resp(ret_code)
        return resp

    start_time = data['start_time']
    end_time = data['end_time']
    if start_time > end_time:
        return make_resp(REQUEST_DATA_ERROR)
    ans,data = User_added_by_time(start_time, end_time)
    resp = make_resp(ans,data)

    return resp

@manager.route('/get_all_user_num',methods=['GET'])
def get_all_user_num():

    ans,data = User_all_added()
    resp = make_resp(ans,data)

    return resp

@manager.route('/get_sex_nums',methods=['GET'])
def get_sex_nums():

    ans,data = User_added_by_sex()
    resp = make_resp(ans,data)

    return resp

@manager.route('/get_job_nums',methods=['GET'])
def get_job_nums():

    ans,data = User_added_by_job()
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


@manager.route('/garbage_list', methods=['GET'])
def garbage_list():
    ans, data = Garbage_list()
    resp = make_resp(ans, data)
    return resp

@manager.route('/garbage_info', methods=['POST'])
def garbage_info():
    ret_code, data = parse_json_data(request.data, ['id'])

    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp

    ans, data = Garbage_info(data['id'])
    resp = make_resp(ans, data)
    return resp

@manager.route('/change_garbage', methods=['POST'])
def change_garbage_info():
    ret_code, data = parse_json_data(request.data, ['id', 'name', 'category_id', 'info'])

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
    category_id = data['category_id']
    DEBUG(category_id=category_id)
    if type(category_id) == str:
        category_id = int(category_id)
    if category_id not in [0,1,2,3]:
        return make_resp(UNSUPPORTED_GARBAGE_TYPE)

    ans = Garbage_add_info(data)
    resp = make_resp(ans)

    return resp

@manager.route('/get_garbage_nums', methods=['GET'])
def get_garbage_nums():
    ans,data = Garbage_nums_per_category()
    resp = make_resp(ans,data)
    return resp

@manager.route('/get_all_garbage_num', methods=['GET'])
def get_all_garbage_num():
    ans,data = Garbage_all_added()
    resp = make_resp(ans,data)
    return resp

@manager.route('/get_search_by_category', methods=['GET'])
def get_search_by_category():
    ans,data = Garbage_count_per_category()
    resp = make_resp(ans,data)
    return resp
# 如需查询某一类别（category_id)下的所有garbage信息，请调用routes/garbage.py下的show_one_category接口

@manager.route('/get_user_test_count', methods=['GET'])
def get_user_test_count():
    ans,data = Test_get_account_accuracy()
    resp = make_resp(ans,data)
    return resp

@manager.route('/get_que_test_count', methods=['GET'])
def get_que_test_count():
    ans, data = Test_get_garbage_account_accuracy()
    resp = make_resp(ans, data)
    return resp

@manager.route('/get_question_nums', methods=['GET'])
def get_question_nums():
    ans, data = Test_get_test_account_by_day()
    resp = make_resp(ans, data)
    return resp
