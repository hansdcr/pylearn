# -*- coding: utf-8 -*- 
# @Time : 2020/10/16 11:27 上午 
# @Author : hans.li
# @File : bannerItem.py

from sqlalchemy import Column, Integer, String

from app.models.base import Base


class BannerItem(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    img = Column(String(60), comment="图片地址")
    keyword = Column(String(60))
    type = Column(Integer)
    banner_id = Column(Integer)
    name = Column(String(60))
