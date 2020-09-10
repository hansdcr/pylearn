# -*- coding: utf-8 -*- 
# @Time : 2020/9/10 2:46 下午 
# @Author : hans.li
# @File : wish.py
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from app.models.base import Base


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
