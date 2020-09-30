# -*- coding: utf-8 -*- 
# @Time : 2020/9/28 3:47 下午 
# @Author : hans.li
# @File : forms.py

from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length
from app.validators.base import BaseForm
from app.libs.enums import ClientTypeEnum


class ClientForm(BaseForm):
    account = StringField(validators=[DataRequired('不允许为空'), length(min=5, max=32)])
    secret = StringField()
    # 客户端类型
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client

