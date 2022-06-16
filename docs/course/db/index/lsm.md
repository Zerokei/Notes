---
date-created: 2022-06-13 19:27
date-updated: 2022-06-13 19:35
---

# LSM Tree

## 基本概念

- 一种写优化的存储结构
- 采取分层存储的结构![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220613192949.png)
- 相比于B+树，它在总能保持在内存中写

## 具体策略

- Memory的$L_0$层满之后，直接写入Disk中的$L_0^1$层（只需要一次的seek即可）；
- 当Disk的$L_0$层满时，需要合并(Compaction)$L_0$层所有的树，然后再写入$L_1$层；
- 当涉及更新/删除操作时，同样化为插入操作执行插入。并在Compaction时正式执行。
