# -*- coding: utf-8 -*- 
# @Time : 2020/9/28 3:12 下午 
# @Author : hans.li
# @File : token.py

import json
from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.api import api
from app.validators.forms import ClientForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User


@api.route('/v1/token', methods=['POST'])
def get_token():
    # 接收用户数据并且对数据进行验证
    form = ClientForm().validate_for_api()
    # 去数据库查询并且验证用户
    identity = User.verify(form.account.data, form.secret.data)
    # 过期时间
    expiration = current_app.config['TOKEN_EXPIRATION']
    # 权限范围
    scope = identity['scope']
    # 生成令牌
    token = generate_auth_token(identity['uid'], form.type.data, scope, expiration=expiration)

    return jsonify({'token': token.decode('ascii')}), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'uid': uid, 'type': ac_type.value, 'scope': scope})
