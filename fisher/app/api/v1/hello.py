# -*- coding: utf-8 -*- 
# @Time : 2020/9/28 10:45 上午 
# @Author : hans.li
# @File : hello.py
import json
from flask import g
from app.api import api
from app.libs.token_auth import auth
from app.libs.error_code import Forbidden


@api.route('/api/v1/hello')
#@auth.login_required
def hello():
    return json.dumps({'hello': 'world'})
