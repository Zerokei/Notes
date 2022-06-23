---
date-created: 2022-04-18 08:49
date-updated: 2022-06-23 22:07
---

# Skew Heaps

a simple version of the [[C01N-Leftlist Heaps]]

## Character

Any M consecutive operations take at most $O(M\log{N})$ time

## Merge

Always _swap the left and right_ children except that the largest of all the nodes on the right paths does not have its children swapped.

## Analysis

### heavy node

A node p is heavy if the number of descendants of p's right subtree is at least half of the number of descendants of p, and light otherwise.

### Amortized Analysis

Proof
$T_{\rm amortized}=O(\log{N})$
Let
$\Phi(D_i)=\rm number \ of\ heavy\ node$
Thus

$$
\begin{aligned}
&\Phi_i = h_1+h_2+h\\
&\Phi_{i+1} \le l_1+l_2+h(\rm all \ the\ h_i\ will\ change\ into\ l_i)\\
\end{aligned}
$$

$$
\begin{aligned}
T_{\rm amoritized} &= T_{\rm worst}+\Phi_{i+1}-\Phi_{i}\\
&=(l_1+l_2+h_1+h_2) + \Phi_{i+1}-\Phi_{i}\\
&\le 2(l_1+l_2)
\end{aligned}
$$

light nodes along the right path: $l=O(\log{N})\to T_{\rm amortized}=O(\log{N})$
