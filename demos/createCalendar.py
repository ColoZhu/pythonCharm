''' 生成日历    '''

# 引入日历模块
import calendar

# 输入指定年月
# yy = int(input("输入年份: "))
# mm = int(input("输入月份: "))
yy = 2019
mm = 6
# 显示日历
print(calendar.month(yy, mm))

'''
Python 查找列表中最大元素
sort() 或者max()
'''
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("最大元素为:", list1[-1])  # 99
list1 = [10, 20, 1, 45, 99]
print("最大元素为:", max(list1))
