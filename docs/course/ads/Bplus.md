---
date-created: 2022-04-18 09:00
date-updated: 2022-06-23 21:09
---

!!! tips
    - 和 [Database B+ Tree](../db/index/Bplus.md) 是一个原理，相比之下，数据库里的用法和规定更加严谨。

# B+ Trees

## Definition

A B+ tree of order $M$ is a tree with the following structural properties:

- The root is either a leaf or has between 2 and M children.
- All nonleaf nodes (except the root) have between $\lceil M/2 \rceil$  and $M$ children.
- All leaves are at the save depth, have $\lceil \frac{M}{2}\rceil\sim M$ elements.

## Apperance

![](https://s2.loli.net/2022/03/07/MihsWEO5UxFLPfm.png)

## Time Complexity

- ${\rm depth} = \log_{\lceil M/2 \rceil}{N} = \frac{\log{N}}{\log{M}}$
- ${\rm T} = M \times {\rm depth} = M \log{N} / \log{M}$
