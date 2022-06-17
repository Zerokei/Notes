---
date-created: 2022-06-16 14:16
date-updated: 2022-06-16 16:45
---

# SQL

!!! note
    学习提示：SQL这一块的知识，讲究熟能生巧，涉及的语法很多，但不需要全部掌握，能解决实际需求就行。

## Data-Definition Language

提供定义关系模式、删除关系以及修改关系模式的命令

```sql
create table table_name1( 
	ID char(5), 
	name varchar(5) not null,  # 约束非空，也有像unique这样的限制
	dept_name varchar(20), 
	salary numeric(8, 2), 
	primary key (ID),  # 设置主码
	foreign key(dept_name) references table_name2,  # 设置外码
	check (salary >= 0)  # check(P) 确保表达式 P 在该关系中的存在 
)
```

```
drop table table_names; # 删除表及内容
delete table table_names; # 仅删除表的内容
alter table table_names add extra_attribute int; # 添加属性
alter table table_names drop extra_attribute; # 删除属性
```

## Data-Manipulation Language(DML)

### 查询

提供查询信息，在数据库中插入元组、删除元组、修改元组的能力。
查询语句的执行顺序为：$from\to where\to group(aggregate)\to having \to select \to order by$
查询函数的范式：

$$
\begin{aligned}
&{\rm SELECT\ <[DISTINCT]}\ c_1, c_2, ...>\\
&{\rm FROM}\ <r_1, ...>\\
&{\rm [WHERE\ <}condition>]\\
&{\rm [GROUP\ BY }<c_1,c_2,...>[{\rm HAVING}\ <cond_2>]]\\
&{\rm [ORDER\ BY\ <c_1\ [DESC][,c_2[DESC|ASC],...]>]}
\end{aligned}
$$

### group操作

- having相当于where的作用
- 聚合函数 avg/min/max/sum/count

```sql
select cno
from detail natural join pos
where year(detail.cdate)=2018
group by cno
having count(distinct campus)=1;
```

!!! warning
    需保证任何没有出现在 group by 子句中的属性，如果出现在 select/having 语句中，则必须在聚集函数中。


### 集合运算

- except/union/intersect  差集/并集/交集

```sql
select title from movie except
select title from movie
where exists ( 
	select *
	from comment A, comment B
	where A.title=movie.title and A.user_name = B.user_name and B.title=’ the avenger’ and A.grade <=B.grade )
```

### 嵌套子查询

- in/not in: 是否在子查询中
- exists: 子查询是否为空
- all/some： 比较大小

### 插入/删除/修改

```sql
# 插入
insert into table_name values();
# 删除
delete from table_name where P;
# 修改
update r
set attribute = ...
where P
# 修改(case)
update r
set attributes = case
	when ... then ...
	when ... then ...
	...
	else result
end
```

### with子句

```sql
with max_budget(value) as
	(select max(budget)
	 from department)
select budget
from department, max_budget
where department.budget = max_budget.value
```

### 创建索引/视图

```sql
# 创建索引
create index student_ID on student(ID);
# 创建视图
create view as <query expression>;
```

## 事务

事务由查询和更新语句的序列组成

## 授权

```sql
grant/revoke <权限列表> # 包括select, insert, update, delete
on <关系名或视图名>
to <用户/角色列表>;
```

## 数据类型

- 大对象类型
	- clob: 字符数据的大对象数据类 `book_review clob (10KB)`
	- blob: 二进制数据的大对象数据类 `image blob (10MB)`
- 用户定义新类型
	- `create type person_name as varchar(20)`
- 域
	- `create domain dollars as numberic(12,2) not null`
	- 可以加入约束性条件
