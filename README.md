# 搭建私有pypiserver

## 使用方式

- 使用镜像codekoala/pypi
- 第一步是在在本机执行htpasswd -s /srv/pypi/.htpasswd yourusername 生成的文件映射到容器的srv/pypi中
- pip download -d \home\packs -r requirements.txt下载需要用到的包
- docker-compose启动容器后，只要把上一步下载好要添加的包推送到pypi文件夹即可
- 如用户需要使用本地的源文件，需要在本地的～/.config/pip下的pip.conf中设置，配置如下即可，在compose中设置fallbackurl，即可设置源的优先级，
```
[global]
timeout=40
index-url=http://192.168.0.238:9527/simple
extra-index-url=https://pypi.tuna.tsinghua.edu.cn/simple/

[install]
trusted-host=192.168.0.238
             pypi.tuna.tsinghua.edu.cn

```

> 使用了 https://github.com/codekoala/docker-pypi