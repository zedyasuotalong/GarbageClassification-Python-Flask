from db_config import db_init as db

# 定义test模型类


class Tests(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    my_answer = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String(32), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        # print('model')
        return '<test_id %s question_id %s user_id %s>' % (self.id,self.question_id,self.user_id)


def Model_commit():
    ans = 0
    try:
        db.session.commit()
    except:
        ans = 1
    return ans


def Model_add_test(test):
    id = None
    try:
        db.session.add(test)
    except:
        return 1
    return Model_commit()