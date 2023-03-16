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

    data = Class_To_Data(data, g_o.__fields__, 1)
    DEBUG(data=data)

    if len(data) == 0:
        return GARBAGE_INFO_NONEXISTS, None

    return OK, data