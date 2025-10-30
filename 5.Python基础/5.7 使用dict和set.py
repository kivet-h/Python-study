"""
    使用dict和set
"""

# ================================================== dict（字典） ==================================================
# 类似与JS中的对象。
# dict，全称dictionary，在其它语言中称之为map，使用键-值（key-value）存储，具有极快的查找速度。
# Python内置了字典

# 取值
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael']) # ==> 95


# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
# d = { 'Michael': 95, 'Bob': 75, 'Tracy': 85 }
# d['Adam'] = 67
# print(d['Adam']) # ==> 67


# 一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
# d = { 'Michael': 95, 'Bob': 75, 'Tracy': 85 }
# d['Adam'] = 67
# d['Adam'] = 88
# print(d['Adam']) # ==> 88


# 如果key不存在，dict就会报错
# d = { 'Michael': 95 }
# print(d['Michael1']) # ==> KeyError: 'Michael1'


# 判断key是否存在
# d = { 'Michael': 95 }
# print('Michael' in d) # ==> True
# print('Michael1' in d) # ==> False


# get()方法
d = { 'Michael': 95 }
# print(d.get('Michael')) # ==> 95
# print(d['Michael']) # ==> 95

# # 与直接取值不同，get()取不到值的时候，默认返回None。而直接取值取不到就会报错
# print(d.get('Michael1')) # ==> None
# print(d['Michael1']) # ==> KeyError: 'Michael1'

# 同时get()也可以自己指定返回的内容
# print(d.get('Michael1'), 'value is None!') # ==> value is None!


# 删除key，使用pop(key)方法
# d = { 'Michael': 95, 'Bob': 75, 'Tracy': 85 }
# d.pop('Bob')
# print(d) # ==> {'Michael': 95, 'Tracy': 85}

# 注意：dict内部存放的顺序和key放入的顺序是没有关系的


# 与list相比，dict有以下特点：
# a. 查询和插入的速度极快，不会随着key的增加而变慢
# b. 需要占用大量的内存，内存浪费较多
# 即，dict是典型的空间换时间的一种方法。


# 正确使用dict非常重要，需要牢记的第一条就是：dict的key必须是不可变对象。
# 为什么？
# 因为dict需要根据key来计算value的存储位置，如果每次计算相同的key得到的结果不一样，那dict内部就完全混乱了。
# 这里说的通过key计算存储位置的算法是用的哈希算法（Hash）
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
# 而如list是可变的，就不能作为key



# ================================================== set ==================================================
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

# 1.创建set
# a.直接定义
# s = { 1, 2, 'a', 'b' }
# print(s) # ==> {1, 2, 'a', 'b'}

# b.提供一个list作为输入集合
# s = set([1, 2, 'a', 'b'])
# print(s) # ==> {1, 2, 'a', 'b'}

# 重复元素在set中会自动被过滤
# s = {1, 1, 2, 2, 3, 3}
# print(s) # ==> {1, 2, 3}



# 2. 添加元素
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
# s = { 2, 'b' }
# s.add(1)
# s.add('a')
# s.add('a')
# print(s) # ==> {1, 2, 'a', 'b'} # 可以看出，添加是无序的



# 3. 删除元素
# 通过remove(key)方法可以删除元素
# s = {'a', 'b', 2, 1}
# s.remove(2)
# print(s) # ==> {1, 'a', 'b'}

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# print(s1 & s2) # ==> 交集：{2, 3}
# print(s1 | s2) # ==> 并集：{1, 2, 3, 4}

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样.
# 所以，一样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
# 如果试着把list放入set，会报错提醒。

