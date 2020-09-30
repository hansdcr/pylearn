# -*- coding: utf-8 -*- 
# @Time : 2020/9/30 4:56 下午 
# @Author : hans.li
# @File : scope.py


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []
    pass


class AdminScope(Scope):
    pass


class UserScope(Scope):
    allow_module = ['api.hello']
    pass


def is_in_scope(scope, endpoint):
    # 通过反射的方式获得scope对象
    scope = globals()[scope]()
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_module:
        return True
    if endpoint in scope.allow_api:
        return True
    else:
        return False
