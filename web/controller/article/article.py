from flask import Blueprint, request, jsonify, json
from operator import and_, __or__, or_
from common.models.user import User
from common.libs.queryToDict import *
from common.models.article import Article
from application import db

route_article = Blueprint('article', __name__)


@route_article.route("/find", methods=["GET", "POST"])
def find():
    resp = {"errMsg": "查询成功", "data": ""}

    article = Article.query.filter().all()
    if not article:
        return resp
    resp['data'] = query_to_dict(article)
    return resp


@route_article.route("/add", methods=["GET", "POST"])
def add():
    resp = {"errMsg": "新增成功", "data": ""}
    req = request.get_json()
    title = req['title'] if 'title' in req else ''
    content = req['content'] if 'content' in req else ''
    author = req['author'] if 'author' in req else ''
    article = Article()

    article.title = title
    article.content = content
    article.author = author

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
