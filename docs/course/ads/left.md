---
date-created: 2022-04-18 08:48
date-updated: 2022-06-23 22:43
---

# Leftist Heaps

## Definition of NPL

The null path length, Npl(X), of any node X is the length of the shortest path from X to a node without two children. Define Npl(NULL) = -1. $Npl(X)=\min\{Npl(C)+1, \rm for\ all\ C\ as\ children\ of\ X\}$

## Definition of leftist heap

The leftist heap property is that for every node X in the heap, the null path length of the left child is at least as large as that of the right child.

## Theorem

A leftlist tree with $r$ nodes on the right path must have at least $2^{r} - 1$ nodes.

## Insertion(merge)

- Merge(H1->Right, H2)
- Attach(H2, H1->Right)
- Swap(H1->Right, H1->Left) if necessary

## DeleteMin

- Delete the root
- Merge the two subtrees

## Time Complexity

$T_p=O(\log{N})$
