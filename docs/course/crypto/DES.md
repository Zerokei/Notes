---
date-created: 2022-06-04 11:25
date-updated: 2022-06-04 12:29
---

# DES

!!! info
    - 2022/6/14 DES加密过程补充（R(48)和key异或）

Data Encryption Standard  
密钥长度为64bit  
明文加密可采用ECB、CBC、CFB  

## 大致流程

![](https://s2.loli.net/2022/04/02/cQjivrnl1ZwLfuJ.png)

## 密钥处理

- key密钥
    - 密钥，64bit
    - 经过处理生成16个48bit的key，用于16轮加密循环
- key初始化
    - 用户指定初始密钥
    - `key_perm_table`: 从8字节的key中选择56bit，并拆分成左右两半(28bit+28bit)
- key循环过程
    1. `key_rol_steps`，两个28bit分别循环左移
    2. `key_56bit_to_48bit_table`: 从56bit中选出48个bit
    3. 继续执行步骤a

## DES加密

- IP(64bit->64bit)
    - 置换
    - 使用perm进行查表优化
- f(R(32),key(48)) (32bit->32bit)
    - 经过位选择函数E R(32)->R(48) (32bit->48bit)
    - R(48)和key(48)异或
    - S盒 `char S[8][64]` `8*(a1a2a3a4a5a6) = 8*S[a1a6][a2a3a4a5]` (48bit->32bit)
        - ![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220604121538.png)
    - 置换函数P(32bit->32bit)
- FP(64bit->64bit)
    - IP-1，IP的逆运算
    - 使用perm进行查表优化

## 三重DES

c = E(D(E(p,k1), k2), k3)  
p = D(E(D(c,k3), k2), k1)
