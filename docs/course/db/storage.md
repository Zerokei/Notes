---
date-created: 2022-06-13 20:04
date-updated: 2022-06-13 20:15
---

# Database Storage

Database的存储结构可由下图所示：
![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220613201216.png)

## Buffer Manager

- 通过将数据放到主存(Memory)中来提高访问效率。
- buffer manager：用于管理缓冲区中的内存分配。
- 涉及到buffer的替换算法。
  - LRU strategy：替换掉最近使用频率最低的block
  - FIFO：先进先出
  - Random：随机替换
  - Clock: LRU的约简版，有一个reference bit(second chance bit)
- 将数据从主存写入外存后才算是稳定存储（掉电不失）。

## Column-Oriented Storage

**行存储**(row-oriented representation)是最基本的存储方法，即将表中的数据一条一条存储。而**列存储**(column-oriented Storage)在有时可以发挥更大的功效。当然有时候可能也会采取行列混合存储的方式（hybrid row/column stores）。列存储方式如下图所示：![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220613200551.png)

### Benefit

- Reduced IO if only some attributes are accessed
- Improved CPU cache performance
- Improved compression
- Vector processing on modern CPU architectures

### Drawbacks

- Cost of tuple reconstruction from columnar representation
- Cost of tuple deletion and update
- Cost of decompression

### 行存储&列存储对比

![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220613145952.png)
