---
date created: 2022-04-18 09:03
date updated: 2022-04-18 09:29
date-updated: 2022-06-23 20:33
---

# Red-Black Trees

## Definition

- Every node is either red or black
- The root is black
- Every leaf(NIL) is black
- If a node is red, then both its children are black
- For each node, all simple paths from the node to descendant leaves contain the same number of black nodes

## Lemma

- A red-black tree with n internal nodes has height at most $2\ln(N+1)$
- Proof
	$$
	\begin{aligned}
	{\rm sizeof}(x) &= 1+2{\rm sizeof}(child)\\
	&\ge 1+2\cdot2^{bh(child)}\\ 
	&\ge 1+2\cdot2^{bh(x)-1}\\
	&\ge 1+2\cdot2^{h(x)/2-1}\\
	h(x)/2-1 &\le\ln(({\rm sizeof}(x)-1)/2) \le\ln({\rm sizeof }(x))\\
	h(x) &\le 2\ln({\rm sizeof(x)})+1
	\end{aligned}
	$$

## Insert

- the initial color of the node is **red**

![](https://s2.loli.net/2022/02/28/taOFWKVRxGmYAs5.png)

## Delete

- Delete a leaf node: Reset its parent link to NIL
- Delete a degree 1 node: **Replace** the node by its single child
- Delete a degree 2 node: **Replace** the node by the largest one in the left subtree or the smallest one in the right subtree.
- **the number of rotations in the DELETE operation is $O(1)$.**

### How to Replace

Accoring to the three situations, the second and third situation can be transfomed into situation 1.
Therefore, we only need to care about situation1 -- how to delete a leaf node.
Unfortunately, we can't delete leaf node directly, for the existence of external nodes.

- case1
	![](https://s2.loli.net/2022/02/28/YwlmEsORXGxrV1k.png)
- case2
	![](https://s2.loli.net/2022/02/28/B5Gmqe9FHdNcIVs.png)
- case3
	![](https://s2.loli.net/2022/02/28/ZAkrcqGnlstEQeY.png)
- case4
	![](https://s2.loli.net/2022/02/28/eJkIXrlug9yPKcH.png)
