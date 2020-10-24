# -*- coding: utf-8 -*- 
# @Time : 2020/10/15 3:10 下午 
# @Author : hans.li
# @File : banner.py

from sqlalchemy import Column, Integer, String

from app.models.base import Base, db


class Banner(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), comment="Banner名称")
    description = Column(String(120), comment="Banner的描述信息")
    title = Column(String(60), comment="Banner标题")
    img = Column(String(50), comment="Banner图片地址")
    bannerItems = db.relationship('BannerItem', backref='Banner', lazy=True)

    def keys(self):
        return ['id', 'name', 'description', 'title', 'img', 'bannerItems']