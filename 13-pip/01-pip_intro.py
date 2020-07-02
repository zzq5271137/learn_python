"""
pip的基本使用
"""

"""
pip简介:
pip是Python的包管理工具, 它可以从远端服务器上下载你需要的所有包;
使用pip安装包或模块, 默认都是从"https://pypi.org/"这个网站上下载的(可以更改安装源);
pip是2008年发布的, 它是用来替代easy_install的;
Python有Python2和Python3的区别, 那么pip也有pip和pip3的区别, 大概是这样的:
1. pip是python的包管理工具, pip和pip3版本不同, 都位于"Python根目录/Scripts"下;
2. 如果系统中只安装了Python2, 那么就只能使用pip;
3. 如果系统中只安装了Python3, 那么既可以使用pip也可以使用pip3, 二者是等价的;
4. 如果系统中同时安装了Python2和Python3, 则pip默认给Python2用, pip3指定给Python3用;
5. 重要: 虚拟环境中, 若只存在一个Python版本, 可以认为在用系统中pip和pip3命令都是相同的;
6. 通过pip安装的包, 都位于"Python根目录/Lib/site-packages"下, 相应的脚本, 都放在"Python根目录/Scripts"下;

pip常用命令:
1. 安装包(默认安装最新版本):
   pip install django
2. 安装指定版本的包:
   pip install django==1.10.6
3. 卸载包:
   pip uninstall django
4. 升级包:
   pip install -U django
5. 升级pip:
   pip install -U pip
6. 查看当前pip版本:
   1). pip -V
   2). pip --verison
7. 显示某个已安装的包的信息:
   pip show -f django
8. 列出当前环境下安装了哪些包:
   pip list
9. 将当前环境安装的包全部列出来放在文件中:
   pip freeze > requirements.txt
10. 从某个文件中安装包:
    pip install -r requirements.txt
11. 临时更改安装源(以豆瓣镜像为例):
    pip install django -i https://pypi.douban.com/simple
12. 永久更改安装源(以豆瓣镜像为例):
    1). Windows:
        在用户目录下创建: pip/pip.ini, 然后在文件中添加:
        [global]
        index-url = https://pypi.douban.com/simple
    2). Linux/Mac:
        在用户目录下创建: .pip/pip.conf, 然后在文件中添加:
        [global]
        index-url = https://pypi.douban.com/simple

补充:
如果使用pip安装包总是失败(比如安装mysql-python), 你可以下载相应包的.whl文件, 然后手动安装;
手动安装也非常简单, 就是cd到那个.whl文件的目录下, 然后使用"pip install 你的whl文件"的形式进行安装;
"""
