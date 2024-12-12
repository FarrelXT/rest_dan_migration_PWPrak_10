from app.modelele import db
from datetime import datetime


class todos(db.Model):
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=True)
    todo = db.Column(db.String(230), nullable=False)
    description = db.Column(db.String(230), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Todo >'.format(self.todo)