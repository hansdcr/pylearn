# -*- coding: utf-8 -*- 
# @Time : 2020/9/10 3:37 下午 
# @Author : hans.li
# @File : yield_test.py


# class MyResourse:
#     def __enter__(self):
#         print('Connect to resource')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('close resource connection')
#
#     def query(self):
#         print('query data')
#
#
# # 上面实现了上下文协议，所以可以使用with
# with MyResourse() as r:
#     r.query()

# 现在需求不使用上下文协议实现如下功能
# 1。 按照顺序执行下面语句
#    print('Connect to resource')
#    return self
#    print('query data')

from contextlib import contextmanager


class MyResourse:
    def query(self):
        print('query data')


@contextmanager
def make_myresource():
    print('Connect to resource')
    yield MyResourse()
    print('close resource')


with make_myresource() as r:
    r.query()

# 这里使用yield代替return
# 因为yield和return区别在于，yield执行到MyResourse()会中断，等MyResourse()执行完后，会再次回到make_myresource继续执行后面的代码

# 意义在于对第三方模块添加上下文协议

