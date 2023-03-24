import os

from operation.test import Test_operation
from utils.data_process import Class_To_Data
from utils.debug import DEBUG,ERROR
from error_code import *

def Test_list():
    DEBUG(func='api/Test_list')

    t_o = Test_operation()
    data = t_o._all()
    if data == []:
        return OK,data
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, t_o.__fields__, 0)
    DEBUG(data=data)
    return OK,data

def Test_info(id):
    DEBUG(func='api/Test_info')
    t_o = Test_operation()
    data = t_o._info(id)
    if data is None:
        return TEST_NONEXISTS,None
    
    data = Class_To_Data(data,t_o.__fields__, 1)
    DEBUG(data=data)
    if len(data) == 0:
        return TEST_NONEXISTS,None

    return OK,data
  
def Test_add(dict_value):
    DEBUG(func='api/Test_add')

    t_o = Test_operation()
    ans = t_o._add(dict_value)
    DEBUG(add_ans=ans)
    return ans

def Test_delete_info(id):
    DEBUG(func='api/Test_delete_info')
    t_o = Test_operation()
    ans = t_o._delete(id)

    return ans

def Test_get_wrong_question(user_id):
    DEBUG(func='api/Test_get_wrong_question')

    t_o = Test_operation()
    data = t_o._wrong_question(user_id=user_id)
    if data == []:
        return OK,data
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, ['picture','answer','explains','myAnswer','score'], 0)
    DEBUG(data=data)
    return OK,data