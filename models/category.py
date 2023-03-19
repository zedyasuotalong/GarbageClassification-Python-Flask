
from db_config import db_init as db

# 定义category模型类


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    info = db.Column(db.String(200), nullable=False)


def Model_commit():
    ans = 0
    try:
        db.session.commit()
    except:
        ans = 1
    return ans


def Model_add_category(category):
    try:
        db.session.add(category)
    except:
        return 1
    return Model_commit()
