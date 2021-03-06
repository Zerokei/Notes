---
date-created: 2022-06-23 15:53
date-updated: 2022-06-23 15:53
---

# Dynamic Program

动态规划（简称dp），是非常重要和常见的算法思想，基本想法也是把大问题
转化为较小的子问题，但与分治思想不同的是，分治是将大问题转化为若干个不相
关联的小问题，关键在于如何合并。而dp则是尝试从小问题开始，逐步生成最终的
大问题，关键在于如何推进生成。注意也要讲dp 区别于递归，递归是先从顶层考
虑，一路向下，遇到基本情况后再回溯，而dp则是先“搭地基”，把基本情况全部
解出，逐步向上最终得到结果，相比于递归，dp往往能减少重复计算，这是因为从
算法的形式来讲，dp的形式往往是迭代。
