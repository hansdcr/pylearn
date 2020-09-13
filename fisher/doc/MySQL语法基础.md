

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

* 关键字 or
*  任何一个条件满足都会输出

```mysql
SELECT * FROM db_douban.douban_tv WHERE tv_name in ('傲慢与偏见', '神探夏洛克') or tv_director='西蒙.兰顿';
```

```mysql
id	tv_name	tv_director
1301174	傲慢与偏见	西蒙.兰顿
21965460	战地神探	西蒙.兰顿
25750923	神探夏洛克	瑞秋.塔拉雷
```

###### 6.4.5 练习

* and  和 or 一起使用的时候，建议加括号来区分平级关系
* 比较下面两条语句的差异

```mysql
SELECT * FROM db_douban.douban_tv WHERE (tv_name in ('傲慢与偏见', '神探夏洛克') and id <0) or tv_director='西蒙.兰顿';
```

```mysql
SELECT * FROM db_douban.douban_tv WHERE tv_name in ('傲慢与偏见', '神探夏洛克') and (id <0 or tv_director='西蒙.兰顿');
```

#### 7. 内置函数

##### 7.1  数学函数

* 绝对值abs()

```mysql
SELECT abs(id), t.* FROM db_douban.douban_tv t;
```

* 取模mod()

```mysql
SELECT mod(id, 100), t.* FROM db_douban.douban_tv t;
```

##### 7.2 字符函数

* lower()

```mysql
SELECT LOWER('A'), LOWER(t.tv_name), t.* FROM db_douban.douban_tv t;
```

##### 7.3 日期时间函数

* now()
* Current_date()
* Current_time
* Current_timestamp()
* Date_add()

```mysql
SELECT NOW(), CURRENT_DATE(), CURRENT_TIME(), CURRENT_TIMESTAMP, DATE_ADD('2020-02-02', INTERVAL 1 YEAR),t.* FROM db_douban.douban_tv t;
```

```
NOW()	CURRENT_DATE()	CURRENT_TIME()	CURRENT_TIMESTAMP	DATE_ADD('2020-02-02', INTERVAL 1 YEAR)	id	tv_name	tv_director
2020-09-11 15:10:04	2020-09-11	15:10:04	2020-09-11 15:10:04	2021-02-02	1301174	傲慢与偏见	西蒙.兰顿
2020-09-11 15:10:04	2020-09-11	15:10:04	2020-09-11 15:10:04	2021-02-02	21965460	战地神探	西蒙.兰顿
2020-09-11 15:10:04	2020-09-11	15:10:04	2020-09-11 15:10:04	2021-02-02	25750923	神探夏洛克	瑞秋.塔拉雷
2020-09-11 15:10:04	2020-09-11	15:10:04	2020-09-11 15:10:04	2021-02-02	30438115	自修室	未知
```

*  时间比较
* DATEDIFF()
* TIMEDIFF()

```mysql
SELECT DATEDIFF('2020-02-02', '2020-02-03') AS t1 , TIMEDIFF('2020-02-02 23:23:58', '2020-02-02 23:23:59')  AS t2 FROM db_douban.douban_tv;
```

* 字符串转时间
* STR_TO_DATE()

```
SELECT STR_TO_DATE('2020-02-02', '%Y-%m-%d') FROM db_douban.douban_tv;
```

##### 7.4 聚合函数

* 用途
  * 常被用来做统计

* sum()
* Avg()
* Max()
* Min()

```mysql
SELECT COUNT(1), SUM(hot), AVG(hot), max(hot), min(hot)  FROM db_douban.douban_tv;
```

#### 8.  复杂查询

##### 8.1 分组查询

* 根据导演作为维度分组
* 一般分组和聚合函数一起使用
* 分组时使用where和having的区别
  * Where  是先过滤在分组
  * Having 是先分组在过滤

```
-- 原始数据
id	tv_name	hot	tv_director
1301174	傲慢与偏见	101	西蒙.兰顿
21965460	战地神探	100	西蒙.兰顿
25750923	神探夏洛克	102	瑞秋.塔拉雷
30438115	自修室	103	未知
```

```mysql
SELECT 
	t.tv_director, 
	COUNT(hot),
	SUM(hot),
	AVG(hot),
	MAX(hot),
	MIN(hot) 
FROM db_douban.douban_tv t
GROUP BY tv_director;
```

```
--输出结果：
tv_director	COUNT(hot)	SUM(hot)	AVG(hot)	MAX(hot)	MIN(hot)
西蒙.兰顿	2	201	100.5000	101	100
瑞秋.塔拉雷	1	102	102.0000	102	102
未知	1	103	103.0000	103	103
```

* 根据条件进行分组

```mysql
SELECT 
	t.tv_director, 
	COUNT(hot),
	SUM(hot),
	AVG(hot),
	MAX(hot),
	MIN(hot) 
FROM db_douban.douban_tv t
WHERE tv_director = '西蒙.兰顿'
GROUP BY tv_director;
```

* 或者使用having进行条件过滤

```mysql
SELECT 
	t.tv_director, 
	COUNT(hot),
	SUM(hot),
	AVG(hot),
	MAX(hot),
	MIN(hot) 
FROM db_douban.douban_tv t
GROUP BY tv_director
HAVING tv_director = '西蒙.兰顿';
```

##### 8.2 分页查询

* limit

```mysql
SELECT * FROM db_douban.douban_tv ORDER BY hot DESC LIMIT 0,2; -- 第一页 
SELECT * FROM db_douban.douban_tv ORDER BY hot DESC LIMIT 2,2; -- 第二页
```

#### 9.  多表查询

* 创建测试表

```mysql
CREATE TABLE `db_douban`.`douban_tv_detail` (
id BIGINT(20) NOT NULL auto_increment COMMENT '剧情主键',
tv_id  BIGINT(20) NOT NULL DEFAULT 0 COMMENT '电视剧id',
tv_note VARCHAR(256) NOT NULL DEFAULT '' COMMENT '剧情',
PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4;


INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (30438115, '第一集[自修室]');
INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (30438115, '第二集[自修室]');
INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (30438115, '第三集[自修室]');



INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (25750923, '第一集[神探夏洛克]');
INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (25750923, '第二集[神探夏洛克]');
INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (25750923, '第三集[神探夏洛克]');



INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (21965460, '第一集[战地神探]');
INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (21965460, '第二集[战地神探]');
INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (21965460, '第三集[战地神探]');



INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (1301174, '第一集[傲慢与偏见]');
INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (1301174, '第二集[傲慢与偏见]');
INSERT INTO `db_douban`.`douban_tv_detail` (tv_id, tv_note) VALUES (1301174, '第三集[傲慢与偏见]');
```

##### 9.1 内联查询

* 关键字 INNER JOIN
* INNER JOIN  后面加第二张表名
* ON  两个表进行关联的条件

```mysql
USE db_douban;
SELECT * 
FROM douban_tv t1
INNER JOIN douban_tv_detail t2
ON t1.id=t2.tv_id;
```

输出

```
id	tv_name	hot	tv_director	id(1)	tv_id	tv_note
30438115	自修室	103	未知	1	30438115	第一集[自修室]
30438115	自修室	103	未知	2	30438115	第二集[自修室]
30438115	自修室	103	未知	3	30438115	第三集[自修室]
25750923	神探夏洛克	102	瑞秋.塔拉雷	4	25750923	第一集[神探夏洛克]
25750923	神探夏洛克	102	瑞秋.塔拉雷	5	25750923	第二集[神探夏洛克]
25750923	神探夏洛克	102	瑞秋.塔拉雷	6	25750923	第三集[神探夏洛克]
21965460	战地神探	100	西蒙.兰顿	7	21965460	第一集[战地神探]
21965460	战地神探	100	西蒙.兰顿	8	21965460	第二集[战地神探]
21965460	战地神探	100	西蒙.兰顿	9	21965460	第三集[战地神探]
1301174	傲慢与偏见	101	西蒙.兰顿	10	1301174	第一集[傲慢与偏见]
1301174	傲慢与偏见	101	西蒙.兰顿	11	1301174	第二集[傲慢与偏见]
1301174	傲慢与偏见	101	西蒙.兰顿	12	1301174	第三集[傲慢与偏见]
```

* 自定义列输出

```mysql
USE db_douban;
SELECT t1.id, t1.tv_name, t1.tv_director, t2.tv_note
FROM douban_tv t1
INNER JOIN douban_tv_detail t2
ON t1.id=t2.tv_id;
```

输出

```
id	tv_name	tv_director	tv_note
30438115	自修室	未知	第一集[自修室]
30438115	自修室	未知	第二集[自修室]
30438115	自修室	未知	第三集[自修室]
25750923	神探夏洛克	瑞秋.塔拉雷	第一集[神探夏洛克]
25750923	神探夏洛克	瑞秋.塔拉雷	第二集[神探夏洛克]
25750923	神探夏洛克	瑞秋.塔拉雷	第三集[神探夏洛克]
21965460	战地神探	西蒙.兰顿	第一集[战地神探]
21965460	战地神探	西蒙.兰顿	第二集[战地神探]
21965460	战地神探	西蒙.兰顿	第三集[战地神探]
1301174	傲慢与偏见	西蒙.兰顿	第一集[傲慢与偏见]
1301174	傲慢与偏见	西蒙.兰顿	第二集[傲慢与偏见]
1301174	傲慢与偏见	西蒙.兰顿	第三集[傲慢与偏见]
```



###### 9.1.1  内联查询的步骤

* 第一步： 左表的记录和右表的记录逐一匹配
* 第二步：左表没有匹配到右表记录，这一行废弃
* 第三步：右表没有匹配到左表记录，这一行废弃

##### 9.2 左联查询

###### 9.2.1 左联查询的步骤

* 第一步： 左表的记录和右表的记录逐一匹配
* 第二步：左表的数据全部保留
* 第三步：右表的数据如果匹配到左表，那么右表数据保留
* 第四步： 右表的数据如果没有匹配到左表，那么左表的数据保留，右表的数据为空

```mysql
SELECT t1.id, t1.tv_name, t1.tv_director, t2.tv_note
FROM douban_tv t1
LEFT JOIN douban_tv_detail t2
ON t1.id=t2.tv_id;
```

输出

```
id	tv_name	tv_director	tv_note
30438115	自修室	未知	第一集[自修室]
30438115	自修室	未知	第二集[自修室]
30438115	自修室	未知	第三集[自修室]
1301174	傲慢与偏见	西蒙.兰顿	
21965460	战地神探	西蒙.兰顿	
25750923	神探夏洛克	瑞秋.塔拉雷	
```



###### 9.2.2  左联查询和右联查询的区别

##### 9.3 右联查询

###### 9.3.1 右联查询的步骤

* 第一步： 右表的记录和左表的记录逐一匹配
* 第二步：右表的数据全部保留
* 第三步：左表的数据如果匹配到右表，那么左表数据保留
* 第四步： 左表的数据如果没有匹配到右表，那么右表的数据保留，左表的数据为空

```mysql
SELECT t1.id, t1.tv_name, t1.tv_director, t2.tv_note
FROM douban_tv t1
RIGHT JOIN douban_tv_detail t2
ON t1.id=t2.tv_id;
```



##### 9.4 全联查询





















































