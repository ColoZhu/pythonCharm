# -*- coding: UTF-8 -*-

print("你好，世界")

print('你好，世界' * 3)

for i in range(12):
    print(i)

if True:
    print("Answer")
    print("True")

else:
    print("Answer")
    print("False")

item_one = "1"
item_two = "2"
item_three = "3"

total = item_one + \
        item_two + \
        item_three
print("total:" + total)

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
paragraph = '''这是一个段落
包含了多个语句'''
paragraph2 = """这是一个段落 包含了多个语句2"""
print("paragraph:" + paragraph)
print("paragraph2:" + paragraph2)

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')

# 不换行输出
print (x,y)

