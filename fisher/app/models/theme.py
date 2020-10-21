# -*- coding: utf-8 -*- 
# @Time : 2020/10/19 3:33 下午 
# @Author : hans.li
# @File : theme.py

from sqlalchemy import Column, Integer, String, Boolean

from app.models.base import Base


class Theme(Base):
    id = Column(Integer,primary_key=True, autoincrement=True)
    title = Column(String(120))
    description = Column(String)
    name = Column(String)
    extend = Column(String)
    entranceImg = Column(String)
    internalTopImg = Column(String)
    online = Column(Boolean)
    titleImg = Column(String)
    tplName = Column(String)
