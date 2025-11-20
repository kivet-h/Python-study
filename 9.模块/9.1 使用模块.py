"""
    使用模块
"""

# Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。

# 我们以内建的sys模块为例，编写一个hello的模块：
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# ' a test module '
#
# __author__ = 'kivet'
#
# import sys
#
# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
# if __name__=='__main__':
#     test()


# 解释代码
# 顶部两行注释是标准注释
#!/usr/bin/env python3       # 这一行注释可以让当前.py文件直接在Unix/Linux/Mac上运行，
# -*- coding: utf-8 -*-      # 这一行注释表示.py文件本身使用标准UTF-8编码；



# ' a test module '
# # 是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；



# __author__ = 'kivet'
# # 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；


# 以上4行代码，就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。
# 后面开始就是真正的代码部分。


# import sys
# 使用sys模块的第一步，就是导入该模块
# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称。
# print(sys.argv) # ==> ['D:\\web\\python-study-ljf\\9.模块\\9.1 使用模块.py']

# 意思就是：
# 运行python3 hello.py获得的sys.argv就是['hello.py']；
# 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael']。


# if __name__=='__main__':
#     test()
# 当我们在命令行运行当前.py模块文件时，Python解释器把一个特殊变量__name__置为__main__，test()函数就会被执行，并输出对应结果
# 而如果在其他地方导入该模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。



# 比如说当前文件名字为：my_module.py，文件内容代码如下：
# import sys
#
# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('无传参，只有一个默认的参数，为当前文件的文件名：', args[0])
#     elif len(args)==2:
#         print('执行时传入了一个额外的参数，参数名为：%s，传入额外参数为：%s' % (args[0], args[1]))
#     else:
#         print('传入可超过一个的参数')
#
# if __name__ == '__main__':
#     test()

# 在终端命令行中执行以下命令，得到对应输出：（注意是终端中，不是Python的解释器里）
# python my_module.py
# ==> 无传参，只有一个默认的参数，为当前文件的文件名： my_module.py

# python my_module.py param2
# ==> 执行时传入了一个额外的参数，参数名为：my_module.py，传入额外参数为：param2

# python my_module.py param2 param3
# ==> 传入可超过一个的参数



# 存在另一个.py文件，如：other.py文件，导入使用了my_module.py文件，代码如下：
# import my_module.py

# 在终端中执行以下命令：
# python other.py
# 无任何输出，即运行other时，不会执行my_module.py模块文件中的函数。
# 原因：当 my_module 被别的文件 import 时，__name__ 的值是模块名 'my_module'，条件为假，整个if块会被跳过，所以test函数不会被执行。


# 即使你other.py文件中的代码为：
# import my_module
#
# my_module.test() # ==> 无传参，只有一个默认的参数，为当前文件的文件名： my_module.py
# 执行这行代码，会输出打印，但这只是现实得调用了test函数，也并不会触发 if __name__ == '__main__':这个if语句，
# 因为 my_module 是被 other 文件导入的，__name__ 的值是模块名 'my_module'，条件为假，整个块会被跳过。





# ================================================== 作用域 ==================================================
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。

# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
# 模块文件中定义的文档注释也可以用特殊变量__doc__访问，如在other.py文件中打印print(my_module.__doc__)，可以输出：a test module
# 我们自己的变量一般不要用这种变量名；

# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；


# 示例：
# def _private_1(name):
#     return 'Hello, %s' % name
#
# def _private_2(name):
#     return 'Hi, %s' % name
#
# def greeting(name):
#     if len(name) > 3:
#         return _private_1(name)
#     else:
#         return _private_2(name)

# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。