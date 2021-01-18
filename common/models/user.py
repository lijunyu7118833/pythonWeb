

from application import db

class User(db.Model):
    __tablename__ = 'user'
    user_Id = db.Column(db.String(50), primary_key=True)

    user_name = db.Column(db.String(200))
    password = db.Column(db.String(200))

