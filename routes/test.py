from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from error_code import *
from flask import Blueprint,request
import json

test = Blueprint('test',__name__)

from api.question import *

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