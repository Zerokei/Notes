---
date-created: 2022-06-16 13:27
date-updated: 2022-06-16 14:16
---

#db

# Relational Model

## 基本结构

- 一张表对应一个关系(relation)，行对应元组(tuple)，列对应属性(attribute)
- 码 key
	- Let $K \subseteq R$
	- $K$ is a **superkey** of $R$ is values for $K$ are sufficient to identify a unique tuple of each possible relation
	- $K$ is a **condidate key** is $K$ is minial superkey
	- $K$ is a **primary key**, if K is a candidate key and is defined **by user** explicitly
	- **Foreign key** Assume there exists relations $r$ and $s$: $r(A,B,C)$, $s(B,D)$, we can say that attribute $B$ in relation $r$ is foreign key referencing $s$, and $r$ is a referencing relation, and $s$ is a referenced relation.

## 关系代数

关系代数是Relational Model的数学基础，详见[Relational algebra](algebra.md)

## SQL

SQL：结构化查询语言，分为DDL,DML,DCL几种类型，详见[SQL](sql.md)