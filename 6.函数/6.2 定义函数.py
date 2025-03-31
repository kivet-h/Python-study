"""
    定义函数
"""

# 在Python中，定义函数需要使用 def 语句。

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(2)) # ==> 2
# print(my_abs(-2)) # ==> 2


# 1. 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句
# def nop():
#     pass

# pass 语句的作用？
# pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
# pass也还可以用在其他语句里。如
# if age >= 18:
#     pass

# 2. 参数检查
# 数据类型检查可以用内置函数isinstance()实现
# val = 12
# print(isinstance(val, int)) # ==> True
# print(isinstance(val, float)) # ==> False
# print(isinstance(val, str)) # ==> False
# print(isinstance(val, (str, float))) # ==> False

# 3. 返回多个值
# 函数是可以一次性返回多个值的

# def batchReturn(m, n):
#     return m + n, m - n
# print(batchReturn(1, 2)) # ==> (3, -1)

# 但其实这只是一种假象，Python函数返回的仍然是单一值：
# 从返回结果可以看到，它其实是返回了一个tuple。
# 从语法上，返回一个tuple是可以省略括号的，而多个变量可以同时接收一个tuple，按位置赋给对应的值。
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。