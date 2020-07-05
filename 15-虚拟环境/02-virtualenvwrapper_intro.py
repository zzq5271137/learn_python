"""
virtualenvwrapper介绍
"""

"""
virtualenvwrapper这个软件可以让我们管理虚拟环境变得简单, 不用再跑到某个目录下通过virtualenv来创建虚拟环境,
也不用再跑到某个虚拟环境的具体目录下去启动虚拟环境;

安装virtualenvwrapper:
1. Linux:
   pip install virtualenvwrapper
2. Windows:
   pip install virtualenvwrapper-win

virtualenvwrapper的基本使用:
1. 创建虚拟环境:
   执行"mkvirtualenv 虚拟环境的名字"命令;
   执行这个命令后, 会在你当前用户下(C:/Users/用户名)创建一个"Envs"的文件夹(如果不存在的话), 
   然后将这个虚拟环境安装到这个目录下; 
   如果你当前机器的环境变量的配置中, Python3/Scripts的查找路径在Python2/Scripts的前面, 
   那么将会使用Python3作为这个虚拟环境的解释器; 如果Python2/Scripts的查找路径在Python3/Scripts的前面,
   那么将会使用Python2作为这个虚拟环境的解释器(以上讨论的情景是在你的机器上安装了Python2和Python3,
   并且他们都安装了virtualenvwrapper的情况下);
2. 进入虚拟环境:
   执行"workon 虚拟环境的名字"命令;
   它会去"C:/Users/用户名/Envs"文件夹下去找相应名字的虚拟环境(无论你控制台当前处在什么目录下, 都可以);
   只执行"workon"命令, 会列出"C:/Users/用户名/Envs"文件夹下所有已安装的虚拟环境;
   (Powershell和Cmder好像不太行, 得用CMD执行该命令)
3. 退出虚拟环境:
   无论你在哪个虚拟环境中, 无论你控制台当前处在什么目录下, 只需要执行"deactivate"命令, 就可以退出当前的虚拟环境;
   这个执行的"deactivate"命令并不是在虚拟环境的Scripts目录下查找的, 而是在你系统配置的系统变量中,
   你的配置的Python3/Scripts目录下查找的; 所以, 无论你在任何目录下, 执行"deactivate"命令, 都会退出虚拟环境;
4. 删除虚拟环境:
   rmvirtualenv 虚拟环境的名字
5. 列出所有虚拟环境:
   lsvirtualenv
6. 进入到当前Python环境所在目录:
   执行"cdvirtualenv"命令;
   执行这个命令, 会让你cd到当前Python环境所在的目录, 不论你是系统级的Python环境, 
   还是虚拟环境(不论该虚拟环境是在C:/Users/用户名/Envs下, 还是别的自己创建的地方), 都有用;
7. 修改mkvirtualenv的默认路径:
   在环境变量配置中, 添加一个参数WORKON_HOME, 将这个参数的值设置为你想要的路径;
8. 创建虚拟环境时指定Python解释器版本:
   mkvirtualenv --python==Python解释器的绝对路径 虚拟环境的名字
"""
