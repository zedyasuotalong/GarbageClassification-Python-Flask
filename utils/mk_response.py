from flask import make_response
import json
from error_code import *
from utils.debug import *

def make_resp(code : int, resp_data : dict):
  data = dict()
  data['status'] = code
  data['msg'] = CODE_STR[code]
  if resp_data:
    data['data'] = resp_data
  if code != 0:
    ERROR(error_code=code, error_msg=CODE_STR[code])
  else: 
    INFO(response_data=data)
  resp = make_response(json.dumps(data, ensure_ascii=True))
  resp.headers['Content-Type'] = 'application/json'
  return resp