"""
    生成器
"""

# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 比如说创建一个包含100万个元素的列表，它是会占用很大的存储空间的
# 如果我们只需要访问使用前面几个元素，那么后面剩余部分元素占用的空间都是摆摆浪费掉了的了。

# 像这种，列表元素可以按照某种算法推算出来的，我们就可以考虑在循环过程中不断地推算出后续元素，而不需要一次性创建完整的list，从而节省出大量的空间
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
# L = [x * x for x in range(10)] # L是一个list
# print(L) # ==> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# g = (x * x for x in range(5)) # g是一个generator
# 直接打印生成器，会报错
# print(g) # ==> <generator object <genexpr> at 0x0000013F821CC1C8>


# # 如何打印generator的每一个元素？
# # 1. 一个一个打印：
# print(next(g)) # ==> 0
# print(next(g)) # ==> 1
# print(next(g))  # ==> 4
# print(next(g))  # ==> 9
# print(next(g))  # ==> 16
# print(next(g))  # ==> 25
# print(next(g))  # ==> 抛出StopIteration的错误。

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。


# 一直调用next(g)十分不友好，generator也是可迭代对象，可直接使用for循环进行循环
# g = (x * x for x in range(5))
# for x in g:
#     print(x) # 注意，这里没有用next()，而是直接打印值
# # ===>
# # 0
# # 1
# # 4
# # 9
# # 16

# 可以看出，不用next()函数，直接使用for循环，就能取到generator的所有值，且不会存在抛出错误的情况。
# 通常情况下，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。


# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
# 举例：著名的斐波拉契数列（Fibonacci）
# 除第一个和第二个数外，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# 输出斐波拉契数列前 max 个数
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     print('done')
#
# fib(6) # 输出前6个
# ==>
# 1
# 1
# 2
# 3
# 5
# 8
# done


# 解释赋值语句：a, b = b, a + b
# 相当于：
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]


# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
# 也就是说，上面的函数和generator仅一步之遥。
# 要把fib函数变成generator函数，只需要把print(b)改为yield b就可以了：
