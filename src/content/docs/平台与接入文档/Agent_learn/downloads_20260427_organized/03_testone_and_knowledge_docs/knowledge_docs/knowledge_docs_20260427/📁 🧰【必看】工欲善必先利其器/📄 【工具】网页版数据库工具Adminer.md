---
title: "1、安装ODP"
description: "【工具】网页版数据库工具Adminer"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🧰【必看】工欲善必先利其器\\📄 【工具】网页版数据库工具Adminer.md"
---
【工具】网页版数据库工具Adminer

本地开太多IDE太烦了？试试这个轻量级的网页版MySQL数据库工具



# 1、安装ODP
mkdir odp

cd odp

wget '[http://odp.baidu.com/download/odp-3.1.1-develop-nginx-php-5.4.tar.gz](http://odp.baidu.com/download/odp-3.1.1-develop-nginx-php-5.4.tar.gz)'

tar zxvf odp-3.1.1-develop-nginx-php-5.4.tar.gz

./bin/odp_install

 php/sbin/php-fpm start

webserver/loadnginx.sh start   （如果启动的时候端口冲突，修改 webserver/conf/vhost/php.conf 里面的端口即可）

# 2、下载adminer
cd webroot

wget [https://github.com/vrana/adminer/releases/download/v4.7.7/adminer-4.7.7.php](https://github.com/vrana/adminer/releases/download/v4.7.7/adminer-4.7.7.php) （网络问题的话，下载到本地，然后rz上传到对应目录）

sed -i 's/is_utf8/is_utf_8/' adminer-4.7.7.php   (函数命名冲突，修改一下)

# 3、访问
[http://{YOUR_HOST}:{YOUR_PORT}/adminer-4.7.7.php](http://testone-test.bcc-szzj.baidu.com:8000/testone-database-proxy.php)
