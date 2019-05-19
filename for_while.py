# while 循环


# for 循环

for letter in 'Python':
    print('当前字母 :', letter)

# 序列索引迭代 range(length),包左不包右
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):  # 函数 len() 返回列表的长度
    print('当前水果 :', fruits[index])

# 嵌套循环 while循环体中嵌套for循环


# break 语句  ;continue 语句  ;pass 语句


# 打印质数
for num in range(10, 20):  # 迭代 10 到 20 之间的数字,包左不包右
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))  #10 等于 2 * 5
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print(num, '是一个质数')
