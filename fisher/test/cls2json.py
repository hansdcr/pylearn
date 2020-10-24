# -*- coding: utf-8 -*- 
# @Time : 2020/10/23 4:35 下午 
# @Author : hans.li
# @File : cls2json.py



class Student(object):
    def __init__(self, name, age, sno, address=None):
        self._fields = []
        self.name = name
        self.age = age
        self.sno = sno
        self.address = address

    def __repr__(self):
        return 'Student [name: %s, age: %d, sno: %d]' % (self.name, self.age, self.sno)

    def __getitem__(self, key):
        return self.__dict__.get(self, key)

    def keys(self):
        return ['name', 'age', 'sno', 'address']


class Adress:
    def __init__(self, address, code):
        self._fields = []
        self.address = address
        self.code = code

    def __getitem__(self, key):
        return self.__dict__.get(self, key)

    def keys(self):
        return ['name', 'age', 'sno']



import json


# class MyJSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         d = {}
#         d['__class__'] = o.__class__.__name__
#         d['__module__'] = o.__module__
#         d.update(o.__dict__)
#         return d

class MyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return o
        return MyJSONEncoder.default(self, o)


if __name__ == "__main__":
    a1 = Adress('nanjing', 100)
    s1 = Student('s1', 20, 100, address=a1)

    print(json.dumps(a1))