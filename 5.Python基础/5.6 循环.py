"""
    循环
"""

# python中的循环有两种

# 1. for...in循环
# 可以依次把list或tuple中的每一个元素迭代出来

# names = ['A', 'B', 'C']
# for name in names:
#     print(name)


# 求和
# sum1 = 0
# for n in [1,2,3,4,5,6,7,8,9,10]:
#     sum1 = sum1 + n
# print(sum1) # ==> 55

# 拓展：Python中，快速生成[0, ..., n]
# print(list(range(11))) # ==> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# range()：可以生成一个整数序列
    # print(range(5)) # ==> range(0, 5)
# list()：可以将整数序列转换成list

# for...in 也可以直接循环range()
# sum1 = 0
# for n in range(11):
#     sum1 = sum1 + n
# print(sum1) # ==> 55

# 2. while 循环
# sum2 = 0
# n = 1
# while n <= 10:
#     sum2 = sum2 + n
#     n = n + 1
# print(sum2) # ==> 55

# 3. break 提前结束循环
# n = 1
# while n < 10:
#     if n == 5:
#         break
#     print(n)
#     n = n + 1
# # 无if判断：依次打印1，2，...，9
# # 有if判断：依次打印1,2,3,4，结束循环。

# 4. continue 跳过当前循环，开始下一次循环
# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0:
#         continue
#     print(n)
# 依次打印出1,3,5,7,9