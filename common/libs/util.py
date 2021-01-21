from application import app

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def generate_token(id):
    s = Serializer(app.config['SECRET_KEY'], expires_in=3600)
    token = s.dumps({'id': id}).decode('ascii')
    return token
