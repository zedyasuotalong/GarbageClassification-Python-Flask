
from db_config import db_init as db

class Manager(db.Model):
    __tablename__ = 'manager'
    username = db.Column(db.String(16), nullable=False, primary_key=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        # print('model')
        return '<manager %s>' % self.username