# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 10:09 上午 
# @Author : hans.li
# @File : book.py

from flask import jsonify, request, render_template
from flask_login import current_user

from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from .. import Gift, Wish
from ..view_models.book import BookViewModel, BookCollection
import json

from ..view_models.trade import TradeInfo


@web.route('/book/search')
def search():
    """
    :param q:  代表普通查询关键字 或者  isbn
    :param page: 分页
    :return:
    """

    # 参数校验
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html', book=book,
                           wishes=trade_wishes_model,
                           gifs=trade_gifts_model,
                           has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes)

