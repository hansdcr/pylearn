# -*- coding: utf-8 -*- 
# @Time : 2020/10/21 5:12 下午 
# @Author : hans.li
# @File : specs.py

from sqlalchemy import Column, Integer, String, Boolean, Float

from app.models.base import Base


class Spec(Base):
    """ 规格 """
    id = Column(Integer, primary_key=True, autoincrement=True)
    keyId = Column(Integer)
    key = Column(String)
    valueId = Column(Integer)
    value = Column(String)
