
from operation.search import Search_operation
from operation.category import Category_operation
from utils.data_process import Class_To_Data
from utils.debug import DEBUG, ERROR
from error_code import *
from model.predict import predict_category


def Picture_search(picture_path):
    DEBUG(func='api/Picture_search')

    s_o = Search_operation()
    c_o = Category_operation()
    print(picture_path)
    id = predict_category(picture_path)  # 此处picture为图片文件而非图片地址，但predict_category中接收的是图片地址，有待修改
    if id <= 105:
        category_id = 2
    elif id <= 141:
        category_id = 0
    elif id <= 160:
        category_id = 3
    else:
        category_id = 1

    ans, data1 = s_o._id_search(id)
    DEBUG(ans=ans)
    if data1 is None:
        return ans, None

    data1 = Class_To_Data(data1, s_o.__fields__, 1)
    DEBUG(data1=data1)

    ans, data2 = c_o._category_id_search(category_id)
    DEBUG(ans=ans)
    if data2 is None:
        return ans, None

    data2 = Class_To_Data(data2, c_o.__fields__, 1)
    DEBUG(data2=data2)

    data = dict()
    data['garbage_name'] = data1['name']
    data['garbage_info'] = data1['info']
    data['garbage_category_id'] = data1['category_id']
    data['garbage_category_name'] = data2['name']
    data['garbage_category_info'] = data2['info']

    return ans, data


def Name_search(name):
    DEBUG(func='api/Name_search')

    s_o = Search_operation()
    ans, data = s_o._name_search(name)
    DEBUG(ans=ans)
    if data is None:
        return ans, None

    data = Class_To_Data(data, s_o.__fields__, 0)
    DEBUG(data=data)
    for number in range(len(data)):
        del data[number]['id']
        del data[number]['count']

    return ans, data


def Hot_search(number):
    DEBUG(func='api/Hot_search')

    s_o = Search_operation()
    ans, data = s_o._hot_search(number)
    data = Class_To_Data(data, s_o.__fields__, 0)
    DEBUG(ans=ans)
    DEBUG(data=data)

    for i in range(number):
        data[i] = data[i]['name']

    return ans, data
