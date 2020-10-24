# -*- coding: utf-8 -*- 
# @Time : 2020/9/28 4:05 下午 
# @Author : hans.li
# @File : error_code.py

from app.libs.error import APIException


class NotFound(APIException):
    code = 404
    msg = 'not found'
    error_code = 10001


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'


class Forbidden(APIException):
    code = 403
    error_code = 1006
    msg = 'forbidden, not in scope'


class Success(APIException):
    code = 201
    msg = '成功'
    error_code = 0
