# -*- coding: utf-8 -*- 
# @Time : 2020/10/23 11:15 上午 
# @Author : hans.li
# @File : banner.py

from flask import jsonify
from app.api import api
from app.models.banner import Banner
from app.libs.error_code import NotFound, Success


@api.route("/api/v1/banner/name/<names>")
def banner(names):
    banner = Banner.query.filter_by(name=names).first()
    if banner:
        return Success(data=banner)
    return NotFound()
