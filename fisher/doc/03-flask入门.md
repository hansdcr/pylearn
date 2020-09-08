### flask入门

#### 1.  基础环境配置

##### 1.1  自动热加载功能的开启

* app.run(debug=True)

```python
from flask  import Flask

# 实例化flask对象
app = Flask(__name__)
# 注册路由
@app.route('/hello')
def hello():
    return "hello hans!"


if __name__ == '__main__':
    # 启动flask实例
    app.run(debug=True)



```



##### 1.2 自定义监听地址和端口

*  app.run(host='0.0.0.0', port=5000)

```python
from flask  import Flask

# 实例化flask对象
app = Flask(__name__)


# 注册路由
@app.route('/hello')
def hello():
    return "hello hans!"


if __name__ == '__main__':
    # 启动flask实例
    app.run(host='0.0.0.0', port=5000)



```



##### 1.3 配置文件的加载

* app.config.from_object('config')
* app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])

```python
from flask  import Flask

# 实例化flask对象
app = Flask(__name__)
app.config.from_object('config')


# 注册路由
@app.route('/hello')
def hello():
    return "hello hans!"


if __name__ == '__main__':
    # 启动flask实例
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])

```

#### 2. 自定义返回json类型数据

```python
class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
```

#### 3. 蓝图

##### 3.1  什么是蓝图

* 蓝图的层级关系

```
                    app
                     |
             蓝图                  蓝图
      |        |     |
    视图     视图    视图         
```



##### 3.2 使用蓝图组织文件目录结构

```python
            app
             | --- web # 蓝图
             |       |  --- book.py  #视图
             |       |  --- user.py. #视图
             |       |  --- __init__.py    #用于组织蓝图
             | --- __init__.py #用于组织app
             |
             | --- fisher.py  # 入口文件
```

* fisher.py

```python
from app import create_app


app = create_app()  # 导入flask的app实例

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
```

* app/_init_.py

```python
from flask import Flask

# 创建flask实例
def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app
  
# 蓝图插入app对象
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
```

* web/__init__.py

  Blueprint('web', \__name\__)  web是蓝图的名称，\_name\_是蓝图所在当前模块名称

```python
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book  #将需要注册的视图模块都在这里导入
```

* book.py

```python
from flask import jsonify, Blueprint
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web


@web.route('/book/search/<q>/<page>')  # 使用蓝图关联路由
def search(q, page):
    """
    :param q:  代表普通查询关键字 或者  isbn
    :param page: 分页
    :return:
    """

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
```

##### 3.3 蓝图的注册步骤

* 步骤一： 路由关联视图

```python
@web.route('/book/search/<q>/<page>') 
def search():
	pass
```

* 步骤二： 视图插入蓝图

```python
from flask import Blueprint
web = Blueprint('web', __name__)
```

* 步骤三： 蓝图插入app

```python
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
```

##### 3.4 1



#### 100 问题

##### 1.1 return 'hello' 和 Response的区别

* Response做了封装，比如status, headers

##### 1.2  有哪些方法可以简化if else代码











