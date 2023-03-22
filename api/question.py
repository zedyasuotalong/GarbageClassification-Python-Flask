import os

from operation.question import Question_opration
from utils.data_process import Class_To_Data
from utils.debug import DEBUG,ERROR
from error_code import *

def Question_list():
    DEBUG(func='api/Question_list')

    q_o = Question_opration()
    data = q_o._all()
    if data == []:
        return OK,data
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, q_o.__fields__, 0)
    DEBUG(data=data)
    return OK,data

def Question_info(id):
    DEBUG(func='api/Question_info')
    q_o = Question_opration()
    data = q_o._info(id)
    if data is None:
        return QUESTION_NONEXISTS,None
    
    data = Class_To_Data(data,q_o.__fields__, 1)
    DEBUG(data=data)
    if len(data) == 0:
        return QUESTION_NONEXISTS,None

    return OK,data

def Question_change_info(id, dict_value):
    DEBUG(func='api/Question_change_info')

    q_o = Question_opration()
    ans = q_o._update(id, dict_value)
    DEBUG(ans=ans)
    return ans
  
def Question_add(picture, answer, explains):
    DEBUG(func='api/Question_add')

    q_o = Question_opration()
    ans = q_o._add(picture, answer, explains)
    DEBUG(add_ans=ans)
    return ans

def Question_delete_info(id):
    DEBUG(func='api/Question_delete_info')
    q_o = Question_opration()
    ans = q_o._delete(id)

    return ans

def Question_get_for_test(num):
    DEBUG(func='api/Question_get_for_test')
    q_o = Question_opration()
    data = q_o._get_(num)
    if data is None:
        return QUESTION_NONEXISTS,None
    
    data = Class_To_Data(data,q_o.__fields__, 0)
    DEBUG(data=data)
    if len(data) == 0:
        return QUESTION_NONEXISTS,None

    return OK,data