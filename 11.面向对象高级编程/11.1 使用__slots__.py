"""
    使用__slots__
"""
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。

# # 先定义class：
# class Student(object):
#     pass
#
# # 然后，尝试给实例绑定一个属性：
# s = Student()
# # 动态给实例绑定一个属性
# s.name = 'Michael'
# print(s.name) # ==> Michael
#
# # 还可以尝试给实例绑定一个方法：
# # 定义一个函数作为实例方法
# def set_age(self, age):
#     self.age = age
#
# from types import MethodType
# s.set_age = MethodType(set_age, s)
# s.set_age(25)
# print(s.age) # ==> 25
#
# # 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# s2 = Student()
# # s2.set_age(25) # ==> 报错：AttributeError: 'Student' object has no attribute 'set_age'
#
#
# # 为了给所有实例都绑定方法，可以给class绑定方法：
# def set_score(self, score):
#      self.score = score
#
# Student.set_score = set_score
#
# # 给class绑定方法后，所有实例均可调用：
# s.set_score(100)
# s2.set_score(99)
# print(s.score, s2.score) # ==> 100 99

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。








# ================================================== 使用__slots__ ==================================================
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

# class Student(object):
#     __slots__ = ('name', 'age')

# 然后，再试试：
# s = Student() # 创建新的实例
# s.name = 'Michael' # 绑定属性'name'
# s.age = 25 # 绑定属性'age'
# # s.score = 99 # 绑定属性'score'
# ==> 设置score时报错：
# Traceback (most recent call last):
#   File "D:\web\python-study-ljf\11.面向对象高级编程\11.1 使用__slots__.py", line 63, in <module>
#     s.score = 99 # 绑定属性'score'
#     ^^^^^^^
# AttributeError: 'Student' object has no attribute 'score' and no __dict__ for setting new attributes

# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。




# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# class GraduateStudent(Student):
#     pass
#
# g = GraduateStudent()
# g.score = 99
# print(g.score) # ==> 99

# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。





# 作用范围：
# (情况1) 父类没定义__slots__, 而子类也未定义: 子类的实例属性 -> 无限制
# (情况2) 父类定义了__slots__, 而子类并未定义: 子类的实例属性 -> 无限制、
# class Student(object):
#     __slots__ = ('name')
#
#     def __init__(self, name):
#         self.name = name
#
# class Classmate(Student):
#     pass
#
# A = Classmate('A')
# A.gender = 'female'
# print(f'{A.gender = }')  # -> A.gender = 'female'


# (情况3) 父类未定义__slots__, 而子类定义了: 子类的实例属性 -> 无限制
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
# class Classmate(Student):
#     __slots__ = ('name')
#     pass
#
# A = Classmate('A')
# A.gender = 'female'
# print(f'{A.gender = }')  # -> A.gender = 'female'


# (情况4) 父类定义了__slots__, 且子类也定义了: 子类的实例属性 -> 限制为二者的并集
# class Student(object):
#     __slots__ = ('name')
#     def __init__(self, name):
#         self.name = name
#
# class Classmate(Student):
#     __slots__ = ('age')
#     pass
#
# A = Classmate('A')
# A.gender = 'female'
# print(f'{A.gender = }') # ==> 报错：AttributeError: 'Classmate' object has no attribute 'gender' and no __dict__ for setting new attributes

# 综上所述, 可以简化记忆为:
# - 在__slots__未定义的时候, 将其当作: "__slots__ = 无限可能"
# - 始终遵循的原则是: "子类和父类的 __slots__ 的并集"


