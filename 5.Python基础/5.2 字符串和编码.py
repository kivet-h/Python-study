"""
    打印函数print()
"""

# 1. 字符编码
# 不赘述，参考：https://liaoxuefeng.com/books/python/basic/string-encoding/index.html

# 2. Python的字符串
# 见：https://liaoxuefeng.com/books/python/basic/string-encoding/index.html

# 3. 格式化
# 1. %
# print('hello %s, age: %002d, height: %f, 进制: %x' % ('world', 18, 170.2, 0xff00))
# print('%2d-%002d' % (3, 1))
# print('%.2f' % 3.145592)

# 4. format
# formatStr = 'hello {0}, 展示数字1.235但是保留两位小数{1:.2f}'
# print(formatStr.format('world', 1.235))

# 5. f-string
# a = 2.5
# b = a * 4 + 0.1234
# print(f'结果为：a: {a}, b: {b}, b保留两位：{b:.2f}')