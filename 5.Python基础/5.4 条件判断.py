"""
    条件判断
"""

# ========== if...elif...else
# 1. 写法举例
# age = 20
# if age > 20:
#     print('年龄大于20岁！')
# elif age == 20:
#     print('年龄为20岁')
# else:
#     print('年龄小于20岁')

# if语句的执行特点是，它是从上往下判断的，如果执行到某个判断上为true，把这个判断对应的代码块执行完之后，就会跳过剩下的elif和else。

# 2. if 简写
# x = 0 # ==> False!
# x = '' # ==> False!
# x = [] # ==> False!
# if x:
#     print('True!')
# else:
#     print('False!')

# 值为数字(0)，空串('')，空list([])时，结果都是False




# ========== input
# numstr = input('num: ')
# num = int(numstr)
# # print(numstr, num)
# print(num > 14)

# input输入的数据类型是str，不能直接拿来和数字比较，需先把str转换成数字，Python中使用int()函数进行转换

# int()转换不是数字字符串会报错
# str = input('str:')
# print(int(str))