### web爬虫

#### 1. scrapy安装

```
pipenv install --python 3.7.0
pipenv shell
pipenv install scrapy
```

#### 2. 安装mongodb

```
 brew tap mongodb/brew
 brew install mongodb-community@4.2
 
 #/usr/local/etc/mongod.conf
 #/usr/local/var/log/mongodb
 #/usr/local/var/mongodb
 
 echo 'export PATH="/usr/local/opt/mongodb-community@4.2/bin:$PATH"' >> /Users/vivo/.bash_profile
 启动：
 brew services start mongodb/brew/mongodb-community@4.2
 或者
 mongod --config /usr/local/etc/mongod.conf
 
 
 
 #brew services start mongodb-community
 #brew services stop mongodb-community
 
 #ps aux | grep -v grep | grep mongod
 
 
 
```

#### 3. 项目创建

##### 3.1 新建scrapy项目

```
scrapy startproject douban
```

生成spider文件

```
scrapy genspider douban_spider movie.douban.com
```

#### 4. 确定抓取内容

##### 4.1  Items文件（定义抓取内容）

```
class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 序号
    serial_number = scrapy.Field()
    # 电影名
    movie_name = scrapy.Field()
    # 介绍
    introduce = scrapy.Field()
    # 星级
    star = scrapy.Field()
    # 评论
    evaluate = scrapy.Field()
    # 描述
    describe = scrapy.Field()
```

 ##### 4.2 

#### 5. selenium

##### 5.1 安装selenium

```
 pipenv install selenium --skip-lock
```



