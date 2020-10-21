# -*- coding: utf-8 -*- 
# @Time : 2020/10/19 4:32 下午 
# @Author : hans.li
# @File : Spu.py

from sqlalchemy import Column, Integer, String, Boolean, Float

from app.models.base import Base


class Spu(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    subtitle = Column(String)
    categoryId = Column(Integer)
    rootCategoryId = Column(Integer)
    online = Column(Boolean)
    price = Column(String)
    sketchSpecId = Column(Integer)
    defaultSkuId = Column(Integer)
    img = Column(String)
    discountPrice = Column(String)
    description = Column(String)
    tags = Column(String)
    isTest = Column(Boolean)
    forThemeImg = Column(String)
