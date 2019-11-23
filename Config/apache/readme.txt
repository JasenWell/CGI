LoadFile "e:/python/anaconda3/python35.dll"
LoadModule wsgi_module "e:/python/anaconda3/lib/site-packages/mod_wsgi/server/mod_wsgi.cp35-win_amd64.pyd"
WSGIPythonHome "e:/python/anaconda3"
#pip install mod_wsgi-4.6.8+ap24vc14-cp35-cp35m-win_amd64.whl   mod_wsgi-express module-config 上面3项是安装自动生成的

D:\Sever\Apache\Apache24

Apache服务可能会因为各种原因导致无法启动，下面我们就一些常见的错误给出解决方案。

首先我们要学会查看apache的错误信息。
打开控制面板，打开管理工具，再找到事件查看器，通过windows日志中的应用程序即可查询报错内容。



参考了 https://www.jianshu.com/p/4e2794f9ff09

httpd -k install -n “服务名” 服务名必须加 apache2.4   安装apache服务
httpd -k uninstall    卸载服务

net start apache2.4 启动服务器
net stop apache2.4	关闭服务器