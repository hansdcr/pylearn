# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 4:19 下午 
# @Author : hans.li
# @File : gift.py
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship
from app.models.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)