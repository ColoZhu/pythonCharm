# 1.变量赋值
''''''
from builtins import complex, float

from numpy import long

'''
Python中的变量不需要声明，变量的赋值操作既是变量声明和定义的过程。
每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
'''
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
print(counter, miles, name)

# 2.多个变量赋值
# Python允许你同时为多个变量赋值。例如：
a = b = c = 1
print(a, b, c)

# 您也可以为多个对象指定多个变量。例如：
a, b, c = 1, 2, "john"
print(a, b, c)

# 3.标准数据类型
'''
Python有五个标准的数据类型：
•Numbers（数字）
•String（字符串）
•List（列表）
•Tuple（元组）
•Dictionary（字典）

'''
# 4.Python数字
# 当你指定一个值时，Number对象就会被创建
var1 = 1
var2 = 10
var3 = 12
print(var1, var2)

# 5.del语句的语法是 del var1[,var2[,var3[....,varN]]]]
del var1
del var2, var3

# 6.Python支持四种不同的数值类型：
'''
    •int（有符号整型）
    •long（长整型[也可以代表八进制和十六进制]） 
    • float（浮点型） 
    • complex（复数）
'''

a1 = 9.322e-36j  #复数
a2 = 5356336222298

a3 = -90.
a4 = 0xDEFABCECBDAECBFBAE

a5 = float()  # 定义一个浮点型
a5 = 2.333

a6 = long(111)  #long型,python3没有long型了
# a6 = 5356336222298

print(a1, a2, a3, a4, a5, a6)
