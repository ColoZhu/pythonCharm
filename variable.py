# 1.变量赋值
''''''
from builtins import complex, float, int

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
    • complex（复数） Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
'''

a1 = 9.322e-36j  # 复数
a2 = 5356336222298
a3 = -90.
a4 = 0xDEFABCECBDAECBFBAE
a5 = float()  # 定义一个浮点型
a5 = 2.333
a6 = long(111)  # long型,python3没有long型了
# a6 = 5356336222298

print(a1, a2, a3, a4, a5, a6)

# 7.Python字符串
'''
    python的字串列表有2种取值顺序:
    •从左到右索引默认0开始的，最大范围是字符串长度少1
    •从右到左索引默认-1开始的，最大范围是字符串开头

'''
s = "abcdef"
s1 = s[1:5]  # 取得一段子串的话，可以用到变量[头下标:尾下标]，包左不包右
print(s1)  # bcde
# 取单个字符
print(s[1])  # b
# 下标可以为空表示取到头或尾。
print(s[1:])  # bcdef
# 下标可以为负数
print("s4" + s[-1:3])  # 空
# 下标可以为负数
print("s5:" + s[-1:-3])  # 空
# 下标可以为负数
print("s6:" + s[-3:-1])  # de

# 加号（+）是字符串连接运算符，星号（*）是重复操作。如下实例：
str = 'Hello World!'
print (str)  # 输出完整字符串
print (str[0])  # 输出字符串中的第一个字符
print (str[2:5])  # 输出字符串中第三个至第五个之间的字符串
print (str[2:])  # 输出从第三个字符开始的字符串
print (str * 2)  # 输出字符串两次  Hello World!Hello World!
print (str + "TEST")  # 输出连接的字符串 Hello World!TEST

# 8.Python列表

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print (list)  # 输出完整列表
print (list[0])  # 输出列表的第一个元素   abcd
print (list[1:3])  # 输出第二个至第三个的元素  [786, 2.23]
print (list[2:])  # 输出从第三个开始至列表末尾的所有元素  [2.23, 'john', 70.2]
print (tinylist * 2)  # 输出列表两次  [123, 'john', 123, 'john']
print (list + tinylist)  # 打印组合的列表

# 9.Python元组
'''
    元组是另一个数据类型，类似于List（列表）。
    元组用"()"标识。内部元素用逗号隔开。但是元素不能二次赋值，相当于只读列表。
    元组是不允许更新的。而列表是允许更新的：
'''

tuple = ('abc', 123, 456, '元祖', 20.22)
tinytuple = (123, 'john')
print (tuple)  # 输出完整元组
print (tuple[0])  # 输出元组的第一个元素
print (tuple[1:3])  # 输出第二个至第三个的元素
print (tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2)  # 输出元组两次
print (tuple + tinytuple)  # 打印组合的元组

# 10.Python字典
'''
    字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。 
    两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。 
    字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print (dict['one'])  # 输出键为'one' 的值
print (dict[2])
# print (dict[3]) #如果没有3这个key会报错
print(tinydict)
print(tinydict.keys())  # 输出所有键  dict_keys(['name', 'code', 'dept'])
print(tinydict.values())  # 输出所有值  dict_values(['john', 6734, 'sales'])

# 11.Python数据类型转换
'''
    有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
    以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
    complex(real [,imag])   创建一个复数
    str(x)                  将对象 x 转换为字符串
    repr(x)                 将对象 x 转换为表达式字符串
    eval(str)               用来计算在字符串中的有效Python表达式,并返回一个对象
    tuple(s)                将序列 s 转换为一个元组
    list(s)                 将序列 s 转换为一个列表
    set(s)                  转换为可变集合
    dict(d)                 创建一个字典。d 必须是一个序列 (key,value)元组
    frozenset(s)            转换为不可变集合
    chr(x)                  将一个整数转换为一个字符
    unichr(x)               将一个整数转换为Unicode字符
    ord(x)                  将一个字符转换为它的整数值
    hex(x)                  将一个整数转换为一个十六进制字符串
    oct(x)                  将一个整数转换为一个八进制字符串
'''
x = 20.8
y = int(10)
x1 = int(x)  # 强转int
print(x1)  # 20
x2 = float(y)  # 强转float
print(x2)  # 10.0


