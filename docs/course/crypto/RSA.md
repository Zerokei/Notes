# RSA

- e: 加密公钥
- d: 解密密钥
- N/n: 大数
- p,q: 两个素数
- m: 明文
- c: 密文

## 数学前提

- 欧拉函数 $\phi(n)$: 小于$n$，且与$n$互素的数的个数
- 欧拉定理：若$gcd(x,n)=1$，则$X^{\phi(n)}\equiv 1\mod n$
- 费马小定理：若p为素数，则$X^{p-1}\equiv 1 \mod p$
- 欧拉函数的乘法性质：若$\gcd(x,y)=1$，$\phi(xy)=\phi(x)\phi(y)$

## 密钥生成流程

- 选取两个大素数 p 和 q
- 计算出 n = p * q
- 随机选取加密密钥e(公钥)，使得 gcd(e,(p-1)(q-1))=1
- 计算出e在(p-1)(q-1)下的乘法逆元d，作为解密密钥(私钥)
- 公开(e,n)作为公钥

## 加解密

- 加密 $c=m^e\ {\rm mod}\ N$
- 解密 $m=c^d\ {\rm mod}\ N$

## RSA签名

- 加密邮件的步骤（信件L由A发给B）
  1. 信件L用B的公钥加密
  2. 把内容发给B
  3. B用私钥解密信件
- 验证邮件的步骤（信件L由A发给B）
  1. L做MD5摘要，M=MD5(L)
  2. 用A的私钥进行加密 M'=RSA(M,A的私钥)
  3. 把L、M'和A的公钥发送给B
  4. B用A的私钥解密 m=RSA(M',A的公钥)
  5. 判断MD5(L)是否等于m

## RSA正确性证明

已知 $c=m^e{\rm\ mod}\ N$, $cd\equiv 1 \mod (p-1)(q-1)$, p、q互素，$N=p*q$
证明 $m = c^d{\rm\ mod}\ N$

### Step1 公式化简

$$
\begin{aligned}
&c^d {\rm\ mod}\ N \\
=& (m^e)^d {\rm\ mod}\ N\\
=& m^{ed} {\rm\ mod}\ N\\
=& m^{k(p-1)(q-1)+1} {\rm\ mod}\ N\\
=& m*(m^{(p-1)(q-1)})^k {\rm\ mod}\ N\\
\end{aligned}
$$

### Step2 证明 $m^{(p-1)(q-1)}\equiv 1 \mod N$

$$
\begin{aligned}
&\because gcb(p,q)=1,\phi(p)=p-1,\phi(q)=q-1\\
&\therefore \phi(pq)=\phi(p)\phi(q)=(p-1)(q-1)\\
&\therefore m^{(p-1)(q-1)}=m^{\phi(pq)}=m^{\phi(N)}
\end{aligned}
$$

联想到了欧拉定理：若$\gcd(X,N)=1$，则$X^{\phi(N)}\equiv 1\mod N$
则需要证明 m,N互质。

$$
\begin{aligned}
&\because m<N, if\ \gcd(m,N)\ne1\\
&\therefore m={k_1}*q(k_1<p)\ {\rm or}\ {k_2}*p(k_2<q)\\
&\therefore gcd(m,N)=1
\end{aligned}
$$

所以
$m^{\phi(N)}\equiv 1\mod N$
因此

$$
e^d{\rm\ mod}\ N=m*(m^{\phi(N)})^k{\rm\ mod}\ N = m * 1^k{\rm\ mod}\ N = m{\rm\ mod}\ N = m
$$

QED
