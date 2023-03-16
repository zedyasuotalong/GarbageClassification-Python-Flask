from models.garbage import *
from utils.debug import DEBUG
from error_code import *


class Garbage_operation():
    def __init__(self):
        DEBUG(func='Garbage_operation/__init__')
        self.__fields__ = ['id', 'name', 'time', 'type', 'info', 'count']

    def _all(self):
        DEBUG(func='Garbage_operation/_all')
        garbage_list = Garbages.query.all()
        DEBUG(garbage_list=garbage_list)
        return garbage_list

    def _sort(self, category_id):
        DEBUG(func='Garbage_operation/_sort')
        garbage_list = Garbages.query.filter_by(category_id=category_id)
        DEBUG(garbage_list=garbage_list)
        return garbage_list

    def _update(self, id, dict_value):
        DEBUG(func='Garbage_operation/_sort')
        data = Garbages.query.filter_by(id=id)
        if data.first() is None:
            return GARBAGE_INFO_NONEXISTS
        try:
            ans = data.update(dict_value) # ans should be 1
        except:
            ans = 0
        DEBUG(update_ans=ans)
        if ans != 1:
            return GARBAGE_CHANGE_INFO_ERROR

        ans = Model_commit()
        DEBUG(commit_ans=ans)
        return ans