"""
    调试
"""
# 程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复bug。









# ================================================== print() ==================================================
# 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
# def foo(s):
#     n = int(s)
#     print('>>> n = %d' % n)
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()
#
# # ==》 报错









# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。
# ================================================== 断言 ==================================================
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：类似：
# $ python err.py
# Traceback (most recent call last):
#   ...
# AssertionError: n is zero!


# 注意：assert 语句在 Python 里默认只在 解释器以“调试模式”运行 时才生效。真正控制它是否被执行的开关是内建常量 __debug__


# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：
# $ python -O err.py
# Traceback (most recent call last):
#   ...
# ZeroDivisionError: division by zero

# 注意：断言的开关“-O”是英文大写字母O，不是数字0。
# 关闭后，你可以把所有的assert语句当成pass来看。











# ================================================== logging ==================================================
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：

# import logging
#
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# ==>
# Traceback (most recent call last):
#   File "D:\web\python-study-ljf\12.错误、调试和测试\12.2 调试.py", line 86, in <module>
#     print(10 / n)
#           ~~~^~~
# ZeroDivisionError: division by zero

# logging.info()就可以输出一段文本。但这个时候运行，发现除了ZeroDivisionError，没有任何信息。




# 别急，在import logging之后添加一行配置再试试：
# import logging
# logging.basicConfig(level=logging.INFO)
#
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# ==>
# INFO:root:n = 0                       // 多了行这条信息
# Traceback (most recent call last):
#   File "D:\web\python-study-ljf\12.错误、调试和测试\12.2 调试.py", line 107, in <module>
#     print(10 / n)
#           ~~~^~~
# ZeroDivisionError: division by zero

# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。











# ================================================== pdb ==================================================
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：
# # err.py
# s = '0'
# n = int(s)
# print(10 / n)


# 终端中执行：
# $ python -m pdb err.py
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(1)<module>()
# -> """
# (Pdb)



# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：
# (Pdb) l
#   1  -> """
#   2         12.2 调试文件
#   3     """
#   4
#   5     s = '0'
#   6     n = int(s)
#   7     print(10 / n)
# [EOF]
# (Pdb)


# 输入命令n可以单步执行代码：
# (Pdb) n
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(5)<module>()
# -> s = '0'
# (Pdb) n
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(6)<module>()
# -> n = int(s)
# (Pdb) n
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(7)<module>()
# -> print(10 / n)
# (Pdb) n
# ZeroDivisionError: division by zero
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(7)<module>()
# -> print(10 / n)
# (Pdb)



# 任何时候都可以输入命令   p 变量名     来查看变量：
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(1)<module>()
# -> """
# (Pdb) n
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(5)<module>()
# -> s = '0'
# (Pdb) p s
# *** NameError: name 's' is not defined
# (Pdb) n
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(6)<module>()
# -> n = int(s)
# (Pdb) p s
# '0'
# (Pdb) p n
# *** NameError: name 'n' is not defined
# (Pdb) n
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(7)<module>()
# -> print(10 / n)
# (Pdb) p n
# 0
# (Pdb)



# 输入命令q结束调试，退出程序：
# (Pdb) q

# 这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。












# ================================================== pdb.set_trace() ==================================================
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：


# 终端执行：$ python -m pdb err.py
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(1)<module>()
# -> """
# (Pdb) p s
# *** NameError: name 's' is not defined
# (Pdb) n
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(13)<module>()
# -> import pdb
# (Pdb) c
# > d:\web\python-study-ljf\12.错误、调试和测试\err.py(18)<module>()
# -> print(10 / n)
# (Pdb) p s
# '0'
# (Pdb)

# 这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。














# ================================================== IDE ==================================================
# 如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：
#
# Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。
#
# PyCharm：http://www.jetbrains.com/pycharm/
#
# 另外，Eclipse加上pydev插件也可以调试Python程序。