from models.user import *
from utils.debug import DEBUG
from error_code import *
from datetime import datetime

from db_config import db_init as db
from sqlalchemy import func
# lei
class User_opration():
    def __init__(self):
        DEBUG(func='User_opration/__init__')
        self.__fields__ = ['id','name','password','sex','age','phone','email','job','level','head_img','reg_time'] 

    def _all(self):
        DEBUG(func='User_opration/_all')
        user_list = Users.query.all()
        DEBUG(user_list=user_list)
        return user_list
    
    def _info(self, id):
        DEBUG(func='User_opration/_info')
        user_list = Users.query.filter_by(id=id).first()
        DEBUG(user_list=user_list)
        return user_list
    
    def _login(self, account):
        DEBUG(func='User_opration/_login')
        user_list = None
        user_list = Users.query.filter_by(phone=account).first()
        DEBUG(user_list=user_list)

        return user_list

    def _exists(self, phone):
        DEBUG(func='User_opration/_exists')
        # 目前只支持手机号，不支持邮箱登录
        user_list = Users.query.filter_by(phone=phone).first()
        DEBUG(user_list=user_list)

        return user_list
    
    def _register(self, phone):
        DEBUG(func='User_opration/_register')
        time_str = str(datetime.now())[0:10]
        DEBUG(time=datetime.now())
        user = Users(phone=phone,reg_time=time_str)
        ans,id = Model_add_user(user)
    
        return ans,id
    
    def _update(self, id, dict_value):
        DEBUG(func='User_opration/_update')
        data = Users.query.filter_by(id=id)
        if data.first() is None:
            return USER_ACCOUNT_NONEXISTS
        try:
            ans = data.update(dict_value) # ans should be 1
        except:
            ans = 0
        DEBUG(update_ans=ans)
        if ans != 1:
            return CHANGE_USER_INFO_ERROR

        ans = Model_commit()
        DEBUG(commit_ans=ans)
        if ans != 0:
            return CHANGE_USER_INFO_ERROR
        return ans
    
    def _delete(self, id):
        DEBUG(func='User_opration/_delete')
        data = Users.query.filter_by(id=id)
        if data.first() is None:
            return USER_ACCOUNT_NONEXISTS
        try:
            ans = data.delete() # ans should be 1
        except:
            ans = 0
        DEBUG(update_ans=ans)
        if ans != 1:
            return DELETE_USER_INFO_ERROR

        ans = Model_commit()
        DEBUG(commit_ans=ans)
        if ans != 0:
            return DELETE_USER_INFO_ERROR
        return ans
    def _user_added_by_time(self):
        DEBUG(func='User_opration/_user_added_by_time')
        data = db.session.query(Users.reg_time.label('time'), func.count('*').label('nums')).group_by(Users.reg_time).order_by('time')
        DEBUG(data=data)
        return data