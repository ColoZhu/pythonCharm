# 幂运算


def pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2 == 0:
        return pow(x * x, n / 2)
    else:
        return pow(x * x, n / 2) * x


# 测试

#print(pow(20, 4))  #160000
print(pow(3, 5))
