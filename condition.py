# 条件语句
num = 5
if num < 10:
    print("num<10")
elif num == 10:
    print("num==10")
else:
    print("num>10")

# 多条件判断
'''
    由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，
    如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；
    使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
'''
num1 = 9
if num1 >= 0 and num1 <= 10:  # 判断值是否在0~10之间
    print('num1 >= 0 and num1 <= 10')

num2 = 10
if num2 < 0 or num2 > 10:  # 判断值是否在小于0或大于10
    print('num2 < 0 or num2 > 10')
else:
    print('! (num2 < 0 or num2 > 10)')

'''
    当if有多个条件时可使用括号来区分判断的先后顺序，括号中的判断优先执行，
    此外 and 和 or 的优先级低于>（大于）、<（小于）等判断符号，
    即大于和小于在没有括号的情况下会比与或要优先判断。
'''
