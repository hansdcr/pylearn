# -*- coding: utf-8 -*- 
# @Time : 2020/9/7 7:16 下午 
# @Author : hans.li 
# @File : config


DEBUG = True

SQLALCHEMY_DATABASE_URI = "mysql+cymysql://fisher:123456@localhost:3306/fisher"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

SECRET_KEY = 'aabbcc'
