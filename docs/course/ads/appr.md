---
date-created: 2022-05-09 13:36
date-updated: 2022-06-22 19:05
---

# Approximation

## Approximation Ratio

An algorithm has an approximation ratio of $\rho(n)$ if, for any input of size $n$, the cost $C$ of the solution produced by the algorithm is within a factor of $\rho(n)$ of the cost $C^{*}$ of an optimal solution: $max(\frac{C}{C^{*}}, \frac{C^*}{C})\le \rho(n)$

If an algorithm achieves an approximation ratio of $\rho(n)$, we call it a $\rho(n)-approximation\ algorithm$.

## polynomial-time approximation scheme(PTAS)

An approximation scheme is a _polynomial-time approximation scheme_ if for any fixed $\epsilon > 0$, the scheme runs in time polynomial in the size of its input instance. e.g. $O(n^{2/\epsilon})$

## fully time approximation scheme(FPTAS)

As a special case of PTAS, the run-time of an FPTAS is polynomial in the problem size and in $1/\epsilon$ e.g.$O((1/\epsilon)^2n^3)$

## Bin Packing Problem

### Description

给定$n$个物品，大小均在0～1之间，把它们装进若干个容量均为1的箱子，问容纳它们的箱子的最小数目$m$。

### On-line Algorithm

On-line Algorithm永远不可能最优，可证明$ratio\ge 5/3$

- Next Fit
	- 算法: 放在当前的bin中，不够则开新的bin
	- $ratio = 2$
- First Fit
	- 算法: 寻找第一个可放的bin，不然开新的bin
	- $ratio = 1.7$
- Best Fit
	- 算法: 寻找放入之后能占得尽可能满的bin，不然开新的bin
	- $ratio=1.7$

### Off-line Algorithm

- First Fit/Best Fit Decreasing
	- 算法: 按照从大到小的顺序排序，然后采用First Fit/Best Fit

## The Knapsack Problem

### fractional version

- 问题表述：背包容量为$M$，有N个物体，第i个物体的重量是$w_i$，价值为$p_i$。允许把物体的$x_i$比例装入，利益为$x_ip_i$。求利益最大装法。
- optimal algorithm: 选取$\frac{p_i}{w_i}$最大的尽可能装，以此类推。

### 0/1 version

- 问题表述：背包容量为$M$，有N个物体，第i个物体的重量是$w_i$，价值为$p_i$。只能选择装入或不装入，装入利益为$w_ip_i$。求利益最大装法。
- NP-hard Problem
- greedy算法的$ratio=2$

## K-Center Problem

### Description

对于平面上的$n$个点，找出不超过$k$个圆心的位置覆盖所有点，求最小半径

### Approximation

- 一个结论：选取n个点中的若干点，而非选取平面上的任意点。由下图可知，后者的任意方案，都可以通过前者用**两倍**的半径替代，故$ratio = 2$。

![pic|200](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220622190111.png)

- 具体算法：通过对目标半径$r$进行枚举，判断是否存在$k$个圆心的方案，二分查找获得。
- 除非$P=NP$，否则K-center问题不存在近似率小于2的逼近算法
