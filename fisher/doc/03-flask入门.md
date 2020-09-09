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
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
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

#### 4.  客户端请求数据的处理

##### 4.1  url中问号参数的处理

* 使用flask自带的request处理
* 这个request的使用范围是在flask当中且是在视图中才有效

```python
from flask import request
@web.route('/book/search')
def search():
    """
    :param q:  代表普通查询关键字 或者  isbn
    :param page: 分页
    :return:
    """

    q = request.args['q']  #获取问号参数
    page = request.args['page']

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
```

##### 4.2  参数校验

* 对客户端出入的请求参数进行校验

```python
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
```

* 在视图中引用校验

```python
@web.route('/book/search')
def search():
    # 参数校验
    form = SearchForm(request.args) # 实例化验证对象

    if form.validate(): # 对参数进行校验
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
```

#### 5. 数据库层

##### 5.1 数据库连接配置

* 步骤一： 配置数据库连接

```python
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
SQLALCHEMY_DATABASE_URI = "mysql+cymysql://fisher:123456@localhost:3306/fisher"
```

* 步骤二： 将sqlalchemy插件注册到app

```python
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    # 插入sqlalchemy
    db.init_app(app)
    db.create_all(app=app)

    return app
```

* 步骤三: 定义一个model

```python
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import  SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未知')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
```

##### 5.2 ViewModel

* ViewModel要解决什么问题？
  * 客户端对数据格式的需求千变万化，需要我们对数据作专门的定制
  * 裁剪数据
  * 修饰数据
  * 合并

##### 5.3 序列化







#### 100 问题

##### 1.1 return 'hello' 和 Response的区别

* Response做了封装，比如status, headers

##### 1.2  有哪些方法可以简化if else代码











