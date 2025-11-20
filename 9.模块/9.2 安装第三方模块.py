"""
    安装第三方模块
"""

# 在Python中，安装第三方模块，是通过包管理工具pip完成的。


# 验证电脑使用安装成功pip？
# 终端执行命令: pip
# 如果没有报错，并输出了pip相关信息，则表示安装成功了的。


# 类比前端的npm，就是直接去安装对应的库
# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，
# 比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：pip install Pillow




# ================================================== 安装常用模块 ==================================================
# 在使用Python时，我们经常需要用到很多第三方库，例如，上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。
# 用pip一个一个安装费时费力，还需要考虑兼容性。
# 一般推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。


# 可以从Anaconda官网下载GUI安装包，安装包有500~600M，所以需要耐心等待下载。
# 下载后直接安装，Anaconda会把系统Path中的python指向自己自带的Python，
# 并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录。


# 安装好Anaconda后，重新打开命令行窗口，输入python，可以看到Anaconda的信息：
# C:\Users\kivet>python
# Python 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:17:27) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>>





# ================================================== 模块搜索路径 ==================================================
# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：
# import a_nonexistent_module
# Traceback (most recent call last):
#   File "D:\web\python-study-ljf\9.模块\9.2 安装第三方模块.py", line 43, in <module>
#     import a_nonexistent_module
# ModuleNotFoundError: No module named 'a_nonexistent_module'

# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块
# 搜索路径存放在sys模块的path变量中：
# >>> import sys
# >>> sys.path
# ['D:\\Software\\Install\\PyCharm\\PyCharm 2024.3.4\\plugins\\python-ce\\helpers\\pydev', 'D:\\web\\python-study-ljf', '...']

# 如果我们要添加自己的搜索目录，有两种方法：
# 一是直接修改sys.path，添加要搜索的目录：
# >>> import sys
# >>> sys.path.append('/Users/michael/my_py_scripts')
# 这种方法是在运行时修改，运行结束后失效。


# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加我们自己的搜索路径，Python本身的搜索路径不受影响。