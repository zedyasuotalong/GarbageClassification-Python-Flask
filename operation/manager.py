from models.manager import *
from models.user import Model_commit
from utils.debug import DEBUG
from error_code import *

class Manager_opration():
    def __init__(self):
        DEBUG(func='Manager_opration/__init__')
        self.__fields__ = ['username','password'] 
    
    def _login(self, username):
        DEBUG(func='Manager_opration/_login')
        manager_list = None
        manaegr_list = Manager.query.filter_by(username=username).first()
        DEBUG(manaegr_list=manaegr_list)

        return manaegr_list
    
    def _update(self, username, password, newPassword):
        DEBUG(func='Manager_opration/_update')
        data = Manager.query.filter_by(username=username).first()
        if data is None:
            return USER_ACCOUNT_NONEXISTS
        data = Manager.query.filter_by(username=username, password=password)
        if data.first() is None:
            return USER_PASSWORD_ERROR
        dict_value = dict()
        dict_value['password'] = newPassword
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