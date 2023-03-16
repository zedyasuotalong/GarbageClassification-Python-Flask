from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from error_code import *
from flask import Blueprint,request
import json

garbage = Blueprint('garbage', __name__)

from api.garbage import *


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
    return OK, data


@garbage.route('/garbage_list_one', methods=['POST'])
def garbage_list_one():
    ret_code, data = parse_json_data(request.data, ['type'])

    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp

    type = data['type']
    if data['type'] not in [0, 1, 2, 3]:
        resp = make_resp(UNSUPPORTED_GARBAGE_TYPE)
        return resp

    ans, data = Garbage_showOneCategory(type)
    DEBUG(ans=ans)
    DEBUG(data=data)
    resp = make_resp(ans, data)

    return resp


