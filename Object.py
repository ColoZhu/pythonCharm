# Python3 面向对象
a = 1
'''

类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：类中定义的函数。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
     例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

'''


# 1. 类定义
class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

# 2.  __init__()   ,类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用，
'''
self代表类的实例，而非类
'''


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)  # 类实例化时候会调用init方法,可以有参数,可以不带参数
print(x.r, x.i)  # 输出结果：3.0 -4.5

# 3. self
'''
从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
'''


class Test:
    def prt(self):
        print(self)  # <__main__.Test object at 0x00000000044D8A90>
        print(self.__class__)  # <class '__main__.Test'>


t = Test()
t.prt()


# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
class Test2:
    def prt2(runoob):
        print(runoob)
        print(runoob.__class__)


t2 = Test2()
t2.prt2()

# 4. 类属性与方法
'''
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。

self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。
'''


# 下面是私有变量测试
class JustCounter:
    __selectCount = 0  # 私有变量 ,两个下划线开头，声明该属性为私有
    publicCount = 0  # 公有变量

    def count(self):
        self.__selectCount += 1
        self.publicCount += 1
        print(self.__selectCount)


counter = JustCounter()  # 类的对象
counter.count()  # 1
counter.count()  # 2
print(counter.publicCount)  # 2
# print(counter.__secretCount)  # 报错，实例不能访问私有变量,只能在类的内部调用 ，不能在类的外部调用


# 下面是私有方法
