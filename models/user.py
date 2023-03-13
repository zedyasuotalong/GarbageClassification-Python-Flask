

from db_config import db_init as db
# 定义user模型类
class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    sex = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    phone = db.Column(db.String(16), nullable=False, unique=True)
    email = db.Column(db.String(32), nullable=True)
    job = db.Column(db.String(64), nullable=True)
    isMana = db.Column(db.Integer, nullable=True)
    level = db.Column(db.Integer, nullable=True)
    head_img = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        # print('model')
        return '<User %s>' % self.name

