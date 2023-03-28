import time
import random
import threading
import time

from operation.user import User_opration
from utils.data_process import Class_To_Data
from utils.debug import DEBUG
from error_code import *
from utils.verify_code import send_code
import hashlib

##########################for verify_code##############################
VERIFY_CODE_INTERVAL = 3600
# 用于存储验证码的dict
# 格式是 {"18312341234" : {"code":1234, "time":1668931308.123456, "type":0/1/2}}
verify_code_dict = {}
t1 = None
lock = None
def create_timer():
    DEBUG(func='create_timer')
    global t1,lock
    lock.acquire() 
    for data in verify_code_dict:
        DEBUG(data=data)
        if (time.time() - verify_code_dict[data]['time']) > VERIFY_CODE_INTERVAL:
            verify_code_dict.pop(data)
    lock.release()
    t1 = threading.Timer(VERIFY_CODE_INTERVAL+VERIFY_CODE_INTERVAL/2, create_timer)
    t1.start()
def verify_code_help(phone,code):
    DEBUG(func='verify_code_help')
    ans = OK
    data = None

    global lock
    if not lock:
        lock = threading.Lock()
    lock.acquire()
    # check用户验证码是否存在
    if phone not in verify_code_dict or code != verify_code_dict[phone]['code']:
        ans = USER_VERIFY_CODE_ERROR
    # check用户验证码是否过期
    elif (time.time() - verify_code_dict[phone]['time']) > 3600:
        verify_code_dict.pop(phone)
        ans = USER_VERIFY_CODE_EXPIRED
    # 验证码正确
    else:
        # 注册的时候
        if verify_code_dict[phone]['type'] == 1:
            u_o = User_opration()
            ans,id = u_o._register(phone)
            DEBUG(register_ans=ans)
            DEBUG(register_id=id)
            if ans != 0:
                ans = REGISTER_USER_ERROR
            else:
                data = dict()
                data['id'] = id
        verify_code_dict.pop(phone)
    lock.release()
    return ans,data
########################################################

def User_list():
    DEBUG(func='api/User_list')

    u_o = User_opration()
    data = u_o._all()
    if data == []:
        return OK,data
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, u_o.__fields__, 0)
    DEBUG(data=data)
    return OK,data

# def User_reg(kwargs):
#     u_o = User_operation()
#     data = u_o._reg(kwargs)
#     return data

def User_login(login_type,account,pwd):
    DEBUG(func='api/User_login')

    # 检查用户手机号是否存在
    u_o = User_opration()
    data = u_o._login(account)
    if data is None:
        return USER_ACCOUNT_NONEXISTS,None
    data = Class_To_Data(data,u_o.__fields__, 1)
    if len(data) == 0:
        return USER_ACCOUNT_NONEXISTS,None
    id = dict()
    id['id'] = data['id']

    # 手机号，验证码登录
    if login_type == 0:
        ans,_ = verify_code_help(account,pwd)
        if ans == 0:
            return OK,id
        else:
            return ans,None
    
    # 手机号，密码登录
    if data['password'] is None:
        return USER_PASSWORD_NOTSET,None
    pwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
    if pwd != data['password']:
        return USER_PASSWORD_ERROR,None
    
    return OK,id

def User_send_verify_code(type, phone):
    DEBUG(func='api/User_send_verify_code')

    # 创建删除过期验证码的线程
    global t1,lock
    if not t1:
        lock = threading.Lock()
        t1 = threading.Timer(5, create_timer)
        t1.start()
    
    # 检查用户手机号是否存在
    u_o = User_opration()
    user_list = u_o._login(phone)
    if user_list is None:
        exists = False
    else:
        exists = True
    
    # type为0和2需要用户账户存在，1需要用户账户不存在
    if (type == 0 or type == 2) and exists == False:
        return USER_ACCOUNT_NONEXISTS
    elif type == 1 and exists == True:
        return USER_ACCOUNT_EXISTS
    
    # 发送验证码
    code = ""
    for _ in range(6):
        code += str(random.randint(0,9))
    ans = send_code(phone, code)
    if ans == OK:
        lock.acquire()
        verify_code_dict[phone] = {}
        verify_code_dict[phone]['code'] = code
        verify_code_dict[phone]['time'] = time.time()
        verify_code_dict[phone]['type'] = type
        # if DEBUG: print('send_verify_code:{}'.format(verify_code_dict))
        DEBUG(verify_code_dict=verify_code_dict)
        lock.release()
    
    return ans

def User_verify_verify_code(phone, verify_code):
    DEBUG(func='api/User_verify_verify_code')

    ans,data = verify_code_help(phone, verify_code)
    return ans,data

def User_change_info(id, dict_value):
    DEBUG(func='api/User_change_info')
    u_o = User_opration()
    ans = u_o._update(id, dict_value)
    return ans

def User_info(id, isMana=0):
    DEBUG(func='api/User_info')
    u_o = User_opration()
    data = u_o._info(id)
    if data is None:
        return USER_ACCOUNT_NONEXISTS,None
    
    data = Class_To_Data(data,u_o.__fields__, 1)
    DEBUG(data=data)
    if len(data) == 0:
        return USER_ACCOUNT_NONEXISTS,None
    if isMana == 0:
        # data.pop('id')
        # data.pop('level')
        data.pop('head_img')
        data.pop('password')
        # data.pop('reg_time')
    return OK,data

def User_delete_info(id):
    DEBUG(func='api/User_delete_info')
    u_o = User_opration()
    ans = u_o._delete(id)
    return ans

def User_added_by_time(start_time, end_time):
    DEBUG(func='api/User_added_by_time')

    u_o = User_opration()
    data = u_o._user_added_by_time(start_time, end_time)
    if data == []:
        return OK,data
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, ['time', 'nums'], 0)
    DEBUG(data=data)
    return OK,data

def User_all_added():
    DEBUG(func='api/User_added_by_time')

    u_o = User_opration()
    nums,day_num = u_o._user_all_added()
    if nums == []:
        return OK,{"nums":0,"day_num":0}
    # data（复杂对象）====> 数据
    nums = Class_To_Data(nums, ['time', 'nums'], 0)
    DEBUG(nums=nums)
    day_num = Class_To_Data(day_num, ['time', 'nums'], 0)
    DEBUG(day_num=day_num)
    data = dict()
    data['nums'] = nums[0]['nums']
    data['day_num'] = day_num[0]['nums']
    return OK,data

def User_added_by_sex():
    DEBUG(func='api/User_added_by_sex')

    tmp_data = [
        {"name":"男","value":0},
        {"name":"女","value":0}
    ]
    u_o = User_opration()
    data = u_o._user_by_sex()
    if data == []:
        return OK,tmp_data
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, ['name', 'value'], 0)
    DEBUG(data=data)

    for i in range(len(data)):
        tmp_data[data[i]['name']]['value'] = data[i]['value']

    return OK,tmp_data

def User_added_by_job():
    DEBUG(func='api/User_added_by_job')

    u_o = User_opration()
    data = u_o._user_by_job()
    if data == []:
        return OK,data
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, ['job', 'nums'], 0)
    DEBUG(data=data)
    return OK,data