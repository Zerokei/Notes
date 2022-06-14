---
date-created: 2022-06-03 23:51
date-updated: 2022-06-04 00:09
---

!!! info
	- 2022/6/14 修改Enigma加密流程图

# 古典密码

明文(plaintext) ---> 密文(ciphertext)

## 单表密码

- 使用明文密文对照表

## 仿射密码

$x = (y \times k_1+k_2 )\%n$  
$y = (x-k_2)\times k^{-1} \%n$

## 多表密码

每个明文字母采用不同的单表替换（同一明文字母对应多个密文字符）

### Vigenere Algorithm

```
明文: this cryptto system is not secure
密钥: cipher cipher cipher cipher cipher
密文: VPXZGIA...
t+c = v
t+p = i
```

## Enigma

```
Date: 每一天的密码设计
Ringstellung (delta)添加增量
Steckerverbindungen: 十对字母的相互转化
Kenngrunppen: 和日期对应 方便情报归类
```

### 部件与概念

- rotor1，字母表1
- rotor2，字母表2
- rotor3，字母表3
- reflactor，字母两两对应
- wiring board，连接对应字母
- message key，三个rotor**外面**的显示，外部delta
- ring setting，三个rotor**内部**的设置，内部delta
- delta = message key - ring setting

### 具体加密流程

```
plaintext -> wiring board 
          -> +delta1 -> rotor1 -> -delta1
		  -> +delta2 -> rotor2 -> -delta2
		  -> +delta3 -> rotor3 -> -delta3
		  -> reflactor 
		  -> +delta3 -> rotor3 -> -delta3
		  -> +delta2 -> rotor2 -> -delta2
		  -> +delta1 -> rotor3 -> -delta1 
		  -> wiring board 
		  						-> cripertext
```

同理可知加密、解密是完全可逆的过程  

### 齿轮跳转规则

QEVJZ  
RFWKA  

1. 常规跳转
   - 每按一下，齿轮I跳转一下
   - 当齿轮I从位置Q转到R时，齿轮Ⅱ被带动跳转一下
2. double stepping
   - 当齿轮I从位置Q转到R时，齿轮Ⅱ被带动跳转
   - 若此时齿轮Ⅱ是从D跳转到E，则下一次齿轮Ⅱ从E跳转到F，并带动齿轮Ⅲ跳转
   - 可以理解为 I=Q,Ⅱ=D,Ⅲ=X -> I=R,Ⅱ=E,Ⅲ=X -> I=S,Ⅱ=F,Ⅲ=X+1
