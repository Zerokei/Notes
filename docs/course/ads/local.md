---
date-created: 2022-05-16 14:29
date-updated: 2022-06-22 23:11
---

# Local Search

Local search solves problems approximately, aiming at a **local optimum**

- $S\sim S'$: $S'$ is a neighboring solution of S-S' can be obtained by a small modification of S
- $N(S)$: _neighborhood_ of S

## Vertex Cover

- 问题描述: 在无向图G中找出最小的点集S，对于G的每一条边，至少有一个顶点在S中
- 基础算法
	- 初始默认选取所有点，接下来每次删去一个点，直至不能删去。
- Metropolis Algorithm
	- 初始默认选取所有点，接下来每次删去/增加一个点。
	- 若是增加一个点，只有$e^{-\Delta cost/(kT)}$的概率可以通过。

## Hopfield Neural Networks

- 问题描述：给定带权边$w$的无向图G，要求对节点赋值$s$(正/负)，并满足下述要求
	- 定义好边和坏边(好边就是满足条件的边)：$w_es_us_v<0$
	- 对于一个顶点，如果其$\sum w_es_us_v<0$则称之为满足的，如果所有点都是满足的，那么这个图就是稳定的
- 算法
	- 每次选取一个点u，其$\sum w_es_us_v > 0$，并改变该点赋值，直至所有点均满足
	- 算法复杂度为$O(W)$，$W=\sum |w_e|$。因为每次翻转点，好边的和至少增加1，最多增加$W$次。

## Maximum Cut Problems

- 问题描述：给定一个图，找到一种将其点分成两个集合A、B的方法，使得两端分别在A、B中点边的权重和最大。
- 定理：局部最优解的权重和不会低于全局最优解的一半 $w(A,B)\ge \frac{1}{2}w(A*,B*)$
- big-improvement-flip 算法
	- 当新的局部最优解的增长的幅度小于$\frac{2\epsilon}{|v|}w(A,B)$的时候就停止，为了让算法可以在多项式时间内结束
	- 这样有 $(2+\epsilon)w(A,B)\ge w(A*,B*)$
	- 复杂度为$O(n/\epsilon \log W)$
