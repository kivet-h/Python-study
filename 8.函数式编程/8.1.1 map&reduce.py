"""
    map/reduce
"""

# Python内建了map()和reduce()函数。

# ================================================== map 函数 ==================================================
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# 示例：将一个list的所有元素求平方
# def ff(x):
#     return x * x
#
# r = map(ff, [0, 1, 2, 3, 4, 5])
# print(r) # ==> <map object at 0x000001B334B37EE0>
# print(list(r)) # ==> [0, 1, 4, 9, 16, 25]

# 为什么要用list()函数？
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。


# 示例二：将list的所有元素转换成字符串
# print(list(map(str, range(10)))) # ==> ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# ================================================== reduce 函数 ==================================================
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# # 示例：对一个list的元素求和
# def add(x, y):
#     return x + y
#
# from functools import reduce
# print(reduce(add, [1, 2, 3, 4, 5])) # ==> 15
#
#
# # 示例二：将list所有元素拼接成字符串
# def add(x, y):
#     return str(x) + str(y)
#
# from functools import reduce
# print(reduce(add, [1, 2, 3, 4, 5])) # ==> 12345（字符串类型）

# 示例三：[1, 3, 5, 7, 9]变换成整数13579
# def add(x, y):
#     return x * 10 + y
#
# from functools import reduce
# print(reduce(add, [1, 2, 3, 4, 5])) # ==> 12345（整数）


# ================================================== 结合使用 ==================================================
# 写一个str转换为int函数
# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
# def str2int(s):
#     def char2num(s_item):
#         return DIGITS[s_item]
#     def fn(x, y):
#         return x * 10 + y
#     return reduce(fn, map(char2num, s))
# print(str2int('12345')) # ==> 12345（整数）

# # 使用lambda函数进一步简化：（暂时了解即可）
# from functools import reduce
#
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
# def char2num(s):
#     return DIGITS[s]
#
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
