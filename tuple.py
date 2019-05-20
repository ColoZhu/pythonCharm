# Python3 元组

'''
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
'''
tup1 = ('Google', 'Runoob', 1997, 2000);
tup2 = (1, 2, 3, 4, 5);
tup3 = (50)  # 不加逗号，类型为整型
tup4 = (50,)  # 加上逗号，类型为元组

# 1.访问元组 (下标索引)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 2.连接组合
tup11 = (12, 34.56);
tup12 = ('abc', 'xyz')
# 创建一个新的元组
tup13 = tup11 + tup12;
print(tup13)  # (12, 34.56, 'abc', 'xyz')

# 3.删除元组 (元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组)
tup21 = ('Google', 'Runoob', 1997, 2000)

print(tup21)
del tup21;
print("删除后的元组 tup21 : ")
# print(tup21)   #NameError: name 'tup' is not defined

# 5.元组运算符 (和list类似)
'''

Python 表达式	        结果	                        描述
len((1, 2, 3))	        3	                            计算元素个数
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	            连接
('Hi!',) * 4	        ('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
3 in (1, 2, 3)      	True	                        元素是否存在
for x in (1, 2, 3): print (x,)	1 2 3	                迭代

'''
tuple74 = ('Hi!',) * 4  # 复制
print(tuple74)

# 6.元组索引，截取
L = ('Google', 'Taobao', 'Runoob')
print(L[2])  # -->'Runoob'
print(L[-2])  # -->'Taobao'
print(L[1:])  # -->('Taobao', 'Runoob')

# 7.元组内置函数
tuple7 = ('Google', 'Runoob', 'Taobao')
print("计算元组元素个数", len(tuple7))

tuple72 = ('5', '4', '8')
print("返回元组中元素最大值", max(tuple72))
print("返回元组中元素最小值", min(tuple72))

# 将列表转换为元组
list73 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple73 = tuple(list73)
print(tuple73)
