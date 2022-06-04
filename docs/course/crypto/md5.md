---
date-created: 2022-06-03 22:54
date-updated: 2022-06-03 23:03
---

# MD5

MD5是将明文处理成16byte的哈希摘要

## 用途

md5常与其他算法结合，用于数字签名，如邮件发送

### 加密过程

$$
\begin{aligned}
\rm m&={\rm md5}(letter)\\
\rm m'&={\rm rsa}(m,\rm private\ key)
\end{aligned}
$$

### 检验过程

$$
\begin{aligned}
\rm md5(letter) == \rm rsa(m, public\ key)\\
\end{aligned}
$$

## 实现

### 结构体定义

```c
typedef struct _MD5_CTX
{
	unsigned long state[4];
	unsigned long count[2]; /* 已处理的报文的二进制位数,最大值=2^64-1 */
	unsigned char data[4];  /* 64字节message块 */
}
```

### Init

对state赋初始值，清空count

### Update

每64个字节为一组，进行处理更新

### Final

因为不是所有的明文都是64字节的倍数，所以需要对缺失的内容进行补充，补充的内容包括**填充物**和**明文长度**

- 填充物
  0x80, 0x00, 0x00, ..., 0x00
- 规则![](https://s2.loli.net/2022/03/14/EfzviXS4w7OZ8BG.png)

## 破解

MD5的破解关键在于找到Collision

### Collision

${\rm md5}(x)={\rm md5}(x') \ \ (x\ne x')$

### rainbow table

一种较弱的MD5破解方法，关键在于**预计算**

- 找N组数据
- 对N组数据分别使用MD5处理K轮
- 对目标数X进行MD5处理，并将结果与N个(处理K轮后的)结果进行比较
- 若X与其中某个数相等，则根据X被MD5处理的轮数即可倒推出Collision
- 否则继续对X进行MD5处理
