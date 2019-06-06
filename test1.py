import random

bufangjia = 0
fangjia = 0
for i in range(1, 10000):
    n = random.random()
    print(n)
    if n < 0.5:
        fangjia += n
    else:
        bufangjia += n


print("fangjia:", fangjia)
print("bufangjia:", bufangjia)
