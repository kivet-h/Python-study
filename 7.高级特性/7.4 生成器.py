"""
    生成器
"""

# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 比如说创建一个包含100万个元素的列表，它是会占用很大的存储空间的
# 如果我们只需要访问使用前面几个元素，那么后面剩余部分元素占用的空间都是摆摆浪费掉了的了。

# 像这种，列表元素可以按照某种算法推算出来的，我们就可以考虑在循环过程中不断地推算出后续元素，而不需要一次性创建完整的list，从而节省出大量的空间
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
# L = [x * x for x in range(10)]
# print(L) # ==> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# g = (x * x for x in range(5))
# print(g) # ==> <generator object <genexpr> at 0x0000013F821CC1C8>
#
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
#     print(x) # 注意，这里没有用next，直接打印值
# # ===>
# # 0
# # 1
# # 4
# # 9
# # 16

# 可以看出，不用next()函数，直接使用for循环，就能取到generator的所有值，且不会存在抛出错误的情况

