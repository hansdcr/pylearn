# -*- coding: utf-8 -*- 
# @Time : 2020/9/28 3:56 下午 
# @Author : hans.li
# @File : error.py

from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = 'sorry,we make a mistake'
    error_code = 999
    data = []

    def __init__(self, msg=None, code=None, error_code=None, data=None, header=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code
        if data:
            self.data.append(data)

        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code = self.error_code,
            request = request.method + ' ' + self.get_url_no_param(),
            data = self.data
        )

        return json.dumps(body)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]