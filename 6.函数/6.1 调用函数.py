"""
    调用函数
"""

# Python内置了很多有用的函数，我们可以直接调用。
# 具体可直接翻阅官方文档查看：https://docs.python.org/zh-cn/3.13/library/functions.html

# 如：求绝对值，可以直接使用abs()函数
# print(abs(100)) # ==> 100
# print(abs(-100)) # ==> 100

# 数据类型转换
# print(int('123')) # ==> 123
# print(int(12.34)) # ==> 12
# print(float('12.34')) # ==> 12.34
# print(str(1.23)) # ==> '1.23'
# print(str(100)) # ==> '100'
# print(bool(1)) # ==> True
# print(bool('')) # ==> False

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
# a = abs # 变量a指向abs函数
# print(a(-1)) # 所以也可以通过a调用abs函数 ==> 1

