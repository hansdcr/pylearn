# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 10:09 上午 
# @Author : hans.li
# @File : book.py

from flask import jsonify
from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q:  代表普通查询关键字 或者  isbn
    :param page: 分页
    :return:
    """

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)