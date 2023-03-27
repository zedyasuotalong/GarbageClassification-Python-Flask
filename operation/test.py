from models.test import *
from models.question import *
from models.user import *
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
        DEBUG(test_list=test_list)
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

    def _update_score(self):
        DEBUG(func='Test_opration/_update_score')
        right = Tests.query.join(Questions, Tests.question_id == Questions.id).filter(
            Tests.my_answer == Questions.answer)
        if right is None:
            return TEST_NONEXISTS
        try:
            ans = right.update({Tests.score: 1})
        except:
            ans = 0
        DEBUG(update_ans=ans)
        if ans != 1:
            return CHANGE_TEST_INFO_ERROR

        wrong = Tests.query.join(Questions, Tests.question_id == Questions.id).filter(
            Tests.my_answer != Questions.answer)
        if wrong is None:
            return TEST_NONEXISTS
        try:
            ans = wrong.update({Tests.score: 0})
        except:
            ans = 0
        DEBUG(update_ans=ans)
        if ans != 1:
            return CHANGE_TEST_INFO_ERROR

        ans = Model_commit()
        DEBUG(commit_ans=ans)
        if ans != 0:
            return CHANGE_TEST_INFO_ERROR
        return ans

    def _get_user_id(self):
        DEBUG(func='Test_operation/_get_user_id')
        users = db.session.query(distinct(Tests.user_id)).all()
        DEBUG(users=users)
        return users

    def _user_test_account(self, user_id):
        DEBUG(func='Test_operation/_user_test_account')
        # data = db.session.query(Users.phone.label('name'), func.count('*').label('num'),
        #                         func.sum(Tests.score).label('right_num')) \
        #     .filter(Users.id == user_id, Tests.user_id == user_id)
        data = db.session.query(Users.phone.label('name'), func.count('*').label('sum'),
                                func.sum(Tests.score).label('right_num')).join(Tests) \
            .filter(Users.id == user_id)
        DEBUG(data=data)
        return data

    def _question_account_per_category(self):
        DEBUG(func='Test_operation/_question_account_per_category')
        # data = db.session.query(Questions.answer.label('name'), func.count('*').label('num'),
        #                         func.sum(Tests.score).label('right_num')) \
        #     .join(Questions, Tests.question_id == Questions.id).group_by(Questions.answer).order_by('name')
        data = db.session.query(Questions.answer.label('name'), func.count('*').label('sum'),
                                func.sum(Tests.score).label('right_num')) \
            .join(Tests).group_by(Questions.answer).order_by('name')
        DEBUG(data=data)
        return data

    def _test_all_be_done(self):
        DEBUG(func='Test_operation/_test_all_be_done')
        data = db.session.query(func.count('*').label('num'), func.sum(Tests.score).label('right_num'))
        DEBUG(data=data)
        return data

    def _test_done_by_day(self, today):
        DEBUG(func='Test_operation/_test_done_by_day')
        data = db.session.query(func.count('*').label('num')).filter(Tests.time == today)
        DEBUG(data=data)
        return data
