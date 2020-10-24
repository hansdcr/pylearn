# -*- coding: utf-8 -*- 
# @Time : 2020/10/19 4:32 下午 
# @Author : hans.li
# @File : Spu.py

from sqlalchemy import Column, Integer, String, Boolean, Float

from app.models.base import Base


class Spu(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(256))
    subtitle = Column(String(256))
    categoryId = Column(Integer)
    rootCategoryId = Column(Integer)
    online = Column(Boolean)
    price = Column(String(256))
    sketchSpecId = Column(Integer)
    defaultSkuId = Column(Integer)
    img = Column(String(256))
    discountPrice = Column(String(256))
    description = Column(String(256))
    tags = Column(String(256))
    isTest = Column(Boolean)
    forThemeImg = Column(String(256))
