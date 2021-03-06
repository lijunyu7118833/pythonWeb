from application import db


class Article(db.Model):
    __tablename__ = 'article'
    article_Id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)

    title = db.Column(db.String(200))
    content = db.Column(db.String(200))
    author = db.Column(db.String(200))
    tag = db.Column(db.String(200))
    like_count = db.Column(db.Integer)
    likes = db.Column(db.Integer)

    create_date = db.Column(db.DateTime)

