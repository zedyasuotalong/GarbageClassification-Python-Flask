from models.question import *
from utils.debug import DEBUG
from error_code import *
# lei
class Question_opration():
    def __init__(self):
        DEBUG(func='Question_opration/__init__')
        self.__fields__ = ['id','picture','answer','explains','status'] 

    def _all(self):
        DEBUG(func='Question_opration/_all')
        question_list = Questions.query.all()
        DEBUG(question_list=question_list)
        return question_list
    
    def _info(self, id):
        DEBUG(func='Question_opration/_info')
        question = Questions.query.filter_by(id=id).first()
        DEBUG(question=question)
        return question
    
    def _update(self, id, dict_value):
        DEBUG(func='Question_opration/_update')
        data = Questions.query.filter_by(id=id)
        
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

    def _add(self, picture, answer, explains):
        DEBUG(func='Question_opration/_add')
        question = Questions(picture=picture,answer=answer,explains=explains,status=0)
        ans = Model_add_question(question)
        DEBUG(question_id=question.id)
        if ans!= 0:
            return ADD_QUESTION_INFO_ERROR

        return ans
            
    def _delete(self, id):
        DEBUG(func='Question_opration/_delete')
        data = Questions.query.filter_by(id=id)
        if data.first() is None:
            return QUESTION_NONEXISTS
        try:
            ans = data.delete() # ans should be 1
        except:
            ans = 0
        DEBUG(update_ans=ans)
        if ans != 1:
            return DELETE_QUESTION_INFO_ERROR

        ans = Model_commit()
        DEBUG(commit_ans=ans)
        if ans!= 0:
            return DELETE_QUESTION_INFO_ERROR
        return ans
    
