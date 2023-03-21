

from db_config import db_init as db
# 定义user模型类
class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    sex = db.Column(db.Integer, nullable=True, default=0)
    age = db.Column(db.Integer, nullable=True, default=20)
    phone = db.Column(db.String(16), nullable=False, unique=True)
    email = db.Column(db.String(32), nullable=True)
    job = db.Column(db.String(64), nullable=True)
    level = db.Column(db.Integer, nullable=True, default=0)
    head_img = db.Column(db.String(128), nullable=True)
    reg_time = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        # print('model')
        return '<User phone %s>' % self.phone

def Model_commit():
    ans = 0
    try:
        db.session.commit()
    except:
        ans = 1
    return ans

def Model_add_user(user):
    id = None
    try:
        db.session.add(user)
        id = user.id
    except:
        return 1,None
    ans = Model_commit()
    return ans,id

