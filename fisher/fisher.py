# -*- coding: utf-8 -*- 
# @Time : 2020/9/7 5:51 下午 
# @Author : hans.li 
# @File : fisher.py

from app import create_app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
8uu
