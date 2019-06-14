# 欧几里得  求最大公约数

def gcd(m, n):
    while (n != 0):
        rem = m % n
        m = n
        n = rem

    return m;


# 测试

a = gcd(50, 15)
print(a)
