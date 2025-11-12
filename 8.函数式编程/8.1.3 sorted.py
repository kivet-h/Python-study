"""
    sorted
"""

# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较
# r = sorted([11,0,-10,-15,0])
# print(r) # ==> [-15, -10, 0, 0, 11]

# 但如果是字符串，或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。


# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
# r = sorted([11, 0, -10, -15, 0], key=abs)
# print(r) # ==> [0, 0, -10, 11, -15] # 注意：返回的元素还是排序的元素，不是通过key函数转换之后的元素




# 最字符串进行排序：
# 默认情况下，对字符串排序，是按照ASCII的大小比较的

# r = sorted(['bob', 'about', 'Zoo', 'Credit'])
# print(r) # ==> ['Credit', 'Zoo', 'about', 'bob'] # 由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

# # 默认情况下，对字符串排序，是按照ASCII的大小比较的，但可以通过key函数，让其忽略大小写进行排序
# r = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
# print(r) # ==> ['about', 'bob', 'Credit', 'Zoo']


# # 还能传入第三个参数，让其反向排序
# r = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
# print(r) # ==> ['Zoo', 'Credit', 'bob', 'about']



# # 示例：假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# # 别按名字排序：
# def by_name(t):
#     return t[0]
#
# L2 = sorted(L, key=by_name)
# print(L2) # ==> [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
#
#
# # 按成绩从高到低排序：
# def by_score(t):
#     return t[1]
#
# L2 = sorted(L, key=by_score)
# print(L2) # ==> [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]