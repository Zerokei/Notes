
# mkdocs 安装记录

## 本地环境配置

```bash
pip install mkdocs-material
mkdocs new .
```

## 修改mkdocs.yml

设置material主题

```yml
#添加下列代码
theme:
  name: material
```

## 远程部署

采用Github远程部署

### 1. 创建github仓库
### 2. 上传本地的代码
### 3. 设置github action
使用下方代码创建一个新的github action
```yml
name: ci 
on:
    push:
    branches:
        - master 
        - main
jobs:
    deploy:
    runs-on: ubuntu-latest
    steps:
        - uses: actions/checkout@v2
        - uses: actions/setup-python@v2
        with:
            python-version: 3.x
        - run: pip install mkdocs-material 
        - run: mkdocs gh-deploy --force
```
### 4. 设置渲染分支
在Setting页设置渲染的分支
![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220603102723.png)
### 5. 自动渲染
等候渲染成功，即可访问 `<username>.github.io/repository_name`

## 参考资料

[使用MkDocs 快速搭建文档系统](https://www.bluesdawn.top/489/)
[MkDocs Material](https://jamstackthemes.dev/demo/theme/mkdocs-material/)
[Github多域名部署](https://www.cnblogs.com/dev2007/p/13947333.html)
