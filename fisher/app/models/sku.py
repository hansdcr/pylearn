# -*- coding: utf-8 -*- 
# @Time : 2020/10/19 3:49 下午 
# @Author : hans.li
# @File : Sku.py

from sqlalchemy import Column, Integer, String, Boolean, Float

from app.models.base import Base


class Sku(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float)
    discountPrice = Column(Float)
    online = Column(Boolean)
    img = Column(String(256))
    title = Column(String(256))
    spuId = Column(Integer)
    categoryId = Column(Integer)
    rootCategoryId = Column(Integer)
    specs = Column(String(256))
    code = Column(String(256))
    stock = Column(Integer)
