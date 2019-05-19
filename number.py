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
print(math.ceil(x))  # 向上取整 -10

# 2.数字比较大小
# print(math.cmp(10, 20))  # 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1 ,python3无法使用
a = 1
b = 2
print(operator.lt(a, b))  # a < b 结果:True
print(operator.lt(a, b))  # a < b 结果:True
print(operator.lt(a, b))  # a < b 结果:True
print(operator.lt(a, b))  # a < b 结果:True
print(operator.lt(a, b))  # a < b 结果:True

print(math.exp(1))  # 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
print(math.exp(1))  # 绝对值
print(math.exp(1))  # 绝对值
print(math.exp(1))  # 绝对值
