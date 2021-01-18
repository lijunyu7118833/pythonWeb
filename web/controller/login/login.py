from flask import Blueprint, request, jsonify, json
from operator import and_, __or__, or_
from common.models.user import User
from common.libs.queryToDict import *

route_user = Blueprint('user', __name__)


@route_user.route("/doLogin", methods=["GET", "POST"])
def login():
    resp = {"errMsg": "登陆成功", "data": ""}
    req = request.get_json()
    # 用户名
    user_name = req['name'] if 'name' in req else ''
    password = req['password'] if 'password' in req else ''
    user = User.query.filter(and_(User.user_name == user_name, User.password == password)).first()
    if user is None:
        resp['errMsg'] = "用户名密码错误，请重新登录！"
        return jsonify(resp)
    resp['data'] = query_to_dict(user)
    return jsonify(resp)
