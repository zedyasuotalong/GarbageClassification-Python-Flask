from models.user import Users
from utils.debug import DEBUG
# lei
class User_opration():
    def __init__(self):
        DEBUG(func='User_opration/__init__')
        self.__fields__ = ['id','name','password','sex','age','phone','email','job','isMana','level','head_img'] 

    def _all(self):
        DEBUG(func='User_opration/_all')
        user_list = Users.query.all()
        DEBUG(user_list=user_list)
        return user_list
    
    def _login(self, loginType, account, pwd):
        DEBUG(func='User_opration/_login')
        user_list = None
        if loginType == 0 or loginType == 1:
            user_list = Users.query.filter_by(phone=account).first()
        else:
            user_list = Users.query.filter_by(email=account).first()

        return user_list