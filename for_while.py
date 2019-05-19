# while 循环


# for 循环

for letter in 'Python':
    print('当前字母 :', letter)

# 序列索引迭代 range(length),包左不包右
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):  # 函数 len() 返回列表的长度
    print('当前水果 :', fruits[index])

# 嵌套循环 while循环体中嵌套for循环
'''
    以下实例使用了嵌套循环输出2~100之间的素数
'''
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print(i, " 是素数")
    i = i + 1

print("Good bye!")

'''
实例一：使用循环嵌套来获取100以内的质数
'''
num = [];
i = 2
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        num.append(i)
print(num)

'''
实例二：使用嵌套循环实现×字塔的实现 
'''
# *字塔
i = 1
# j=1
while i <= 9:
    if i <= 5:
        print("*" * i)

    elif i <= 9:
        j = i - 2 * (i - 5)
        print("*" * j)
    i += 1
else:
    print("")

# break 语句  ;continue 语句  ;pass 语句
'''
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句。
'''
# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)
print("Good bye!")

# 打印质数
for num in range(10, 20):  # 迭代 10 到 20 之间的数字,包左不包右
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))  # 10 等于 2 * 5
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print(num, '是一个质数')

# 打印1-9三角形阵列：
for i in range(1, 11):
    for k in range(1, i):
        print(k, end=" ")  # print是一个函数,不换行
    print("\n")

# 打印空心等边三角形
# rows = int(raw_input('输入行数：'))  #Python3中用input()取代了raw_input()，
rows = int(input('输入行数：'))
for i in range(0, rows):
    for k in range(0, 2 * rows - 1):
        if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
            print(" * ", end=" ")
        elif i == rows - 1:
            if k % 2 == 0:
                print(" * ", end=" ")
            else:
                print("   ", end=" ")
        else:
            print("   ", end=" ")
    print("\n")
