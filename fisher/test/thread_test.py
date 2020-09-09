# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 9:26 下午 
# @Author : hans.li
# @File : thread_test.py

import threading
import time


def worker():
    time.sleep(10)
    print('i am worker thread')
    t = threading.current_thread()
    print(t.getName())

# 测试新创建一个线程
new_t = threading.Thread(target=worker, name='worker_thread')
new_t.start()

# 测试打印主线程名字
t = threading.current_thread()
print(t.getName())

