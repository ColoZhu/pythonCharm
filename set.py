# Python3 集合
a = 1
'''
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

'''
# 1.创建  set1 ={value01,value02,...}  或者set1 =  set(value)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("basket:", basket)  # -->{'banana', 'pear', 'orange', 'apple'}   排序改变

fruit = set(('orange', 'banana', 'pear', 'apple'))  # -->{'pear', 'banana', 'orange', 'apple'}
print("fruit:", fruit)

# 2.下面展示两个集合间的运算.
a = set('123456')
b = set('345678')
print("a :", a)
print("b :", b)

print("a - b :", a - b)  # 集合a中包含而集合b中不包含的元素  -->  {'2', '1'}
print("a | b :", a | b)  # 集合a或b中包含的所有元素  -->  {'4', '6', '1', '7', '3', '8', '2', '5'}
print("a & b :", a & b)  # 集合a和b中都包含了的元素  -->  {'5', '4', '6', '3'}
print("a ^ b :", a ^ b)  # 不同时包含于a和b的元素  -->  {'8', '1', '2', '7'}

# 3.集合推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print("a:", a)  # -->{'r', 'd'}

# 4.添加元素  格式 :s.add( x )
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print("thisset:", thisset)  # {'Facebook', 'Taobao', 'Google', 'Runoob'}
# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：s.update( x ) x 可以有多个，用逗号分开。
thisset.update({1, 3})  # thisset: {'Google', 'Facebook', 1, 3, 'Taobao', 'Runoob'}
print("thisset:", thisset)
thisset.update((5, 7, 1))  # 重复元素只会出现一次 set
print("thisset:", thisset)  # thisset: {1, 'Runoob', 3, 'Taobao', 'Google', 5, 7, 'Facebook'}

# 5.移除元素  格式 :s.remove( x )
# ①将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误
thisset.remove("Taobao")
print("thisset:", thisset)
# thisset.remove("Taobao")  #KeyError: 'Taobao'
# ②此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示： s.discard( x )
thisset.discard("Facebook")  # 不存在不会发生错误
print("thisset:", thisset)
print("thisset:", thisset)  # -->{1, 3, 5, 7, 'Runoob', 'Google'}
# ③随机删除集合中的一个元素  s.pop()
x = thisset.pop()
print("pop:", x)  # -->{3, 5, 7, 'Runoob', 'Google'}
# 然而在交互模式，pop 是删除集合的第一个元素（排序后的集合的第一个元素）

# 6.计算集合元素个数  len(set)
print("len:", len(thisset))  # -->5

# 7.清空集合   s.clear()
thisset.clear()
print("thisset.clear:", thisset)  # --> set()

# 8.判断元素是否在集合中存在   x in s
thisset8 = set(("Google", "Runoob", "Taobao"))
print("'Runoob' in thisset:", "Runoob" in thisset8)  # -->True

# 9.集合内置方法完整列表
'''
方法	        描述
add()	        为集合添加元素
clear()	        移除集合中的所有元素
copy()	        拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	    删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	删除集合中的元素，该元素在指定的集合中不存在。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	    判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	        随机移除元素
remove()	    移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	        返回两个集合的并集
update()	    给集合添加元素

'''

x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.union(y)

print(z)  # {'apple', 'cherry', 'banana', 'google', 'runoob'}
