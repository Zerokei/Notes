---
date-created: 2022-06-03 23:17
date-updated: 2022-06-04 12:31
---

# 分组密码工作模式与流密码

## 1. 电子密码簿模式 ECB

Electronic codebook mode，将明文拆分成若干段，分别加密。

- ECB的加密过程：$C_j = E_k(P_j)$
- ECB的解密过程：$P_j = D_k(C_j)$
- ECB的缺点：同样内容的明文段，加密结果总是相同，容易被攻破
- ECB的优点：加密和解密过程均可并行

## 2. 密文块链接模式 CBC

Cipher Block Chaining Mode，加密过程如下，每次加密都依赖上一次的密文。加密流程如下图所示。  
![](https://s2.loli.net/2022/03/21/9vTicxaWhLOdreA.png)

- CBC缺点：加密过程只能串行
- CBC优点：相较ECB更为安全，且解密过程可以并行

## 3. 密文反馈模式 CFB

Cipher feedback mode
可以设置位移步长（当步长为一组的长度时，算法约等于CBC），组与组之间理论上存在相互印证关系，使得其在密文传输中若产生错误，也只会影响部分数据。

一般情况下，ECB的加密块大小为8byte，而CFB采用1byte。加密流程如下图所示。其中P为明文(P1,P2...Pn)，C为密文，Ek为以k为密钥的加密算法，X1为初始
![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220603234404.png)

- CFB优点：相较ECB更为安全，可以从传输的密文错误中恢复。

## 4. 流密码算法 RC4
