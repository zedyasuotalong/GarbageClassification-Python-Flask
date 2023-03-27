import os

from operation.test import Test_operation
from utils.data_process import Class_To_Data
from utils.debug import DEBUG,ERROR
from error_code import *
import datetime

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
    data = Class_To_Data(data, ['picture','answer','explains','my_answer','score'], 0)
    DEBUG(data=data)
    return OK,data
def Test_get_account_accuracy():
    DEBUG(func='api/Test_get_account_accuracy')

    t_o = Test_operation()
    t_o._update_score()
    users = t_o._get_user_id()  # 元素为user_id的list
    DEBUG(users=users)
    if users == []:
        return OK, users

    accuracy = []
    for user_id in users:
        DEBUG(user_id_0=user_id[0])
        data = t_o._user_test_account(user_id[0])
        if users == []:
            continue
        data = Class_To_Data(data, ['name', 'sum', 'right_num'], 0)
        if users == []:
            continue
        accuracy.append({'name': data[0]['name'],
                         'sum': data[0]['sum'],
                         'accuracy': round(int(data[0]['right_num']) / data[0]['sum'] * 100, 2)})

    return OK, accuracy


def Test_get_garbage_account_accuracy():
    DEBUG(func='api/Test_get_garbage_account_accuracy')

    tmp_data = [
        {"name": "干垃圾", "sum": 0, "accuracy": 0},
        {"name": "湿垃圾", "sum": 0, "accuracy": 0},
        {"name": "可回收物", "sum": 0, "accuracy": 0},
        {"name": "有害垃圾", "sum": 0, "accuracy": 0}
    ]

    t_o = Test_operation()
    data = t_o._question_account_per_category()
    if data == []:
        return OK, data
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, ['name', 'sum', 'right_num'], 0)
    DEBUG(data=data)

    for i in range(len(data)):
        tmp_data[data[i]['name']]['sum'] = int(data[i]['sum'])
        tmp_data[data[i]['name']]['accuracy'] = round(int(data[i]['right_num']) / data[i]['sum'] * 100, 2)

    return OK, tmp_data


def Test_get_test_account_by_day():
    DEBUG(func='api/Test_get_test_account_by_day')

    today = str(datetime.datetime.today()).split()[0]
    DEBUG(today=today)
    tmp_data = {"sum": 0, "test_count": 0, "accuracy": 0}

    t_o = Test_operation()
    today_num = t_o._test_done_by_day(today)
    all_num = t_o._test_all_be_done()
    if today_num == []:
        return OK, today_num
    elif all_num == []:
        return OK, all_num

    today_num = Class_To_Data(today_num, ['num'], 0)
    DEBUG(today_num=today_num)
    all_num = Class_To_Data(all_num, ['num', 'right_num'], 0)
    DEBUG(all_num=all_num)

    tmp_data["sum"] = all_num[0]['num']
    tmp_data["test_count"] = today_num[0]['num']
    tmp_data["accuracy"] = round(int(all_num[0]['right_num'])*1.0 / all_num[0]['num'] * 100, 2)

    return OK, tmp_data
