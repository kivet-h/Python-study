"""
    模式匹配
"""

# ========== match 语句
# 1. 基础用法
# 类似于JS的Switch语句

# score = 'B'
# match score:
#     case 'A':
#         print('A')
#     case 'B':
#         print('B')
#     case 'C':
#         print('C')
#     case _:
#         print('其它')

# 2. 复杂匹配
# match 语句除了可以匹配简单的单个值之外，还可以匹配多个值、匹配一定范围，并且还能把匹配到的值绑定到变量。
# age = 16
# match age:
#     case x if x < 10:
#         print(f'年龄小于10岁，年龄为: {x}')
#     case 10:
#         print('年龄为10岁')
#     case 11 | 12 | 13 | 14 | 15:
#         print('年龄为11-15岁')
#     case _:
#         print('年龄大于15岁')

# - 匹配多个值
# 使用 | 分隔即可

# - 匹配一定范围，并且还能把匹配到的值绑定到变量
# 如上面：case x if x < 10
# 表示当age < 10时匹配成功，并且将值赋值给变量x，在所匹配的代码块中被使用。

# 3. 匹配列表
# match 功能是十分强大的，还可以匹配列表

# args = ['gcc', 'hello.c', 'world.c', 'AAA']
# # args = ['gcc']
#
# match args:
#     case ['gcc']:
#         print('列表中仅存在gcc')
#     case ['gcc', file1, *files]:
#         print(file1) # ==> hello.c
#         print(files) # ==> ['world.c', 'AAA']
#         print('gcc ' + file1 + ' | ' + ','.join(files)) # ==> gcc hello.c | world.c,AAA
#     case _:
#         print('其它')


# case ['gcc']:
    # 列表中仅存在gcc一个元素时匹配
# ['gcc', file1, *files]：
    # 列表第一个元素时gcc，第二个元素绑定到变量file1，之后所有的元素按列表的形式绑定到变量files（*号的作用在函数参数中有涉及）
    # 此case实际上表示至少指定一个文件