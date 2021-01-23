from flask import Blueprint, request, jsonify, json
from operator import and_, __or__, or_
from common.models.user import User
from common.libs.queryToDict import *
from common.models.article import Article
from common.models.article_like import Article_like

from application import db
import datetime

route_article = Blueprint('article', __name__)


@route_article.route("/find", methods=["GET", "POST"])
def find():
    resp = {"errMsg": "查询成功", "data": "", "token": ""}
    req = request.get_json()
    body = req['body'] if 'body' in req else ''
    user_id = req['user_id'] if 'user_id' in req else ''

    if not body:
        article = Article.query.filter().all()
    else:
        article = Article.query.filter(Article.content.like('%' + body + '%')).all()

    for a in article:
        article_like1 = Article_like.query.filter(
            and_(Article_like.user_id == user_id, Article_like.article_id == a.article_Id)).first();
        if article_like1:
            a.likes = article_like1.likes
        else:
            a.likes = 0

    for a in article:
        article_like2 = Article_like.query.filter(Article_like.article_id == a.article_Id).all();
        a.like_count = sum([b.likes for b in article_like2])

    if not article:
        return resp

    resp['data'] = query_to_dict(article)
    return jsonify(resp)


@route_article.route("/add", methods=["GET", "POST"])
def add():
    resp = {"errMsg": "新增成功", "data": ""}
    req = request.get_json()
    title = req['title'] if 'title' in req else ''
    content = req['content'] if 'content' in req else ''
    author = req['author'] if 'author' in req else ''

    tag = req['tag'] if 'tag' in req else ''

    article = Article()

    article.title = title
    article.content = content
    article.author = author
    article.tag = ' '.join(tag)
    article.likes = 0

    article.create_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.session.add(article)

    # 提交
    db.session.commit()
    return resp


@route_article.route("/edit", methods=["GET", "POST"])
def edit():
    resp = {"errMsg": "修改成功", "data": ""}
    req = request.get_json()
    title = req['title'] if 'title' in req else ''
    content = req['content'] if 'content' in req else ''
    author = req['author'] if 'author' in req else ''
    id = req['article_Id'] if 'article_Id' in req else ''

    article = Article()

    article.title = title
    article.content = content
    article.author = author
    article.article_Id = id

    a = query_to_dict(article)
    Article.query.filter(Article.article_Id == id).update(query_to_dict(article))

    # 提交
    db.session.commit()
    return resp


@route_article.route("/dellete", methods=["GET", "POST"])
def dellete():
    resp = {"errMsg": "删除成功", "data": ""}
    req = request.get_json()
    for article in req:
        res = Article.query.filter(Article.article_Id == article["article_Id"]).delete()
    db.session.commit()
    return resp


@route_article.route("/like", methods=["GET", "POST"])
def like():
    resp = {"errMsg": "修改like成功", "data": ""}
    req = request.get_json()
    user_id = req['user_id'] if 'user_id' in req else ''
    article_id = req['article_Id'] if 'article_Id' in req else ''
    likes = req['likes'] if 'likes' in req else ''

    article_like0 = Article_like.query.filter(
        and_(Article_like.user_id == user_id, Article_like.article_id == article_id)).first()
    article_like = Article_like()
    article_like.user_id = user_id
    article_like.article_id = article_id
    article_like.likes = likes
    if not article_like0:
        db.session.add(article_like)
    else:
        article_like.id = article_like0.id
        Article_like.query.filter(Article_like.id == article_like0.id).update(
            query_to_dict(article_like))
    db.session.commit()
    return resp
