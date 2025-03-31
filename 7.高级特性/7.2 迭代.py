"""
    迭代
"""

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

# Python代码
# L = ['a', 'b', 'c', 'd']
# for item in L:
#     print(item)

# # JS 代码
# L = ['a', 'b', 'c', 'd']
# for (i = 0; i < L.length; i++) {
#     console.log(list[i])
# }

# 可以看出，Python的for循环抽象程度要高于C的for循环，
# 因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
# 在Python中，很多数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代。比如说dict

# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key, d[key])
# # ===>
# # a 1
# # b 2
# # c 3

# 有时候，例如上面dict，打印出来的顺序有可能不是a,b,c这种依次顺序，可能是a,c,b，或者其它顺序。
# 这是隐藏dict的存储不是安装list的方式顺序排序的，所以迭代出来的结果顺序可能不一样。

# 默认情况下，dict迭代的是key。
# 如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()。

# 字符串也是可迭代对象，因此，也可以用for循环进行迭代
# s = 'ABCD'
# for item in s:
#     print(item)

# 总结：在Python中，只要是可迭代对象，都可以使用for循环进行迭代。
# 常见可迭代对象有：list、tuple、dict、字符串


# 如何判断一个对象是否是可迭代对象？
# 答：通过collections.abc模块的Iterable类型判断
# from collections.abc import Iterable
# print(isinstance([1,2], Iterable)) # ==> True
# print(isinstance((1,2), Iterable)) # ==> True
# print(isinstance({'a':1, 'b': 2}, Iterable)) # ==> True
# print(isinstance('abc', Iterable)) # ==> True
# print(isinstance(123, Iterable)) # ==> False

# 如何对list实现类似Java那种下标循环？
# 答：Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
# L = ['A', 'B', 'C']
# for i, value in enumerate(L):
#     print(i, value)
# # ===>
# # 0 A
# # 1 B
# # 2 C

# for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)
# # ==>
# # 1 1
# # 2 4
# # 3 9