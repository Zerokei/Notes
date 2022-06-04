
# ECC

椭圆曲线可以定义为所有满足方程 $E: y^2=x^3+ax+b$ 的点(x,y)所构成的集合。

## ECC算法的六要素

- a，b：椭圆曲线系数
- p：模数
- 基点G（曲线上的一个点）
- G的阶n (n * G = O)
- 余因子 = 曲线的阶/G的阶

## ECC算法的数学基础

1. 椭圆曲线在素域$Z_p$上的运算规则
   - P+O=O+P=P;
   - 若P($x_1$,$y_1$), Q($x_2$,$y_2$)满足$x_1=x_2,y_1+y_2=0$，则P+Q=O;
   - 若P($x_1$,$y_1$), Q($x_2$,$y_2$)不满足上面的性质，则
     - $x_3 = \lambda^2-x_1-x_2$
     - $y_3=\lambda(x_1-x_3)-y_1$
     - 若$P\ne Q$，$\lambda=(y_2-y_1)/(x_2-x_1)$;
     - 若$P=Q$，$\lambda=(3x_1^2+a)/(2y_1)$.
2. 椭圆曲线的乘法性质
   - 若$Q=k*P$(k<n)，其中k是常数，Q、P是曲线上的点，则通过k,P计算Q简单，但是通过Q、P推算k较为复杂。

## OpenSSL中的ECC库

- 创建group `EC_GROUP *group=EC_GROUP_new(EC_GFp_simple_method());`
- a,b,p初始化group `EC_GROUP_set_curve_GFp(group,p,a,b,ctx);`
- 创建基点G并通过tx,ty初始化 `G=EC_POINT_new(group);` `EC_POINT_set_affine_coordinates_GFp(group,G,tx,ty,ctx);`
- G,n,余因子(1)设置group `EC_GROUP_set_generator(group, G, n, BN_value_one());`
- 获得点T的坐标(tx,ty) `EC_POINT_get_affine_coordinates_GFp(group,T,tx,ty,ctx)`
- ECC上的加法 T = T + G `EC_POINT_add(group,T,T,G,ctx)`
- ECC上的乘法 T = m * G `EC_POINT_mul(group,T,m,NULL,NULL,ctx)`
  - T = m * G + n * P `EC_POINT_mul(group,T,m,P,n,ctx)`

## ECC加密解密

- 公钥(公钥点) R = d * G
- 私钥 d (d < n)
- 加密(r(x),s)
  - r(x) = (k * G).x  ,其中k < n, r(x)结果不能对n取模
  - s = m * (k * R).x mod n, 其中m为明文
- 解密(利用私钥d)
  - 通过r(x)推出点r
  - m = s / (r * d).x
    = (m * (k * R).x) / (k * G * d).x
    = (m * (kd * G).x) / (kd * G).x
    = m

## ECC算法签名

- ecdsa(elliptic curve digital signature)
  - 签名(r,s)
    - r = k * G
    - s = (m + r * d)/k
  - 验证: (m / s) * G + (r / s) * G == r
- ecnr
  - 签名(r,s)
    - r = (k * G).x + m
    - s = k - (r * d).x
  - 验证: r - (s * G + r * R) == m