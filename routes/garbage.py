
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


@garbage.route('/show_one_category', methods=['POST'])
def show_one_category():
    ret_code, data = parse_json_data(request.data, ['category_id'])

    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp

    category_id = data['category_id']
    if data['category_id'] not in [0, 1, 2, 3]:
        resp = make_resp(UNSUPPORTED_GARBAGE_TYPE)
        return resp

    ans, data = Garbage_showOneCategory(category_id)
    DEBUG(ans=ans)
    DEBUG(data=data)
    resp = make_resp(ans, data)

    return resp



