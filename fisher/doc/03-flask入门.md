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

##### 4.3 自定义校验

* 自定义校验使用“validate__字段名”作为函数名

```python
class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空，请输入你的密码'), Length(6, 32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少两个字符，最多10个字符')])

		# 自定义校验, 自定义email字段的校验，校验邮件是否已经注册
    def validate_email(self, field):
        """ 自定义验证器 """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')
            
		# 自定义校验，校验昵称是否已经存在
    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')
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

* python只能对字典类型进行序列化，那么该如何对对象进行序列化？

```python
json.dumps(books, default=lambda o: o.__dict__)
```

完整代码

```python
@web.route('/book/search')
def search():
    """
    :param q:  代表普通查询关键字 或者  isbn
    :param page: 分页
    :return:
    """

    # 参数校验
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__) #序列化
    else:
        return jsonify(form.errors)
```



##### 5.4 数据查询

##### 5.5 数据修改

##### 5.6 数据保存

##### 5.7 数据删除

##### 5.8 一对多

##### 5.9 多对多

##### 5.10 数据库的事务管理

###### 5.10.1  理解上下文管理协议

* 什么是上下文管理协议？
  * 实现了\__enter\__ 和 \__exit\_ 就实现了上下文管理协议_
* 上下文管理协议的用途是什么？
  * 帮助我们处理类似资源需要打开和关闭回收这样功能的处理，比如对文件资源或数据库资源的操作
* 实际例子如下

```python
class MyResourse:
    def __enter__(self):
        print('Connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('close resource connection')

    def query(self):
        print('query data')


# 上面实现了上下文协议，所以可以使用with
with MyResourse() as r:
    r.query()
```

输出如下:

```python
Connect to resource
query data
close resource connection
```

###### 5.10.2  使用@contextmanager实现上下文管理协议

* 为什么要使用@contextmanager实现上下文管理器
  * 对于第三方编写的模块，我们想要它具备上下文管理协议的功能的需求时
  * 可以简化上下文管理器的实现
* 如果想实现5.10.1的功能该如何改写？

```python
class MyResourse:
    def query(self):
        print('query data')
```

```python
from contextlib import contextmanager

@contextmanager
def make_myresource():
    print('Connect to resource')
    yield MyResourse()
    print('close resource')
```

```python
with make_myresource() as r:
    r.query()
```

```python
# 这里使用yield代替return
# 因为yield和return区别在于，yield执行到MyResourse()会中断，等MyResourse()执行完后，会再次回到make_myresource继续执行后面的代码
```

输出:

```
Connect to resource
query data
close resource connection
```

###### 5.10.3  在实际项目中的应用

```python
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer


class SQLAlchemy(_SQLAlchemy):
    @contextmanager		# 实现上下文管理协议
    def auto_commit(self):
        try:
            yield
            self.session.commit() # 提交事务
        except Exception as e:
            db.session.rollback()  # 失败回滚
            raise e


db = SQLAlchemy()


class Base(db.Model):
	pass
```

视图函数中的使用

```python
@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    """ 赠送图书 """
    if current_user.can_save_to_list(isbn):
        with db.auto_commit(): # 使用上下文管理协议改写，实现自动提交和回滚功能
            gift = Gift()
            gift.isbn = isbn
            # current_user实际代表的是User模型，是通过@login_manager.user_loader它获得的
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
```

未使用auto_commit()改造之前的写法

```python
@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    """ 赠送图书 """
    if current_user.can_save_to_list(isbn):
        try:
            gift = Gift()
            gift.isbn = isbn
            # current_user实际代表的是User模型，是通过@login_manager.user_loader它获得的
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    else:
        print('这本书已经添加至你的赠送清单或已经存在于你的心愿清单，请不要重复添加')
```

##### 5.11 重新filter_by的方法

* 为什么要重写filter_by?
  * 我们想查询的时候自动携带status=1这个软删除的字段
* 如何实现自定义的filter_by?
  * flask中提供了重写的入口，在SQLAlchemy(query_class=Query)这里

```python
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery

class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)
        
   
 db = SQLAlchemy(query_class=Query)
```



#### 6.  注册登录

##### 6.1 登陆验证

###### 6.1.2  登陆流程

* 客户端发送用户名密码等验证信息给服务器
* 服务器对用户名密码进行校验
* 服务器校验通过颁发票据给客户端
* 客户端保存票据到cookie中
* 客户端每次获取资源需要携带票据



*  使用flask-login插件进行登陆和cookie设置

步骤一：

```python
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    # 插入sqlalchemy
    db.init_app(app)
    # db.create_all(app=app)
    with app.app_context():
        db.create_all()

    # 注册login登陆管理插件
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    return app
```

步骤二： 继承UserMixin

UserMixin实现了相关的方法

```python
from flask_login import UserMixin
from app.models.base import Base


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
```

步骤三:  在视图中使用login_user

```python
@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)  # 向cookie中写入票据
            next = request.args.get('next') # 获取问号后面的内容
            if not next or next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            print("账号不存在或密码错误")
    return 'login'
```

###### 6.1.3 权限验证

步骤一： 启动加载flask-login插件

```python
from flask import Flask
from app.models.base import db
from app.models import *  # 注意这里导入了User模型
from flask_login.login_manager import LoginManager  # 导入LoginManager


login_manager = LoginManager()  # 创建LoginManager对象

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    # 插入sqlalchemy
    db.init_app(app)
    # db.create_all(app=app)
    with app.app_context():
        db.create_all()

    # 注册login登陆管理插件
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    return app
  
# 使用user_loader加载User对象  
@login_manager.user_loader
def get_user(uid):
    return User.query.get(uid)
```

步骤二： 视图中使用验证装饰器@login_required

```python
@web.route('/my/gifts')
@login_required
def my_gifs():
    return 'my gifts'
```









#### 100 问题

##### 1.1 return 'hello' 和 Response的区别

* Response做了封装，比如status, headers

##### 1.2  有哪些方法可以简化if else代码



#### 101 遇到的问题

##### 101.1  sqlalchemy不能自动创建表的问题

* 现象：
  * 不能根据模型创建表，也不报任何错误
* 原因
  *  没有导入模型
* 解决方法
  * 如下图

```python
from flask import Flask
from app.models.base import db
from app.models import *   # 这里要把模型导入进来
from flask_login.login_manager import LoginManager


login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    # 插入sqlalchemy
    db.init_app(app)
    #db.create_all(app=app)
    with app.app_context():
        db.create_all()

    # 注册login登陆管理插件
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    return app
```















