"""
    切片
"""

# 取一个list或tuple的部分元素

# 如取一个list前3个元素
# 方式一：下标的方式
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print([L[0], L[1], L[2]]) # ==> ['Michael', 'Sarah', 'Tracy']


# 方式2：循环
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# def my_slice(list, n):
#     result = []
#     for i in range(n):
#         result.append(list[i])
#     return  result
# print(my_slice(L, 3)) # ==> ['Michael', 'Sarah', 'Tracy']


# 方式三：切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3]) # ==> ['Michael', 'Sarah', 'Tracy']


# 对这种经常取指定索引范围的操作，用循环是十分繁琐的，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果第一个索引是0，还可以省略：L[:3]


# 类似的，Python同样支持倒数切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[-3:]) # ==> ['Tracy', 'Bob', 'Jack']
# print(L[-3:-1]) # ==> ['Tracy', 'Bob']
# 记住：倒数第一个元素的索引是-1。


# 每隔2个取值
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(L[:]) # ==> [1, 2, 3, 4, 5, 6, 7, 8, 9]  直接复制一个L
# print(L[::2]) # ==> [1, 3, 5, 7, 9]
# print(L[:9:2]) # ==> [1, 3, 5, 7, 9]
# print(L[:5:2]) # ==> [1, 3, 5]


# 直接使用[:]， 能直接复制一个L，并且是深拷贝，修改复制后的list不会影响到原list
# L = [1, 2]
# CL = L[:]
# CL.append(3)
# print(L, CL) # [1, 2] [1, 2, 3]


# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
# T = (1, 2, 3, 4, 5)
# print(T[1:3]) # ==> (2, 3)


# 同样，字符串也可以看成是一种list，
# print('ABCDEFG'[:3]) # ==> ABC
# print('ABCDEFG'[::2]) # ==> ACEG

