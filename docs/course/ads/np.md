---
date-created: 2022-04-18 14:09
date-updated: 2022-06-22 17:31
---

# NP Completeness

- Decision problem (yes/no)
- Search problem (find the answer)
- Optimization problem

## Nondeterministic Turing machine

- A **Deterministic Turing Machine** executes one instruction at each point in time. And then depending on the instruction, it goes to the next unique instruction.
- A **Nondeterminism** is now typically represented by giving a machine an extra input, the certificate or witness.

## NP

- NP: Nondeterministic polynomial-time
- NP Problem: 在 polynomial-time 时间内可以验证的问题。
- $NP \overset{?}{=} P$: 是否所有能在 polynomial-time 时间内**验证**的算法都能在 polynomial-time 内被**解决**

## Reduction and NP-Complete Problems

An **NP-complete problem** has the property that any problem in NP can be polynomially reduced to it.

### reduction 约化

To prove a reduction $A\le_P B$ , we require 3 steps

1. We have to find the mapping function $f$ and show that it runs in polynomial time.
2. for all $x \in A$, then $f(x) \in B$
3. If $f(x)\in B$, then $x\in A$

### 常见 NPC 问题

- SAT Problem(第一个被证明为 NPC 的问题): 给定一个n个布尔变量组成的布尔表达式，判断其有没有可能为真
- Hamiltonian cycle Problem: 给定一个图，判断是否有一个simple cycle恰好经过每个顶点一次
- Traveling Problem: 给定一个带权图，问是否存在一个simple cycle经历过每个节点且经历边的权重和不超过K?
- Vertex Cover Problem: 给定一个图，判断是否存在其一个大小不超过K的点集，使得图中任一条边至少有一个顶点在这个点集中
- clique problem: 给定一个图，判断图是否有一个大小至少为K的完全子图（团）。

## NP-Hard

If a NP-Hard problem is in NP, it is a HP-complete problem.

![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/3333.png)

### 常见NP-hard问题

- 所有NP-Complete问题
- Halting problem(不属于NP-Complete)

## Formal-language Theory*

- An alphabet $\Sigma$ is a finite set of symbols
- A language $L$ over $\Sigma$ is any set of strings mode up of symbols from $\Sigma$
- Denote empty string be $\varepsilon$
- Denote empty language by $\emptyset$
- Language of all strings over $\Sigma$ is denoted by $\Sigma^{\star}$
- The complement of $L$ is denoted by $\Sigma^{\star}-L$
- The concatenation of two languages $L_1$ and $L_2$ is the language $L=\{x_1x_2: x_1\in L_1\ {\rm and}\ x_2\in L_2\}$
- The closure of _Kleene star_ of a language $L$ is the language $L^{\star}=\{\varepsilon\}\cup L\cup L^2\cup L^3\cup \cdots$, where $L^k$ is the language obtained by cocncatenating $L$ to itself $k$ times
