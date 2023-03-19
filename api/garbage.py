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

    if len(data) == 0:
        return GARBAGE_INFO_NONEXISTS, None

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
