---
date-created: 2022-05-30 15:21
date-updated: 2022-06-23 15:02
---

# External Sorting

!!! tip
    - 在 ![Database Query Process](../db/query.md) 中提到过External Sort。

## What are the concerns

- Seek time: O(number of passes)
- Block transfers: Time to read or write one block of records
- Time to **internally sort** M records
- Time to merge N records from input buffers to the output buffer

## How to reduce the number of passes?

- 使用 k-way merge，passes = $1+\lceil \log_k(N/M)\rceil$，但是需要2k的tapes
- 当然也可以使用斐波那契式的合并方法，只需要k+1个tapes

## How to Handle the Buffers for parallel operation?

![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220623141041.png)

- 对buffer的读取/写回进行优化
- 对于一个K路归并，需要2k个输入buffer和2个输出buffer来进行并行操作
	- 为什么不是k和1？答：因为是一个正式一个缓冲
- 事实上K不是越大越好，因为如果K增大，就会导致input buffer的数量需求增加，导致buffer size减少，导致磁盘中一个block的size减少，导致访问磁盘的seek time增加，因此最优的K值取决于磁盘的参数和外部memory的规模

## How to generate a longer run?

- 使用堆的结构来进行排序操作，规则是一直取出堆中现存的可以放在现在所在的run后面的最小的数，直到堆中的数据都放不进当前run了再更换一个run
- 如果内存可以容纳M个元素，则这种方法生成的run的平均长度为2M
- 在输入的元素**接近已经排好序**的状态时非常有效

## How to minimize the merge time?

使用Huffman树
![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220623140112.png)
