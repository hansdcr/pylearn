

### MySQL语法基础

#### 1.  数据库

##### 1.1  创建数据库

```mysql
Create database db_douban Default Character set utf8;
Create database db_12306 Default Character set utf8;
Create database db_taobao Default Character set utf8;
```

##### 1.2  显示所有数据库

```
show DATABASES;
```

##### 1.3  切换数据库

```
USE db_taobao;
```

##### 1.4  删除数据库

```
DROP DATABASE db_taobao;
```

#### 2. 表

##### 2.1 创建表

```
CREATE TABLE `db_douban`.`douban_tv`(
	id bigint(20) not null auto_increment comment '电视剧id',
	tv_name varchar(256) not null default '' comment '电视剧名',
	tv_director varchar(256) not null default '' comment '导演名',
	primary key (`id`)
) engine=INNODB Default Charset=utf8mb4;
```

##### 2.2 常用引擎

* InnoDB
  * 支持事务和强一致性
  * 主要用于银行、金融等领域
* MyIASM
  * 不支持事务和强一致性
  * 主要用在大数据、数据仓库领域

##### 2.3 主键

* 作用
  * 主键不能重复
* 自增主键

##### 2.4  数据类型

* int 32位整型
* bigint 64位整型
* date 日期类型
* timestamp  时间戳类型
* varchar  文本类型
* decimal  金额类型 
* double   浮点型

##### 2.5  添加列

​	*	新增一列hot

```mysql
ALTER TABLE db_douban.douban_tv ADD COLUMN hot int not null DEFAULT 100 AFTER tv_name;
```

##### 2.6 删除列

* 删除一列hot

```mysql
ALTER TABLE db_douban.douban_tv DROP COLUMN hot;
```

##### 2.7 修改列

```mysql
ALTER TABLE db_douban.douban_tv CHANGE COLUMN tv_name tv_name VARCHAR(200) NOT NULL DEFAULT '' COMMENT '电视剧名';
```

##### 2.8 删除表

```
DROP TABLE db_douban.douban_tv;
```

#### 3.  插入

```mysql
INSERT INTO db_douban.douban_tv (id ,tv_name, tv_director) VALUES (30438115, '自修室', '未知');
INSERT INTO db_douban.douban_tv (id ,tv_name, tv_director) VALUES (25750923, '神探夏洛克', '瑞秋.塔拉雷');
INSERT INTO db_douban.douban_tv (id ,tv_name, tv_director) VALUES (1301174, '傲慢与偏见', '西蒙.兰顿');
```

#### 4. 更新

##### 4.1 全表修改

```mysql
SET SQL_SAFE_UPDATES = 0; -- 关闭安全模式
UPDATE db_douban.douban_tv SET tv_director = '未知';
```

##### 4.2 过滤修改

```mysql
UPDATE db_douban.douban_tv SET tv_director = '未知-1' WHERE id=30438115;
```

#### 5. 删除

##### 5.1 过滤删除

```mysql
DELETE FROM db_douban.douban_tv WHERE id=30438115; 
```

##### 5.2 永久删除

```mysql
trancate TABLE db_douban.douban_tv;
```

##### 5.3 全表删除

```mysql
DELETE FROM db_douban.douban_tv;
```

#### 6. 查询

##### 6.1 单列查询

```mysql
SELECT tv_director FROM db_douban.douban_tv;
```

##### 6.2 多列查询

```mysql
SELECT tv_name, tv_director FROM db_douban.douban_tv;
```

```mysql
SELECT id, tv_name, tv_director FROM db_douban.douban_tv;
```

##### 6.3 虚拟列查询

* 虚拟列的作用
  * 可以自己定制表的列，比如新增一个原来的表没有的列
  * 对列进行计算等

* 1 是虚拟列
* 1 as number, number是列的别名
* t 是表doubt_tv的别名

```mysql
SELECT 1 as `number`, t.* FROM db_douban.douban_tv t;
```

```mysql
SELECT 1 as `number`, t.*, tv_name as tv_name_new FROM db_douban.douban_tv t;

输出：
number	id			tv_name		 tv_director		tv_name_new
1			1301174		傲慢与偏见		西蒙.兰顿				傲慢与偏见
1			25750923	神探夏洛克		瑞秋.塔拉雷		  神探夏洛克
1			30438115	自修室			  未知					 自修室
```

```mysql
-- 对列进行计算
SELECT t.id, t.id + 100 as new_id FROM db_douban.douban_tv t;
```

##### 6.4 条件查询

###### 6.4.1  算数运算

```mysql
-- SELECT * FROM db_douban.douban_tv WHERE id=1301174;
-- SELECT * FROM db_douban.douban_tv WHERE id!=1301174;
-- SELECT * FROM db_douban.douban_tv WHERE id > 1301174;
-- SELECT * FROM db_douban.douban_tv WHERE id < 1301174;
-- SELECT * FROM db_douban.douban_tv WHERE id >= 1301174;
-- SELECT * FROM db_douban.douban_tv WHERE id <= 1301174;
```

###### 6.4.2  条件枚举查询

* 关键字 in

```mysql
SELECT * FROM db_douban.douban_tv WHERE tv_name in ('傲慢与偏见', '神探夏洛克');
```

* 关键字 not in

```mysql
SELECT * FROM db_douban.douban_tv WHERE tv_name not in ('傲慢与偏见', '神探夏洛克');
```

###### 6.4.3 条件且查询

* 关键字 and
* 需求： 查找的电影在指定的清单（'傲慢与偏见', '神探夏洛克'）中，且是“西蒙.兰顿”导演的电影

```mysql
SELECT * FROM db_douban.douban_tv WHERE tv_name in ('傲慢与偏见', '神探夏洛克') and tv_director='西蒙.兰顿';
```

###### 6.4.4 条件或查询

* 

























































