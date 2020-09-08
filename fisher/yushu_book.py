# -*- coding: utf-8 -*- 
# @Time : 2020/9/7 9:42 下午 
# @Author : hans.li
# @File : yushu_book.py

from httper import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=10, start=0):
        url = YuShuBook.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result