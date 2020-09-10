# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 4:19 下午 
# @Author : hans.li
# @File : gift.py
from flask import current_app
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, SmallInteger, desc
from sqlalchemy.orm import relationship
from app.models.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)

    @classmethod
    def recent(cls):
        # 链式调用
        # 主体 Query
        # 子函数
        # first() all()
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift