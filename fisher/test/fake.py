# -*- coding: utf-8 -*- 
# @Time : 2020/9/30 3:43 下午 
# @Author : hans.li
# @File : fake.py

from app import create_app
from app.models.base import db
from app.models.user import User

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        with db.auto_commit():
            pass
            # 创建一个超级管理员
            # user = User()
            # user.nickname = 'super'
            # user.password = '123456'
            # user.email = 'super@t.com'
            # user.auth = 2
            # db.session.add(user)

            #db.create_all()
