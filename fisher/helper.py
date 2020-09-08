# -*- coding: utf-8 -*- 
# @Time : 2020/9/7 8:11 下午 
# @Author : hans.li 
# @File : helper


def is_isbn_or_key(word):
    """
    判断查询的内容是普通的关键词还是isbn编号
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'

    return isbn_or_key
