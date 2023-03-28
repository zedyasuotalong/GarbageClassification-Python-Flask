from models.garbage import *
from utils.debug import DEBUG
from error_code import *


class Search_operation():
    def __init__(self):
        DEBUG(func='Search_operation/__init__')
        self.__fields__ = ['id', 'name', 'category_id', 'info', 'count']

    def _id_search(self, id):
        DEBUG(func='Search_operation/_id_search')
        garbage_info = Garbages.query.filter_by(id=id)
        if garbage_info.first() is None:
            return SEARCH_RESULTS_NONEXISTS, None
        try:
            ans = garbage_info.update({Garbages.count: Garbages.count+1}) # ans should be 1
        except:
            ans = 0
        DEBUG(update_ans=ans)
        if ans != 1:
            return COUNT_INCREASE_ERROR, None

        ans = Model_commit()
        DEBUG(commit_ans=ans)
        if ans != 0:
            return COUNT_INCREASE_ERROR, None

        garbage_info = garbage_info.first()
        DEBUG(garbage_info=garbage_info)
        return ans, garbage_info

    def _name_search(self, name):
        DEBUG(func='Search_operation/_name_search')
        garbage_info = Garbages.query.filter(Garbages.name.like('%' + name + '%'))
        if garbage_info.first() is None:
            return SEARCH_RESULTS_NONEXISTS, None
        try:
            ans = garbage_info.update({Garbages.count: Garbages.count+1})
        except:
            ans = 0
        DEBUG(update_ans=ans)
        ans = Model_commit()
        DEBUG(commit_ans=ans)
        if ans != 0:
            return COUNT_INCREASE_ERROR, None

        garbage_info = garbage_info.all()
        DEBUG(garbage_info=garbage_info)
        return ans, garbage_info

    def _hot_search(self, number):
        DEBUG(func='Search_operation/_hot_search')
        garbage_info = Garbages.query.order_by(Garbages.count.desc()).limit(number).all()
        DEBUG(garbage_info=garbage_info)
        return OK, garbage_info

