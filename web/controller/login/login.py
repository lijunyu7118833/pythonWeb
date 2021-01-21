from flask import Blueprint, request, jsonify, current_app, json
from operator import and_, __or__, or_

from common.models.user import User
from common.libs.queryToDict import *
from application import db

route_user = Blueprint('user', __name__)


@route_user.route("/doLogin", methods=["GET", "POST"])
def login():
    resp = {"errMsg": "登陆成功", "data": "", "token": ""}
    req = request.get_json()
    # 用户名
    user_name = req['name'] if 'name' in req else ''
    password = req['password'] if 'password' in req else ''
    user = User.query.filter(User.user_name == user_name).first()
    if not user.verify_password(password):
        resp['errMsg'] = "用户名密码错误，请重新登录！"
        return jsonify(resp)
    resp['token'] = user.generate_auth_token()
    resp['data'] = query_to_dict(user)
    return jsonify(resp)


@route_user.route("/doRegister", methods=["GET", "POST"])
def doRegister():
    resp = {"errMsg": "注册成功", "data": ""}
    req = request.get_json()
    user_name = req['name'] if 'name' in req else ''
    password = req['password'] if 'password' in req else ''
    user1 = User.query.filter(User.user_name == user_name).first()
    if user1:
        resp['errMsg'] = "用户名已被注册,请更换用户名"
        return jsonify(resp)

    user = User()
    user.user_name = user_name
    user.hash_password(password)

    db.session.add(user)

    # 提交
    db.session.commit()
    return jsonify(resp)


@route_user.route("/find", methods=["GET", "POST"])
def find():
    resp = {"errMsg": "查询成功", "data": "", "token": ""}
    user = User.query.filter().all()
    if not user:
        return resp
    resp['data'] = query_to_dict(user)
    return jsonify(resp)
