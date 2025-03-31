"""
    列表生成式
"""

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 如：要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
# print(list(range(1,11))) # ==> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成：[1x1, 2x2, 3x3, ..., 10x10]
# 方法一：循环
# L = []
# for x in range(1, 11):
#     L.append(x * x)
# print(L) # ==> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 方法二：列表生成式
# val = [x * x for x in range(1, 11)]
# print(val) # ==> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来。

# for循环后面还可以加上if判断，如只需要偶数的平方：
# val = [x * x for x in range(1, 11) if x % 2 == 0]
# print(val) # ==> [4, 16, 36, 64, 100]

# for循环还可以再套for循环
# val = [m + n for m in 'ABC' for n in 'XYZ']
# print(val) # ==> ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
# 三层及三层以上，也能实现，但是实际开发中很少这么用。

# 运用列表生成式，可以写出非常简洁的代码，如：打印出当前文件同级目录下所有文件名称
# import os
# val = [d for d in os.listdir('.')]
# print(val) # ==> 打印出当前文件同级目录下所有文件名称，list形式

# 前面迭代有介绍，for循环是可以同事使用两个甚至多个变量，如dict的items()可以同时迭代key和value
# d = {'a': 1, 'b': 2, 'c': 3}
# for k, v in d.items():
#     print(k, '=', v)
# # ==>
# # a = 1
# # b = 2
# # c = 3

# 列表生成式也可以使用两个变量来生成list
# d = {'a': 'A', 'b': 'B', 'c': 'C'}
# val = [k + '=' + v for k, v in d.items()]
# print(val) # ==> ['a=A', 'b=B', 'c=C']

# 把一个list中所有的字符串变成小写：
# L = ['Hello', 'World', 'IBM', 'Apple']
# val = [s.lower() for s in L]
# print(val) # ==> ['hello', 'world', 'ibm', 'apple']

# 在列表生成式中使用if...else
# val = [x if x % 2 == 0 else -x for x in range(1, 11)]
# print(val) # ==> [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

# 写法解释：for前面的部分是一个表达式，它必须根据x计算出一个结果。如果只有x if x % 2 == 0 没有else的话，是计算不出结果的
# val = [x if x % 2 == 0 for x in range(1, 11)]
# print(val) # ==> 报错

# 上面[x if x % 2 == 0 else -x for x in range(1, 11)]中，for前面的表达式x if x % 2 == 0 else -x才能根据x计算出确定的结果。

# # for循环后面的else
# val = [x for x in range(1, 11) if x % 2 == 0 else 0]
# print(val) # ==> 报错

# 总结：可见，在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
