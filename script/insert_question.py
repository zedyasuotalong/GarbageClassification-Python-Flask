import os
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='test_user', password='123.com', \
  database='garbage_classification', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
conn.autocommit(1)

map_tb = {
  '充电头':'chongdiantou',
  '勺子':'shaozi',
  '报纸':'baozhi',
  '打火机':'dahuoji',
  '眼镜':'yanjing',
  '电池':'dianchi',
  '梨':'li',
  '苹果':'pingguo'
}
answer_tb = {
  '充电头':2,
  '勺子':2,
  '报纸':2,
  '打火机':0,
  '眼镜':0,
  '电池':3,
  '梨':1,
  '苹果':1
}
DEST_DIR = '../static/question/'
SRC_DIR = [
  ['../static/question/test_image/可回收垃圾_充电头',40],
  ['../static/question/test_image/可回收垃圾_勺子',40],
  ['../static/question/test_image/可回收垃圾_报纸',20],
  ['../static/question/test_image/干垃圾_打火机',20],
  ['../static/question/test_image/干垃圾_眼镜',20],
  ['../static/question/test_image/有害垃圾_电池',20],
  ['../static/question/test_image/湿垃圾_梨',20],
  ['../static/question/test_image/湿垃圾_苹果',20],
]

def help(src_dir, nums, dest_dir):
  files = os.listdir(src_dir)
  for i in range(nums):
    zh_name = src_dir.split('_')[-1]

    answer = answer_tb[zh_name]

    # new_file = files[i][4:].replace(zh_name, map_tb[zh_name])
    new_file = map_tb[zh_name]+'_'+files[i].split('_')[-1]

    old = os.path.join(src_dir,files[i])
    new = os.path.join(dest_dir,new_file)
    os.system('cp -f {} {}'.format(old, new))
    sql = f"insert into question(picture,answer,explains) values('{new_file}',{answer},'{files[i].split('_')[1]}')"
    print(sql)
    cursor.execute(sql)
    # break

if __name__ == '__main__':
  for i in range(len(SRC_DIR)):  
    help(SRC_DIR[i][0], SRC_DIR[i][1], DEST_DIR)

  cursor.close()
  conn.close()