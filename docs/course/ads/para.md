---
date-created: 2022-05-30 13:22
date-updated: 2022-06-23 11:58
---

# Parallel Algorithms

## Parallel Random Access Machine (PRAM)

- Exclusive-Read Exclusive-Write (EREW)
- Concurrent-Read Exclusive-Write (CREW)
- Concurrent-Read Concurrent-Write (CRCW)

## Work-Depth(WD)

相比于PRAM，WD的每个时钟内，不一定所有CPU都在工作

## Measuring the performance

- W(n): 解决问题所要的基本操作数量
- T(n): 最坏时间复杂度，包括计算时间和并行时间两部分。

$$
\rm{Time\ Cost} = \begin{cases}
T(n) &P(n)>\frac{W(n)}{T(n)}\\
W(n)/P(n) &P(n) \le \frac{W(n)}{T(n)}\\
T(n)+W(n)/P(n) & for\ all\ P(n)\\
\end{cases}
$$

## Summation Problem

### PRAM Model

对于空闲的CPU，必须等待。
![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220623102512.png)

### WD Presentation

![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220623102518.png)

- $W(N)=O(N)$
- $T(N) = O(\log{N})$

## Prefix-Sums

- 问题：利用并行算法求前缀和

![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220623105334.png)

- 算法：自底至上计算B()，自顶向下计算C()
	- B(): 计算子树和
	- C(): 计算前缀和
	- $$
		                    \begin{cases}
		                    C(h,i)=B(h,i)& i==1\\
		                    C(h,i)=C(h+1,i)& i为偶数\\
		                    C(h,i)=C(h+1,\frac{i-1}{2})+B(h,i) & i为奇数且大于1
		                    \end{cases}
		$$
	- ![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220623105816.png)
- $T(N)=O(\log{N})$
- $W(N)=O(N)$

## Merging/Ranking Problem

- 问题：利用并行算法合并有序序列
- 算法
	- 要合并两个有序序列，需要先知道他们每个元素在对方序列中的排名，记为 `Rank`
	- 权衡二分查找和顺序遍历的利弊，采取分块的方式
	- 第一步(Partitioning)：在两个序列中各均匀取$\frac{N}{\log{N}}$个元素，采用二分查找的方法获取其位置
	- 第二步(Actual Ranking)：对于已知Rank元素之间的元素，采取顺序遍历的方式
- $T(N)=O(\log{N})$
- $W(N)=O(N)$

## Maximum Finding

### replace '+' by 'max' in the summation algorithm

- $T(N)=O(\log{N})$
- $W(N)=O(N)$

### 大功率跑车法

![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220623112142.png)

- $T(N)=O(1)$
- $W(N)=O(N^2)$

### Doubly-logarithmic Paradigm

- 方根分组法：把序列分成$\sqrt{n}$组，递归此方法，在找到最大值后，使用大功率跑车法合并
	- 有$T(n)\le T(\sqrt{n})+1$，$W(n)\le\sqrt{n}W(\sqrt{n})+n$
	- $T(N)=O(\log\log{n})$
	- $W(n)=O(n\log\log{n})$
- 双对数分组法: 把序列分成$\log\log{n}$组，递归此方法，在找到最大值后，使用大功率跑车法合并
	- 有$T(n)\le T(n/\log\log{n})+1$，$W(n)\le(n/\log\log{n})W(n/\log\log{n})+n$
	- $T(N)=O(\log\log{N})$
	- $W(N)=O(N)$

### Random Sampleing
- 算法流程：![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220623120319.png)
- $T(N)=O(1)$
- $W(N)=O(N)$
- 极大的概率得到正确答案，不正确的概率仅为$O(1/n^c)$