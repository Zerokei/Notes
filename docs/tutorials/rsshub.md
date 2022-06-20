# RSSHub
!!! note
    目前采用的是docker部署，长期使用比较稳定，缺点可能是为配合RSSHub radar，需要偶尔手动更新docker镜像。
## RSSHub安装
1. 需要一个服务器/不断电的机子
2. 安装docker
3. 部署RSSHub镜像
    ```bash
    $ docker pull diygod/rsshub
    $ docker run -d --name rsshub -p 1200:1200 diygod/rsshub
    ```
4. 打开ip:1200，若显示下方内容，则部署成功![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/image-20220620090822856.png)

## RSSHub更新
```bash
$ docker stop rsshub
$ docker rm rsshub
$ docker pull diygod/rsshub
$ docker run -d --name rsshub -p 1200:1200 diygod/rsshub
```
## Reference
- [RSSHub Docker部署](https://docs.rsshub.app/install/#docker-bu-shu)