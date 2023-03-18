from db_config import db_init as db

# 定义category模型类


class Questions(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    picture = db.Column(db.String(128), nullable=False)
    answer = db.Column(db.Integer, nullable=False)
    explains = db.Column(db.String(512), nullable=True)
    status = db.Column(db.Integer, default=0)

    def __repr__(self):
        # print('model')
        return '<Question picture %s>' % self.picture


def Model_commit():
    ans = 0
    try:
        db.session.commit()
    except:
        ans = 1
    return ans


def Model_add_question(question):
    id = None
    try:
        db.session.add(question)
    except:
        return 1
    return Model_commit()