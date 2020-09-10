# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 4:19 下午 
# @Author : hans.li
# @File : base.py


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)
    create_time = Column('create_time', Integer)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != id:  # 某个对象是否包含key的属性
                setattr(self, key, value)  # 对某个对象的key进行赋值value

