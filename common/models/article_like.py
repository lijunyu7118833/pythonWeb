from application import db


class Article_like(db.Model):
    __tablename__ = 'article_like'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer)
    article_id = db.Column(db.Integer)
    likes = db.Column(db.Integer)
