from models.category import *
from utils.debug import DEBUG
from error_code import *

class Category_operation():
    def __init__(self):
        DEBUG(func='Category_operation/__init__')
        self.__fields__ = ['id', 'name', 'info']

    def _category_id_search(self, category_id):
        DEBUG(func='Category_operation/_category_id_search')
        category_info = Category.query.filter_by(id=category_id)
        if category_info.first() is None:
            return SEARCH_RESULTS_NONEXISTS, None
        category_info = category_info.first()
        DEBUG(category_info=category_info)
        return OK, category_info