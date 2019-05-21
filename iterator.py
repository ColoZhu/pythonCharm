# Python3 迭代器与生成器
import sys

'''

迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。(迭代器只能往前不会后退)。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：

'''
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
print(next(it))

list2 = [1, 2, 3, 4]
it2 = iter(list2)
for x in it2:
    print(x, end=" ")  # 1 2 3 4

# 引入 sys 模块
list3 = [1, 2, 3, 4]
it3 = iter(list3)  # 创建迭代器对象
print()
while True:
    try:
        print(next(it3))
    except StopIteration:
        sys.exit()
