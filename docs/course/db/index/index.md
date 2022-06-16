---
date-created: 2022-06-13 19:42
date-updated: 2022-06-13 20:02
---

# Database Index

## 概述

数据库索引是为了便于在各样的操作中定位所需的数据项。根据索引方式可分为顺序索引、散列索引等。

## 顺序索引(ordered indices)

顾名思义，就是对数据进行顺序的索引，如下图所示：
![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220613194508.png)

上面这样的一一对应关系，又被称为**稠密索引***(Cluster Index)。
如果恰好数据本身就是依照这个索引顺序排列的，那么这个索引也被称为**主索引**(聚集索引)(Primary Index)；反之，则为**辅助索引**(非聚集索引)(Secondary Index)，比如下图：
![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220613195121.png)
对于**主索引**，我们可以采取**稀疏索引**(Dense Index)的方式节省索引空间：
![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220613195300.png)
但有时，直接稠密索引不能被直接放在Memory中（因为太大了），所以需要采用**多级索引**(Multilevel Index)的方式。分为outer index和inner index。![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220613195618.png)

### B+树索引

实际上B+树索引也属于顺序索引。顾名思义，就是利用B+树建立索引，B+树的内容可以参考[B+ Tree](Bplus.md)。
在实际的工业应用中，[B+ Tree](Bplus.md)往往会和[LSM Tree](lsm.md)结合使用，以减少在Disk中反复操作的overhead（写优化）。

## 散列索引

使用Hash表进行索引。
