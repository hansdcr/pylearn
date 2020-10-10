# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 10:58 上午 
# @Author : hans.li
# @File : __init__.py
import time
import json
from flask import Flask, g, request
from app.models.base import db
from app.models import *
from app.core.logger import Mylog
from flask_login.login_manager import LoginManager


login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.log')

    register_blueprint(app)
    register_plugin(app)

    register_before_request(app)
    register_after_request(app)

    return app


def register_before_request(app):
    @app.before_request
    def request_cost_time():
        g.request_start_time = time.time()
        g.request_time = lambda: "%.5f" % (time.time() - g.request_start_time)


def register_after_request(app):
    @app.after_request
    def log_response(resp):
        log_config = app.config.get('LOG')
        if not log_config['REQUEST_LOG']:
            return resp
        message = '[%s] -> [%s] from:%s costs:%.3f ms' % (
            request.method,
            request.path,
            request.remote_addr,
            float(g.request_time()) * 1000
        )
        if log_config['LEVEL'] == 'INFO':
            app.logger.info(message)
        elif log_config['LEVEL'] == 'DEBUG':
            req_body = '{}'
            try:
                req_body = request.get_json() if request.get_json() else {}
            except:
                pass
            message += " data:{\n\tparam: %s, \n\tbody: %s\n} " % (
                json.dumps(request.args, ensure_ascii=False),
                req_body
            )
            app.logger.debug(message)
        return resp


def register_plugin(app):
    # 插入sqlalchemy
    db.init_app(app)
    #db.create_all(app=app)
    with app.app_context():
        db.create_all()

    # 注册login登陆管理插件
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    # 注册日志
    Mylog(app)

    return app


def register_blueprint(app):
    from app.web.book import web
    from app.api import api

    app.register_blueprint(web)
    app.register_blueprint(api)


@login_manager.user_loader
def get_user(uid):
    return User.query.get(uid)
