# 数据结构

a = "bbbbb"
b = "bbbbb"
c = a
print("a is  b:", a is b)  # True
print("c is  a:", c is a)  # True
a = "cccc"
print("a is  b:", a is b)  # False
print("c is  a:", c is a)  # False

s11 = "hello";
s1 = "hello";
s2 = "world";
s3 = "helloworld";
s4 = s1 + s2;
print("s11 is  s1:", s11 is s1)  #
print(id(s11))  #
print(id(s1))  #
print(id(s2))  #
print(id(s3))  #
print(id(s4))  #





# 字符串对象是不可以改变得,重新赋值会生成一个新的对象
