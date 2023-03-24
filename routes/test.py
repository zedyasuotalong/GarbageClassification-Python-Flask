from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from error_code import *
from flask import Blueprint,request
import json

test = Blueprint('test',__name__)

from api.question import Question_get_for_test
from api.test import *

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

@test.route('/one',methods=['GET'])
def one():
    ans,data = Question_get_for_test(1)
    DEBUG(ans=ans)
    DEBUG(data=data)
    if ans == 0 and len(data) > 0:
      data = data[0]
    resp = make_resp(ans,data)

    return resp

@test.route('/ten',methods=['GET'])
def ten():
    ans,data = Question_get_for_test(10)
    DEBUG(ans=ans)
    DEBUG(data=data)
    resp = make_resp(ans,data)

    return resp

@test.route('/submit_one',methods=['POST'])
def submit_one():
    ret_code, data = parse_json_data(request.data, ['question_id', 'user_id', 'myAnswer', 'score'])

    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp
    ans = Test_add(data)
    DEBUG(ans=ans)
    resp = make_resp(ans)

    return resp

@test.route('/submit_ten',methods=['POST'])
def submit_ten():
    try:
        data = json.loads(request.data) # data is json
    except: # data is not json
        print()
        return make_resp(REQUEST_DATA_FORMAT_ERROR)

    for d in data:
        for key in ['question_id', 'user_id', 'myAnswer', 'score']:
            if key not in d:
                return make_resp(MISSING_REQUIRED_PARAMS)
    for d in data:
        ans = Test_add(d)
        DEBUG(ans=ans)
        if ans!= 0:
            return make_resp(ans)
    resp = make_resp(ans)

    return resp

@test.route('/wrong_question',methods=['POST'])
def wrong_question():
    ret_code, data = parse_json_data(request.data, ['id'])

    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp
        
    ans,data = Test_get_wrong_question(data['id'])
    DEBUG(ans=ans)
    DEBUG(data=data)
    resp = make_resp(ans,data)

    return resp