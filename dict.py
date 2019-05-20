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
# 3.删除字典元素

# 3.删除字典元素

# 3.删除字典元素
