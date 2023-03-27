from models.test import *
from models.question import *
from utils.debug import DEBUG
from error_code import *
from sqlalchemy import func,distinct
from datetime import datetime
from db_config import db_init as db
# lei
class Test_operation():
    def __init__(self):
        DEBUG(func='Test_operation/__init__')
        self.__fields__ = ['id','question_id','user_id','my_answer','time','score'] 

    def _all(self):
        DEBUG(func='Test_operation/_all')
        test_list = Tests.query.all()
        DEBUG(qtest_list=test_list)
        return test_list
    
    def _info(self, id):
        DEBUG(func='Test_operation/_info')
        test = Tests.query.filter_by(id=id).first()
        DEBUG(test=test)
        return test
    
    def _update(self, id, dict_value):
        DEBUG(func='Question_opration/_update')
        data = Tests.query.filter_by(id=id)
        
        if data.first() is None:
            return QUESTION_NONEXISTS
        try:
            ans = data.update(dict_value) # ans should be 1
        except:
            ans = 0
        
        DEBUG(update_ans=ans)
        if ans != 1:
            return CHANGE_QUESTION_INFO_ERROR

        ans = Model_commit()
        DEBUG(commit_ans=ans)
        if ans != 0:
            return CHANGE_QUESTION_INFO_ERROR
        return ans

    def _add(self, dict_value):
        DEBUG(func='Test_operation/_add')
        time_str = str(datetime.now())[0:10]
        test = Tests(question_id=dict_value['question_id'], user_id=dict_value['user_id'], \
            my_answer=dict_value['my_answer'], score=dict_value['score'], time=time_str)
        ans = Model_add_test(test)
        DEBUG(test_id=test.id)
        if ans!= 0:
            return ADD_TEST_INFO_ERROR

        return ans
    def _wrong_question(self, user_id):
        DEBUG(func='Test_operation/_wrong_question')
        # test = Tests.query.filter_by(id=user_id).all()
        test = db.session.query(distinct(Questions.picture).label('picture'),(Questions.answer),\
            (Questions.explains),(Tests.my_answer),(Tests.score)).\
            join(Tests).filter(Tests.user_id==user_id,Tests.score==0)
        DEBUG(test=test)
        return test