# 安装mysql5.6 8.x    安装界面化操作工具Navicate Heidsql 
# 1、pip install pymysql
# 2、pip install Flask-SQLAlchemy


# --------------------配置数据库---------------------
from flask_sqlalchemy  import SQLAlchemy
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)
# 数据库配置                                               用户名：密码@ip：port/数据库名字
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test_user:123.com@127.0.0.1:3306/garbage_classification'

# 数据库操作对象
db_init = SQLAlchemy(app)

