from utils.debug import DEBUG
from error_code import *
from operation.manager import Manager_opration
from utils.data_process import Class_To_Data

def Manager_login(username, password):
    DEBUG(func='api/Manager_login')

    # 检查用户手机号是否存在
    m_o = Manager_opration()
    data = m_o._login(username)
    if data is None:
        return USER_ACCOUNT_NONEXISTS
    
    # 手机号，密码登录
    data = Class_To_Data(data,m_o.__fields__, 1)
    if len(data) == 0:
        return USER_ACCOUNT_NONEXISTS
    if data['password'] is None:
        return USER_PASSWORD_NOTSET
    if password != data['password']:
        return USER_PASSWORD_ERROR
    
    return OK

def Manager_change_password(username, password, new_password):
    DEBUG(func='api/Manager_change_password')

    m_o = Manager_opration()
    ans = m_o._update(username, password, new_password)
    
    return ans