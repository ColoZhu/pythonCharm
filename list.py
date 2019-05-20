# Python 列表(List)


list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

'''
Python包含6中内建的序列，即列表、元组、字符串、Unicode字符串、buffer对象和 xrange 对象。
序列通用的操作包括：索引、长度、组合（序列相加）、重复（乘法）、分片、检查成员、遍历、最小值和最大值。

序列都可以进行的操作包括索引，切片，加，乘，检查成员。
Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

'''
# 1.访问列表值(索引 或者 方括号内截取)
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# 2.Python列表脚本操作符
print("list3 长度: ", len(list3))  # 4
print("list相加 : ", list1 + list2)  # ['physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5]
print("list 重复: ", list2 * 4)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print("元素是否存在于列表中: ", 3 in list2)  # True
# 3.list迭代
print("list3迭代")
for x in list3:
    print(x, end=" ")

# 4.Python列表截取与拼接
L = ['Google', 'Runoob', 'Taobao']
print(L[2])  # 读取第三个元素 ->	'Taobao'
print(L[-2])  # 从右侧开始读取倒数第二个元素: count from the right ->Runoob
print(L[1:])  # 输出从第二个元素开始后的所有元素 ->['Runoob', 'Taobao']

# 5.嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print("x:", x)

# 6.Python列表函数&方法
'''
len(list) 列表元素个数
max(list) 返回列表元素最大值
min(list) 返回列表元素最小值
list(seq) 将元组转换为列表

list.append(obj)    在列表末尾添加新的对象
list.count(obj)     统计某个元素在列表中出现的次数
list.extend(seq)    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)     从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj) 将对象插入列表
list.pop([index=-1])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)    移除列表中某个值的第一个匹配项
list.reverse()      反向列表中元素
list.sort( key=None, reverse=False) 对原列表进行排序
list.clear()        清空列表
list.copy()         复制列表

'''
list = ['Google', 'Runoob', 'Taobao1']
print("list:", list)
list.append('hahaha')
print("append后list:", list)
list4 = [2, 2, 2, 4, 4, 4, 46, 66, 0, 1]
print("统计某个元素在列表中出现的次数:", list4.count(4))

list5 = [1, 2, 3, 4]
list6 = [0, 2, 3, 4]
list5.extend(list6)
print("用新列表扩展原来的列表:", list5)
list.sort()
print("list排序:", list)
# 降序
list.sort(reverse=True)
print("list降序:", list)
