"""
    函数的参数
"""

# Python的函数定义非常简单，但灵活度却非常大。
# 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# 1. 位置参数
# 计算任意数值的n次方：power(x, n)函数
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
# print(power(2, 3)) # ==> 8

# 上面函数x和n两个参数，都是位置参数，调用函数时，需要按照顺序依次传值给x和n两个参数赋值



# 2. 默认参数
# def power(x, n = 2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
# print(power(2)) # ==> 4

# 设置默认参数时，需要注意：必须参数必须在默认参数之前

# 多个默认参数
# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
#
# enroll('Bob', 'M', 7)
# enroll('Adam', 'M', city='Tianjin') # 可直接跳过age对city直接赋值

# 注意：默认参数必须指向不变对象！

# def add_end(L = []):
#     L.append('END')
#     return L
#
# # 正常使用时
# print(add_end([1, 2, 3])) # ==> [1, 2, 3, 'END']
# print(add_end(['x', 'y', 'z'])) # ==> ['x', 'y', 'z', 'END']
#
# # 使用默认参数时
# print(add_end()) # ==> ['END']
#
# # 但是再次执行时
# print(add_end()) # ==> ['END', 'END']

# 解释：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]。
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，下一次的默认参数的内容就变了，不再是函数一开始定义时的[]了。
# 相当于第一次调用后，默认参数从[]变成了['END']

# 上面问题可以怎么优化？
# def add_end(L = None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# print(add_end()) # ==> ['END']
# print(add_end()) # ==> ['END']

# 为什么要设计str、None这样的不变对象呢？
# 因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


# 3. 可变参数
# 可变参数，即：传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

# 如计算一些数字相加
# 一种方案是使用传入list和tuple的方式
# def num_sum(list):
#     result = 0
#     for num in list:
#         result = result + num
#     return result
#
# print(num_sum([1, 2, 3])) # ==> 6
#
# # 可变参数的写法
# def num_sum(*nums):
#     result = 0
#     for num in nums:
#         result = result + num
#     return result
# print(num_sum(1, 2, 3)) # ==> 6

# def num_sum(*nums):
#     print(nums) # ==> (1, 2, 3)
# num_sum(1, 2, 3)
# 打印可变参数可以看到，实际上可变参数接收到的是一个tuple。
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
# def num_sum(*nums):
#     result = 0
#     for num in nums:
#         result = result + num
#     return result
# numsList = [1, 2, 3, 4]
# print(num_sum(*numsList)) # ==> 10
# *numsList表示把numsList这个list的所有元素作为可变参数传进去。


# 4. 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# def person(name, **kw):
#     print('name:', name, 'other:', kw)
#
# person('kivet') # ==> name: kivet other: {}
# person('kivet', age = 18, address = '四川省成都市') # ==> name: kivet other: {'age': 18, 'address': '四川省成都市'}

# 关键字参数有什么用？
# 它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name这一个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。
# 比如说，你正在做一个用户注册的功能，除了用户名是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

# 同理，Python允许你在dict前面加两个**号，把dict的元素变成关键字参数传进去
# def person(name, **kw):
#     print('name:', name, 'other:', kw)
#
# extra = {'age': 18, 'address': '四川省成都市'}
# person('kivet', **extra) # ==> name: kivet other: {'age': 18, 'address': '四川省成都市'}

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict。
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


# 5. 命名关键字参数
# def person(name, **kw):
#     if 'age' in kw:
#         # 有age参数
#         pass
#     if 'address' in kw:
#         # 有address参数
#         pass
#     print('name:', name, 'other:', kw)
# # 以以上函数为例，除了name这个位置参数，我们想检查关键字参数kw中是否有age和address两个参数
# # 但是调用者仍然可以传入其它不收限制的参数
# person('kivet', age = 18, address = '四川', iphone = '110120119') # ==> name: kivet other: {'age': 18, 'address': '四川', 'iphone': '110120119'}

# 如果要限制关键字参数的名字，就可以用命名关键字参数，
# 例如，只接收age和address作为关键字参数。这种方式定义的函数如下：
# def person(name, *, age, address):
#     print(name, age, address) # ==》 kivet 18 四川
# person('kivet', age = 18, address='四川')

# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
# def person(name, *args, city, job):
#     print(name, args, city, job)
# person('kivet', 1,2,3, city='成都', job='web') # ==> kivet (1, 2, 3) 成都 web

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错，如：
# person('kivet', 1,2,3, '成都', 'web') # 报错
# 报错原因：由于调用时缺少参数名city和job，Python解释器把第一个参数视为位置参数，后所有参数都传给乐*args，但缺少命名关键字参数导致报错。

# 命名关键字参数也可以有默认值
# def person(name, *args, city = '成都', job = 'web'):
#     print(name, args, city, job)
# person('kivet', 1,2,3, '成都', 'web') # ==> kivet (1, 2, 3, '成都', 'web') 成都 web

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
# def person(name, age, city, job):
#     # 缺少 *，city和job被视为位置参数
#     pass


# 6. 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是需要注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 不再赘述，下面记录一些打印输出参考
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# >>> f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
# >>> f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
# >>> f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
# >>> f1(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
# 通过一个tuple和dict，你也可以调用上述函数
# >>> args = (1, 2, 3, 4)
# >>> kw = {'d': 99, 'x': '#'}
# >>> f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# >>> f2(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
# 通过一个tuple和dict，你也可以调用上述函数
# >>> args = (1, 2, 3)
# >>> kw = {'d': 88, 'x': '#'}
# >>> f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

