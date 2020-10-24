# -*- coding: utf-8 -*- 
# @Time : 2020/10/21 6:16 下午 
# @Author : hans.li
# @File : closure.py

from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return self.template.format_map(kwargs)


if __name__ == "__main__":
    # http://finance.yahoo.com/d/quotes.csv?s='IBM,AAPL,FB'&f='sl1c1v'
    yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
    for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
        print(line)
