---
date-created: 2022-06-13 20:21
date-updated: 2022-06-16 11:20
---

#db

# Query Processing & Optimization

查询处理共分为三个过程：执行(Parsing & Translation)、优化(Optimization)、估计(Evaluation)

## Parsing & Translation

### Measures of Query Cost

- $t_T$: time to transfer one block
- $t_S$: time for one seek
- Cost for b block transfers plus S seeks: $b*t_T + S*t_S$

### Selection

- Linear Search(equality on key): 线性搜索
	- worst cost: $b_r * t_T + t_S$ （关系表存放在$b_r$个block中）
	- average cost: $(b_r/2)*t_T + t_S$
- Primary B+-Tree index(equality on key): B+树主索引搜索
	- Cost: $(h_i+1)*(t_T+t_S)$，$h_i$是B+树的高度，每次需要从Disk中Seek该块并读入，而后面的1是指最后找到目标块时，需要进行seek+transfer(使用Index必不可少的)
- Primary B+-Tree index(equality on nonkey): B+树主索引，单值(非唯一)
	- Cost: $h_i*(t_T+t_S)+t_S+b*t_T$，其中b是包含查找值的数据块个数。
- Secondary B+-Tree index(equality on key): B+树辅助索引
	- Cost: $(h_i+1)*(t_T+t_S)$，和B+树主索引搜索原理一样
- Secondary B+-index on nonkey: B+树辅助索引，单值v(非唯一)
	- Cost: $(h_i + m+ n) * (t_T + t_S)$
	- m指B+树中，对应查找值v索引的块的数量
	- n指包含查找值v的数据块的数量
	- ![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220613212054.png)

### External Merge Sort

- M: memory size，内存共可存放的页的个数
- 大致流程可以通过下图表示：![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220615202516.png)
	- 第一轮传入M块数据，进行原地排序。（使用快排、堆排序等原地排序算法）
	- 第二轮及后面每轮，合并M-1个有序序列。
	- 注意，需要在memory块中预留一个区域存放排序好的有序序列，所以每轮合并后，有序序列的段数就少了M-1倍（预留出一个输出块的原因是：可以以块为单位写回，节省时间开销）
- block transfers
	- Total number of merge passes required: $\lceil \log_{M-1}(b_r/M)\rceil$ (第一次排序被视为初始化，不计入其中，可带入检验$b_r=M$和$b_r=M-1$的情况)
	- 因为在一轮归并排序中，一个块需要经历写入内存、然后写回磁盘，所以每轮的开销是 $2b_r$
	- 最后一轮排序，不计算写回disk的开销。
	- 所以总次数是$b_r(2\lceil \log_{M-1}(b_r/M)\rceil + 1)$
- seek times
	- 第一次排序：$\lceil b_r/M\rceil$ 次seek
	- 第二次排序及后面的排序：假设每次读入/写出的块数为$\lceil b_b \rceil$ 则需要$\lceil b_r/b_b\rceil$次读出和写入，此处共经历$\lceil \log_{M-1}{(b_r/M)} \rceil$轮排序，最后一轮不用写入，故一共为$\lceil b_r/b_b\rceil(2\lceil \log_{M-1}{(b_r/M)} \rceil -1)$次seek
	- 总计为$2\lceil b_r/M \rceil + \lceil b_r/b_b\rceil(2\lceil \log_{M-1}{(b_r/M)} \rceil -1)$

### Join

(1) Nested-Loop Join
$r\bowtie_\theta s$，伪代码如下：

```
for each tuple tr in r do begin
	for each tuple ts in s do begin
		test pair (tr, ts) to see if they satisfy the join condition
		if they do, add tr·ts to the result
	end
end
```

- 最坏情况（只能载入两个block，r/s各一个）
	- block transfers: $b_r+n_r*b_s$
		- r共要载入$b_r$次，而s共要载入$n_r*b_s$次
	- seek times: $b_r+n_r$
		- r共要seek $b_r$次，而s共要seek $n_r$次
- 最好情况（全部元组都能直接载入内存）
	- block transfers $b_r + b_s$
	- seek times: $2$

(2) Block Nested-Loop Join

```
for each block Br in r do begin
	for each block Bs in s do begin
		for each tuple tr in Br do begin
			for each tuple ts in Bs do begin
				test pair (tr, ts) to see if they satisfy the join condition
				if they do, add tr·ts to the result
			end
		end
	end
end
```

- 最坏情况（只能载入两个block，r/s各一个）
	- block transfers: $b_r+b_r*b_s$
		- r共要载入$b_r$次，而s共要载入$b_r*b_s$次
	- seek times: $2b_r$
		- r共要seek $b_r$次，而s共要seek $b_r$次
- 最好情况（全部元组都能直接载入内存）
	- block transfers $b_r + b_s$
	- seek times: $2$

(3) Indexed Nested-Loop Join

- 原理：外层遍历tuple，内层使用索引匹配（如B+树索引等）
- 最坏情况（只能载入两个block，r/s各一个）
- 因为索引本身的复杂度较复杂，故只给出较粗略的估算$b_r*(t_T+t_S)+n_r*c$
	- 其中$c$指单次查询的平均开销

(4) Merge-Join

- 算法流程
	1. 根据index的attributes进行排序
	2. 连接两个排序过的表（从头到尾扫描）
- 理想情况下（每个块只需要读进内存一次）
	- block transfers: $b_r + b_s$ +(排序)
	- seek times: $\lceil b_r/b_b\rceil + \lceil b_s/b_b\rceil$ +(排序)

(5) Hash-Join

大致流程如下

```
将r划分成nh个块
将s划分成nh个块

for 0 to nh-1
	对r对应块中的元素建立索引Ri
	for 遍历s对应块中的元素
		检索索引Ri
		for 所有匹配的tuple in r
			join
		end
	end
end
```

假设r,s分别被划分了$n_r,n_s$个块，但当$n_r,n_s>M$超过内存的容纳空间时，则需要进行递归划分。

- 若没有递归划分
	- block transfer: $3(b_r+b_s)+4n_h$
		- 划分过程需要遍历表，包含读出和写回 $2*(b_r+b_s)$
		- 匹配过程需要遍历表，只包含读出 $b_r+b_s$
		- 但是若Hash表非满，则至多制造出$n_h$个非满块，涉及划分的写回和匹配的读出，作用于两个表，故共$4n_h$ (实际中$n_h$一般很小，可以忽略不计)
	- seek times: $2(\lceil b_r/b_b\rceil +\lceil b_s/b_b\rceil)+2n_h$
		- 划分过程需要遍历表，假设每次放入内存块中$b_b$个，则读出写回共需$2(\lceil b_r/b_b\rceil +\lceil b_s/b_b\rceil)$次
		- 匹配过程中直接取Hash块，共$2n_h$
- 若有递归划分
	- 递归划分的原则是，每次将划分的大小降为原来的$M-1$，直至每个划分的最多占$M$块为止（使得内存能够容纳下，以便于建立索引）
	- block transfer: $2(b_r+b_s)\lceil log_{M-1}(b_s)-1\rceil+b_r+b_n$
		- 共进行$\lceil log_{M-1}(b_s)-1\rceil$轮
		- 其余参照没有递归划分的情况
	- seek times: $2(\lceil b_r/b_b\rceil +\lceil b_s/b_b\rceil)\lceil log_{M-1}(b_s)-1\rceil+2n_h$
		- 共进行$\lceil log_{M-1}(b_s)-1\rceil$轮
		- 其余参照没有递归划分的情况

## Evaluation

对一些单操作的复杂度有了解之后，可以使用物化(Materialization)和流水(pipelining)的方法将他们串起来

- 实体化：依次进行表达式的计算，构建前缀树递归进行
- 流水线：同时评估多个操作

## Optimization

### Equivalence Rule(等价关系表达式)

1. Conjunctive selection operations can be deconstructed into a sequence of indicidual selections $\sigma_{\theta_1\land\theta_2}(E)=\sigma_{\theta_1}(\sigma_{\theta_2}(E))$
2. Selection operations are commutative $\sigma_{\theta_1}(\sigma_{\theta_2}(E)) = \sigma_{\theta_2}(\sigma_{\theta_1}(E))$
3. Only the last in a sequence of projection operations is needed, the others can be ommitted.$\Pi_{L_1}(\Pi_{L_2}(...(\Pi_{L_n}(E))...))=\Pi_{L_1}(E)$
4. Selections can be combined with Cartesian products and theta joins.
		(1) $\sigma_{\theta}(E_1\times E_2) = E_1 \bowtie_\theta E_2$
		(2) $\sigma_{\theta_1}(E_1\bowtie_{\theta_2} E_2)=E_1\bowtie_{\theta_1\land\theta_2}E_2$
5. Theta-join operations (and natural joins) are commutative.$E_1\bowtie_\theta E_2 = E_2\bowtie_\theta E_1$
6. Natural join operatins are associative $(E_1\bowtie E_2)\bowtie E_3 = E_1\bowtie(E_2\bowtie E_3)$, Theta joins are associative in the following manner $(E_1\bowtie_{\theta_1} E_2)\bowtie_{\theta_2\land\theta_3} E_3 = E_1\bowtie_{\theta_1\land \theta_3}(E_2\bowtie_{\theta_2} E_3)$, where $theta_2$ involves attributes from only $E_2$ and $E_3$.
7. The selection operation distributes over the theta join operation under the following two conditions:
		(1) When all the attributes in $\theta_0$ involve only the attributes of one of the expressions ($E_1$) being joined $\sigma_{\theta_0}(E_1\bowtie_{\theta}E_2)=(\sigma_{\theta_0}(E_1))\bowtie_\theta E_2$
		(2) When $\theta_1$ involves only the attributes of $E_1$ and $\theta_2$ involves only the attributes of $E_2$. $\sigma_{\theta_1\land \theta_2}(E_1\bowtie_{\theta}E_2)=(\sigma_{\theta_1}(E_1))\bowtie_{\theta}(\sigma_{\theta_2}(E_2))$
8. The projetion operation distributes over the theta join operation as follows:
		(1) if $\theta$ involves only attributes from $L_1 \cup L2$: $\Pi_{L1\cup L_2}(E_1\bowtie_{\theta}E_2)=(\Pi_{L_1}(E_1))\bowtie_{\theta}(\Pi_{L_2}(E_2))$
		(2) Consider a join $E_1\bowtie_\theta E_2$.
		(3) Let $L_1$ and $L_2$ be sets of attributes from $E_1$ and $E_2$ respectively
		(4) Let $L_3$ be attributes of $E_1$ that are involved in join condition $\theta$, but are not in $L_1 \cup L_2$
		(5) Let $L_4$ be attributes of $E_2$ that are involved in join condition $\theta$, but are not in $L_1\cup L_2$
		$\Pi_{L_1\cup L_2}(E_1\bowtie_\theta E_2)=\Pi_{L_1\cup L_2}((\Pi_{L_1\cup L_3}(E_1))\bowtie_\theta(\Pi_{L2\cup L_4}(E_2)))$
9. The set operations union and intersection are commutative $E_1 \cup E_2 = E_2 \cup E_1$, $E_1\cap E_2 = E_2 \cap E_1$
10. Set union and intersection are assocative $(E_1\cup E_2)\cup E_3 = E_1 \cup (E_2\cup E_3)$, $(E_1\cap E_2)\cap E_3=E_1\cap(E_2\cap E_3)$
11. The selection operation distributes over $\cap$, $\cup$ and $-$ $\sigma_\theta(E_1-E_2)=\sigma_\theta(E_1)-\sigma_\theta(E_2)$
12. The projection operation distributes over union $\Pi_{L}(E_1\cup E_2)=(\Pi_L(E_1))\cup (\Pi_{L}(E_2))$

### Cost Estimation(结果集大小估计)

- 基本概念
	- $n_r$: number of tuples in a relation $r$
	- $b_r$: number of blocks containing tuples of $r$
	- $l_r$: size of a tuple of $r$
	- $f_r$: blocking factor of $r$
	- $V(A,r)$: number of distinct values that appear in $r$ for attribute $A$; same as the size of $\Pi_A(r)$
	- $b_r=\lceil \frac{n_r}{f_r} \rceil$
- 算法估计
	- 选择估计$\sigma_{A=v}(r)$
		- 一般假设为均匀分布
		- $n_r/V(A,r)$
	- 复杂选择估计
		- 合取$\sigma_{\theta_1\land \theta_2\land\dots\land\theta_n(r)}$: $n_r\cdot\frac{s_1\cdot s_2\dots s_n}{n_r^n}$
		- 析取$\sigma_{\theta_1\lor \theta_2\lor\dots\lor\theta_n(r)}$: $n_r\cdot(1-(1-\frac{s_1}{n_r})(1-\frac{s_2}{n_r})\dots(1-\frac{s_n}{n_r}))$
	- 连接估计$r\bowtie s$
		- 若两个关系无共同属性: $n_r · n_s$

		- 若共同属性是r的key: ${\rm size} \le n_s$ ![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220616100956.png)

		- 若共同属性是s到r的foregin key: $n_r$![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220616101006.png)

		- 若共同属性不是key: $\min(\frac{n_s\cdot n_r}{V(A,s)}, \frac{n_s\cdot n_r}{V(A,r)})$![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220616101205.png)
	- 投影: $\Pi(s)$: $V(A,r)$
	- 聚合: $\mathcal{G}(s)$: $V(A,r)$
	- 集合：转换为合取和析取
- Heuristic Optimization 探索式的优化
	- 尽早进行selection
	- 尽早进行projection
	- 选择最严格的selection和operations操作
