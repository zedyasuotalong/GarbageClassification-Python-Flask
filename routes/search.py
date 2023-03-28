
from utils.debug import INFO,DEBUG
from utils.mk_response import make_resp
from error_code import *
from flask import Blueprint,request
import json

search = Blueprint('search', __name__)

from api.search import *

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


@search.route('/picture', methods=['POST'])
def picture_search():
    """
    ret_code, data = parse_json_data(request.data, ['picture'])

    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp
    """
    picture = request.files['file']
    # print(picture)
    # picture_bytes = picture.read()
    # picture = data['picture']
    print(picture)
    picture_name = picture.filename
    print(picture_name)
    picture_path = 'D:/企业实训/本地项目/GarbageClassification-Flask/static/' + picture_name
    print(picture_path)
    picture.save(picture_path)

    ans, data = Picture_search(picture_path)
    resp = make_resp(ans, data)

    return resp


@search.route('/keyword', methods=['POST'])
def keyword_search():
    ret_code, data = parse_json_data(request.data, ['name'])

    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp

    name = data['name']

    ans, data = Name_search(name)
    resp = make_resp(ans, data)

    return resp


@search.route('/hot_words', methods=['POST'])
def hot_words_search():
    ret_code, data = parse_json_data(request.data, ['number'])

    if ret_code != OK:
        resp = make_resp(ret_code)
        return resp

    number = data['number']
    number = int(number)

    ans, data = Hot_search(number)
    resp = make_resp(ans, data)

    return resp