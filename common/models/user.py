from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from application import app

from application import db
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    __tablename__ = 'user'
    user_Id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)

    user_name = db.Column(db.String(200))
    password = db.Column(db.String(200))

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.user_name}).decode()

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)