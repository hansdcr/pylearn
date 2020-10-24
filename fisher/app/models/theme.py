# -*- coding: utf-8 -*- 
# @Time : 2020/10/19 3:33 下午 
# @Author : hans.li
# @File : theme.py

from sqlalchemy import Column, Integer, String, Boolean

from app.models.base import Base


class Theme(Base):
    id = Column(Integer,primary_key=True, autoincrement=True)
    title = Column(String(120))
    description = Column(String(256))
    name = Column(String(256))
    extend = Column(String(256))
    entranceImg = Column(String(256))
    internalTopImg = Column(String(256))
    online = Column(Boolean)
    titleImg = Column(String(256))
    tplName = Column(String(256))
