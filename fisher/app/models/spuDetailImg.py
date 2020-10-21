# -*- coding: utf-8 -*- 
# @Time : 2020/10/19 5:10 下午 
# @Author : hans.li
# @File : SpuDetailImg.py


from sqlalchemy import Column, Integer, String, Boolean, Float

from app.models.base import Base


class SpuDetailImg(Base):
    id = Column(Integer)
    img = Column(String)
    spuId = Column(Integer)
    index = Column(Integer)
