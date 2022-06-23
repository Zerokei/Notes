---
date-created: 2022-04-18 08:52
date-updated: 2022-06-23 15:35
---

# Backtracking

## Definition

Backtracking enables us to **eliminate** the explicit examination of a large subset of the candidates while still guaranteeing that the answer will be found if the algorithm is run to termination.

## 八皇后问题

- 问题: 在棋盘中找到八个位置放置皇后，使得它们都不同行且不同列，也不能同时位于对角线上

## The Turnpike Reconstruction Problem

- 问题：在一条直线上找到n个地方建立加油站，已知它们两两之间的距离($N(N-2)/2$组)，求出所有加油站的位置，假定第一个加油站的坐标是0
- 算法流程
	1. 先将第一个加油站和最后一个加油站的位置确定，并将已经可以计算出的距离从路径中删除
	2. 找到剩下的距离中最大的距离并检验，不断重复上述过程，如果检验失败则回到上一种情况，恢复原本被删除的距离再往下回溯

## $\alpha-\beta$ 剪枝

### Minimax Strategy

- 在人机对弈的时候
- 人需要最小化当前情况P的可能赢的情况，而AI要将它最大化
- goodness函数$f(P)=W_{AI}-W_{Human}$，W是当前情况下某一方可能赢的所有结果，不需要考虑另一方后面会怎么下，只要计算自己在当前局势下的任何可以赢的方

### 剪枝策略

- α剪枝：min层在选最小值时，发现自己已经不可能是同一min层中的最大者，不可能被max层选中，剪掉其其所有未被遍历过的子节点。
- β剪枝：max层在选最小值时，发现自己已经不可能是同一max层中的最小者，不可能被min层选中，剪掉其其所有未被遍历过的子节点。
