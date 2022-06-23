---
date-created: 2022-05-23 13:16
date-updated: 2022-06-23 09:21
---

# Randomized Algorithms

## Monte Carlo method

efficient raodomized algorithms that only need to yield the correct answer with high probability.

## Las Vegas algorithm

randomized algorithms that are always correct, and run efficiently in expectation.

## Hiring Problem

- 依次面试$N$个人，目的是找到最好的那个人。每个人面试完必须马上告知是否录用，如果已录用，必须支付代价$Ch$，每次面试也有代价$Ci$，但是$Ci\ll Ch$。
- **一般算法**：依次面试，期望时间开销为$Ch\times \log N + Ci\times N$
	- 因为对于第$i$个人，比前面$i-1$个人都优秀的概率为$\frac{1}{i}$，$\sum\limits^{N}_{i=1} \frac{1}{i}=\ln{N}$
- **Online Hiring Algorithm**：依次面试前面$k$个人，后面k+1~N的人中，若有比前面k个人优秀的，就直接录用，并结束面试
	- 定义两个事件
		- 事件A: 在最优秀的员工在位置$i$
		- 事件B: 位置在k+1~i-1的员工没有一个被雇佣
		- A和B相互独立，对于A，概率为$\frac{1}{N}$；对于B，概率为$\frac{k}{i-1}$ (前i-1个员工中最优秀的在前k个位置中)
	- 能雇佣到最优秀员工的概率为$\frac{k}{N}\ln(\frac{N}{k})\le Pr[S]\le \frac{k}{N}\ln(\frac{N-1}{k-1})$，$Pr[S]=\frac{k}{N}\sum\limits^{N-1}_{i=k}\frac{1}{i}$
	- 大约在$k=\frac{N}{e}$，概率取到最大值

## Quick Sort

### time complexity proof

假设$A^{j}_{i}$ 为第i位和第j位进行比较的事件，易知只有第i+1...j-1位没有被选成pivot时该事件才会发生，故$P(A^{j}_{i})=\frac{2}{j-i+1}$
$T=\sum\limits_{j}\sum\limits_{i}P(A^{j}_{i}) = O(n\log{n})$

### Modified Quick Sort

- central splitter：将数组分成两段的pivot并且每段至少是总长度的1/4
- Modified Quicksort：在开始递归之前选择出一个中心分割点
- 选出Modified Quicksort的期望次数为2（因为满足条件的点共占$\frac{1}{2}$）
