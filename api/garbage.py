import time
import random
import threading
import time

from operation.garbage import Garbage_operation
from utils.data_process import Class_To_Data
from utils.debug import DEBUG
from error_code import *


def Garbage_showOneCategory(category_id):
    DEBUG(func='api/User_list')
    g_o = Garbage_operation()
    data = g_o._sort(category_id)

    if data is None:
        return GARBAGE_INFO_NONEXISTS, None

    data = Class_To_Data(data, g_o.__fields__, 0)
    DEBUG(data=data)

    # if len(data) == 0:
    #     return GARBAGE_INFO_NONEXISTS, None

    return OK, data


def Garbage_list():
    DEBUG(func='api/Garbage_list')
    g_o = Garbage_operation()
    data = g_o._all()

    if data == []:
        return OK, data
    data = Class_To_Data(data, g_o.__fields__, 0)

    DEBUG(data=data)
    return OK, data

def Garbage_info(id):
    DEBUG(func='api/Garbage_info')
    g_o = Garbage_operation()
    data = g_o._info(id)
    if data is None:
        return GARBAGE_INFO_NONEXISTS,None

    data = Class_To_Data(data,g_o.__fields__, 1)
    DEBUG(data=data)
    if len(data) == 0:
        return GARBAGE_INFO_NONEXISTS,None
    return OK,data

def Garbage_change_info(id, dict_value):
    DEBUG(func='api/Garbage_change_info')
    g_o = Garbage_operation()
    ans = g_o._update(id, dict_value)
    return ans


def Garbage_delete_info(id):
    DEBUG(func='api/Garbage_delete_info')
    g_o = Garbage_operation()
    ans = g_o._delete(id)
    return ans


def Garbage_add_info(dict_value):
    DEBUG(func='api/Garbage_add')
    g_o = Garbage_operation()
    ans = g_o._add(dict_value)
    return ans

def Garbage_nums_per_category():
    DEBUG(func='api/Garbage_nums_per_category')

    tmp_data = [
        {"name":"干垃圾","value":0},
        {"name":"湿垃圾","value":0},
        {"name":"可回收物","value":0},
        {"name":"有害垃圾","value":0}
    ]
    g_o = Garbage_operation()
    data = g_o._nums_per_category()
    if data == []:
        return OK,tmp_data
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, ['name', 'value'], 0)
    DEBUG(data=data)

    for i in range(len(data)):
        tmp_data[data[i]['name']]['value'] = data[i]['value']

    return OK,tmp_data

def Garbage_all_added():
    DEBUG(func='api/User_added_by_time')

    g_o = Garbage_operation()
    nums = g_o._garbage_all_added()
    if nums == []:
        return OK,{"nums":0}
    # data（复杂对象）====> 数据
    nums = Class_To_Data(nums, ['id', 'nums'], 0)
    DEBUG(nums=nums)
    data = dict()
    data['nums'] = nums[0]['nums']
    return OK,data

def Garbage_count_per_category():
    DEBUG(func='api/Garbage_count_per_category')

    tmp_data = [
        {"name":"干垃圾","count":0},
        {"name":"湿垃圾","count":0},
        {"name":"可回收物","count":0},
        {"name":"有害垃圾","count":0}
    ]
    g_o = Garbage_operation()
    data = g_o._counts_per_category()
    if data == []:
        return OK,tmp_data
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, ['name', 'count'], 0)
    DEBUG(data=data)

    for i in range(len(data)):
        tmp_data[data[i]['name']]['count'] = int(data[i]['count'])

    return OK,tmp_data