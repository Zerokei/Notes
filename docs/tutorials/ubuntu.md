# Ubuntu 22.04 安装记录

## 0. 基础软件

```bash
$ sudo apt install tmux
$ sudo apt install git
$ sudo apt install vim
$ sudo apt install make
$ sudo apt install g++
```

## 1. Chrome浏览器

[参考安装文章](https://www.cnblogs.com/zhuangshenhao/articles/15532151.html)

## 2. 中文输入法

[参考安装文章](https://blog.csdn.net/weixin_44916154/article/details/124582379)

## 3. 局域网 ssh 登录

### 1) zjunet

[ZJUNET仓库](https://github.com/QSCTech/zjunet)

```bash
$ zjunet user add # 注意user name 后面要接上@abc，其中a表示10元，b表示30元，以此类推。
$ zjunet vpn -c
```

### 2) ssh服务

```bash
$ sudo apt-get install openssh-server
```

## 5. vivado

安装vivado2019.2

```bash
$ sudo apt install libncurses5
```

在`.bashrc` 文件中添加

```bash
$ source /opt/xilinx/Vivado/2019.2/settings64.sh
```

## 6. texlive

```bash
$ sudo apt install texlive
```

## 7. 添加新用户组

```bash
$ sudo groupadd nscscc2022
$ sudo useradd -m -G nscscc2022 ty # -m 创建目录 -G 添加至用户组
$ sudo useradd -m -G nscscc2022 wjj
$ sudo passwd ty
$ sudo passwd wjj
```

安装zsh

```bash
$ sudo apt install zsh
```

配置oh-my-zsh

```bash
$ sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh \
    | sed 's|^REPO=.*|REPO=${REPO:-mirrors/oh-my-zsh}|g' \
    | sed 's|^REMOTE=.*|REMOTE=${REMOTE:-https://gitee.com/${REPO}.git}|g')"
```

## 8. 龙芯环境配置

```bash
# install mipsel cross compiler
$ sudo apt install binutils-mipsel-linux-gnu gcc-mipsel-linux-gnu
$ sudo apt install gdb-multiarch
$ sudo apt install qemu-system-mipsel # 这个qemu的版本过高了

# install java
$ sudo apt install openjdk-11-jdk

# install sbt
$ sudo apt-get update
$ sudo apt-get install apt-transport-https curl gnupg -yqq
$ echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
$ echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
$ curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo -H gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/scalasbt-release.gpg --import
$ sudo chmod 644 /etc/apt/trusted.gpg.d/scalasbt-release.gpg
$ sudo apt-get update
$ sudo apt-get install sbt

# install verilator
$ sudo apt-get install verilator
```

## 9. docker安装
[参考安装文章](https://docs.docker.com/engine/install/ubuntu/#installation-methods) 

```bash
$ sudo apt-get update
$ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
$ sudo mkdir -p /etc/apt/keyrings
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
$  echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

### docker 解决qemu-system-mipsel版本问题
```bash
$ sudo docker pull ubuntu:20.04
$ sudo docker run -it -name ubuntu20 -v ~:/ccc ubuntu:20.04 /bin/bash #命名 目录挂载
$ sudo docker start ubuntu20
$ sudo docker exec -it ubuntu20 /bin/bash
```

```bash
$ apt-get update    
$ apt-cache madison qemu-system-mips # 查看可用版本
$ apt install qemu-system-mips=1:4.2-3ubuntu6.23
```
然后重复8中的步骤