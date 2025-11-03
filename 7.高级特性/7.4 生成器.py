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
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# f = fib(6)
# print(f) # ==> <generator object fib at 0x000001D1B04CC900>

# 解释：
# 这是定义generator的另一种方法。
# 如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个 generator 函数，调用一个 generator 函数将返回一个 generator


# generator 函数的执行流程：（generator函数和普通函数的执行流程不一样）
# 普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成 generator 的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 以上面例子为例
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# f = fib(6)
# print(next(f)) # ==> 1
# print(next(f)) # ==> 1
# print(next(f)) # ==> 2
# print(next(f)) # ==> 3
# print(next(f)) # ==> 5
# print(next(f)) # ==> 8
# print(next(f)) # ==> 报错

# 示例2：
# def odd():
#     print('step 11')
#     yield 1
#     print('step 22')
#     yield 2
#     print('step 33')
#     yield 3
#
# o = odd()

# 直接执行
# next(o) # ==> step 11
# next(o) # ==> step 22
# next(o) # ==> step 33
# next(o) # ==> 报错

# 打印值：
# print(next(o))
# # ==> step 11
# # ==> 1
# print(next(o))
# # ==> step 22
# # ==> 2
# print(next(o))
# # ==> step 33
# # ==> 3
# print(next(o))
# # ==> 报错

# 代码解释：odd不是普通函数，而是generator函数，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。




# 注意：
# 调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。
# def odd():
#     print('step 11')
#     yield 1
#     print('step 22')
#     yield 2
#     print('step 33')
#     yield 3
#
# next(odd()) # ==> step 11
# next(odd()) # ==> step 11
# next(odd()) # ==> step 11
# next(odd()) # ==> step 11

# 代码解释：上面多次next，返回的值都是一样的。这就是因为，odd()的时候会创建一个新的generator对象，即：上面代码实际上是创建了4个完全独立的generator，所以每次都是返回的第一个值。




# 使用for...in遍历获取值：
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# for n in fib(6):
#     print(n)

# ==>
# 1
# 1
# 2
# 3
# 5
# 8


# 上面示例输出结果可以看出，是拿不到最后return的done字符串的，如何能获取到？
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# g = fib(6)
# while True:
#      try:
#          x = next(g)
#          print('g:', x)
#      except StopIteration as e:
#          print('Generator return value:', e.value)
#          break

# ==>
# g: 1
# g: 1
# g: 2
# g: 3
# g: 5
# g: 8
# Generator return value: done


