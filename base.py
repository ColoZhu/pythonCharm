# 编程基础
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b  # a, b = b, a+b 的计算方式为先计算右边表达式，然后同时赋值给左边，  b=a + b,然后a=b ,右边表达式的执行顺序是从左往右的。
''' 
    等价于 
    b_temp = b
    sum = a + b
    a = b_temp
    b = sum
'''

# 1. end 关键字
a1, b1 = 0, 1
while b1 < 1000:
    print(b1, end=',')
    a1, b1 = b1, a1 + b1
