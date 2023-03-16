from datetime import datetime
from db_config import db_init as db

# 定义garbage模型类


class Garbages(db.Model):
    __tablename__ = 'garbage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    time = db.Column(db.Datetime, default=datetime.date())
    category_id = db.Column(db.Interger, nullable=False)
    info = db.Column(db.String(200), nullable=False)
    count = db.Column(db.Integer, nullable=False, default=0)
    __table_args__ = (db.CheckConstraint(category_id.in_([0, 1, 2, 3])))


def Model_commit():
    ans = 0
    try:
        db.session.commit()
    except:
        ans = 1
    return ans


def Model_add_garbage(garbage):
    try:
        db.session.add(garbage)
    except:
        return 1
    return Model_commit()