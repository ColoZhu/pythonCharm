import random

import math
import operator

# 数字
#
# 1. Python math 模块、cmath 模块
'''
Python math 模块、cmath 模块
Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。
Python math 模块提供了许多对浮点数的数学运算函数。
Python cmath 模块包含了一些用于复数运算的函数。
cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。
要使用 math 或 cmath 函数必须先导入
'''

x = -10.2

print(abs(x))  # 绝对值
print(round(4.5))  # 四舍五入

print(math.ceil(x))  # 向上取整 -10
print(math.exp(1))  # 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045

print(math.floor(1.5))  # 向下取整
print(math.log(100, 10))  # 2.0
print(math.log(math.e))  # 1.0
print(math.log10(1000))  # 3.0
print(max(1, 2, 3, 6))  # 最大值

list = [1, 2, 3, 5, 70]
print(max(list))  # 最大值
print(math.modf(3.1415))  #
print(math.pow(3, 2))  # x**y 运算后的值
print(round(3.2))  # 返回浮点数x的四舍五入值。
print(math.sqrt(36))  # 返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j

# Python随机数函数random
print("从 range(100) 返回一个随机数 : ", random.choice(range(100)))
print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))
# 从 1-100 中选取一个奇数
print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
# 从 0-99 选取一个随机数
print("randrange(100) : ", random.randrange(100))  # [start,] stop [,step]  从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
# 第一个随机数
print("[0-1)随机生成一个数字random() : ", random.random())

list2 = [20, 16, 10, 5];
random.shuffle(list2)
print("随机排序列表 : ", list2)  # 将序列的所有元素随机排序
# print(random.uniform(1, 6))  # 随机生成下一个实数，它在[x,y]范围内。
print("uniform(5, 10) 的随机浮点数 : ", random.uniform(5, 10))

# 3.Python三角函数


# 4.数字比较大小operator
# print(math.cmp(10, 20))  # 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1 ,python3无法使用
a = 1
b = 2
print(operator.lt(a, b))  # a < b 结果:True
print(operator.le(a, b))  # a <= b 结果:
print(operator.eq(a, b))  # a == b 结果:
print(operator.ne(a, b))  # a != b 结果:
print(operator.gt(a, b))  # a > b 结果:
print(operator.ge(a, b))  # a >= b 结果:
