# Python3 字典
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

# 1.访问字典里的值 ,字典中没有key会报错
print(dict['Alice'])  # 2341

# 2.修改字典
print("修改之前:", dict['Beth'])
dict['Beth'] = '哈哈哈哈哈'
print("修改之后:", dict['Beth'])

# 3.删除字典元素
dict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del dict3['Name']  # 删除键 'Name'
print("dict3['Name']:", dict3)  # -->{'Age': 7, 'Class': 'First'}
dict3.clear()  # 清空字典
print("clear:", dict3)  # --> {}
del dict3  # 删除字典
# print("del:", dict3)  #报错
# 4.字典键的特性
'''
字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。

'''
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print("dict['Name']: ", dict['Name'])  # -->Manni
# 2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行

# 4.内置函数

dict4 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(len(dict))  # 计算字典元素个数，即键的总数。
print(str(dict))  # 输出字典，以可打印的字符串表示。。
print(type(dict))  # 返回输入的变量类型  --><class 'dict'>

# 5.内置方法
dict5 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict5.clear()  # 删除字典内所有元素
print(dict5)

dict52 = dict5.copy()  # 返回一个字典的浅复制
print("copy后:", dict52)  # -->{}
dict5 = {'Name': 'Runoob1', 'Age': 71, 'Class': 'First1'}
print("被浅复制对象dict5改变后:", dict52)  # 浅复制是指当对象的字段值被复制时，字段引用的对象不会被复制 --> {}

#	radiansdict.fromkeys()
seq = ('name', 'age', 'sex')

dict53 = {'name': 'Runoob', 'age': 7, 'sex': 'First'}
# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
dict54 = dict53.fromkeys(seq)  # 第一个参数是seq,第二个参数是赋值
print("dict54:", dict54)  # -->dict54: {'name': None, 'age': None, 'sex': None}
dict55 = dict53.fromkeys(seq, 10)
print("dict55:", dict55)  # -->dict55: {'name': 10, 'age': 10, 'sex': 10}

# Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值
# radiansdict.get(key, default=None)
dict56 = {'Name': 'Runoob', 'Age': 27}
print("Age 值为 : %s" % dict.get('Age'))  # -->7
print("Sex 值为 : %s" % dict.get('Sex', "NA"))  # -->NA
print("Sex 值为 : %s" % dict.get('Sex'))  # -->None

# Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
dict57 = {'Name': 'Runoob', 'Age': 7}
print("Value : %s" % dict57.items())  # dict_items([('Name', 'Runoob'), ('Age', 7)])
# 遍历例子
for i, j in dict57.items():
    print(i, ":\t", j)
# 将字典的 key 和 value 组成一个新的列表：
d = {1: "a", 2: "b", 3: "c"}
result = []
for k, v in d.items():
    result.append(k)
    result.append(v)

print(result)  # [1, 'a', 2, 'b', 3, 'c']
