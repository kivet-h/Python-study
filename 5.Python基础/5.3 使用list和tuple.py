"""
    list和tuple
"""

# ================================================== list ==================================================
# 1. list打印、长度、取值
# arr = [1, 2, 3]
# print('打印：', arr, '长度：', len(arr)) # ==> 打印： [1, 2, 3] 长度： 3
# print(arr[1]) # ==> 2




# 2. 超出索引取值，会报错
# arr = [1, 2, 3]
# print(arr[3]) # ==> IndexError: list index out of range




# 3. 逆向取值
# arr = [1, 2, 3]
# print('倒数第一个值：', arr[len(arr) - 1]) # ==> 3
# print('倒数第一个值，也可以：', arr[-1]) # ==> 3
#
# print('倒数第二个值：', arr[-2]) # ==> 2
#
# print('同样超出索引范围会报错：', arr[-4]) # ==> IndexError: list index out of range




# 4. 追加值
# arr = [1, 2, 3]
# arr.append(4)
# print(arr) # ==> [1, 2, 3, 4]




# 5. 插入值
# 插入，是在指定下标前方进行插入
# arr = [1, 2, 4]
# arr.insert(2, 3) # 在下标为2的位置插入3
# print('在下标2前面插入', arr) # ==> 在下标2前面插入 [1, 2, 3, 4]




# 6. 删除默认元素
# a.可以使用pop()函数进行删除
# pop()函数不传参，则默认删除并返回list的最后一个元素
# arr = [1, 2, 3, 4]
# print('末尾元素：', arr.pop(), '，影响了原list：', arr) # ==> 末尾元素： 4 ，影响了原list： [1, 2, 3]

# pop()函数还可以传入对应下标，删除对应下标的元素
# arr = [1, 2, 3, 4]
# print('删除下标为0的元素，元素为：', arr.pop(0), '，影响了原list：', arr) # ==> 删除下标为0的元素，元素为： 1 ，影响了原list： [2, 3, 4]

# 注意：传入下标超过数组范围时，会报错
# arr = [1, 2, 3, 4]
# print(arr.pop(5)) # ==> IndexError: pop index out of range

# 注意：pop() 函数不能作用于空的list，无论是传了参数还是没传参数时，都会报错
# arr = []
# print(arr.pop()) # ==> IndexError: pop from empty list
# print(arr.pop(1)) # ==> IndexError: pop from empty list


# b.通过del的方式也能删除
# arr = [1, 2, 3, 4]
# del arr[2] # 通过del的方式删除
# print('通过del删除后的arr:', arr) # ==> 通过del删除后的arr: [1, 2, 4]



# 7. 替换
# arr = [1, 2, 3, 4]
# arr[1] = '22'
# print(arr)




# ================================================== tuple(元组) ==================================================
# 1. tuple是什么？
# 元组（tuple）和list十分类似，它也是一个有序列表。
# 但是tuple一但初始化，将不能修改，所以它没有append()、pop()、insert()等方法。
# 但是能获取元素，获取方式和list一样
# tupleArr = (1, 2, 3)
# print(tupleArr, tupleArr[1]) # ==> (1, 2, 3) 2



# 2. 不可变的tuple的意义？
# 由于不可变，所以代码会更安全。如果可能，尽量使用tuple代替list。




# 3. tuple陷阱
# 当tuple元素只有一个时，如t=(1)，这种写法定义的其实不是tuple，而是1这个数
# t=(1)
# print(t) # output:1
# 这是因为()既可以表示tuple，又可以表示数学公式里的小括号，这就产生了歧义。Python规定，这种情况下，是会按照小括号进行计算的，所以结果是1

# 注意，定义成空括号也算是tuple
# t = ()
# print(t) # ==> ()

# 如何定义只有一个元素的tuple？
# 在元素后面加个逗号，即可消除歧义
# t=(1,)
# print(t) # output:(1,)



# 4. "可变的"tuple
# 上面说的，tuple是不可变的，指的是它每个元素的指向是不可变的，但是指向的值，是可以被修改的
# tupleArr = (1, 2, ['A', 'B'])
# print(tupleArr) # ==> (1, 2, ['A', 'B'])
# tupleArr[2][0] = 'X'
# tupleArr[2][1] = 'Y'
# print(tupleArr) # ==> (1, 2, ['X', 'Y'])

# 从表面上看，tuple的元素确实是变了，但变的其实不是tuple的元素，而是list的元素。
# 改变前和改变后，tuple的指向都是list，所以tuple说的“不变”，指的是tuple的每一个元素，它的指向永远不变。