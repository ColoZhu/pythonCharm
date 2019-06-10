# Python3 错误和异常

while True:
    print('helloworld')
    break

# 除以0 异常
# 10 * (1 / 0)  # ZeroDivisionError: division by zero

#
while True:
    try:
        x = int(input("请输入一个数字"))
        break

    except ValueError:
        print("这不是一个数字,请再试一次!")

# try语句按照如下方式工作；
'''
首先，执行try子句（在关键字try和关键字except之间的语句）
如果没有异常发生，忽略except子句，try子句执行后结束。
如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如
'''

# 多个异常
import sys

existFile = "C:\\Users\\600336\\PycharmProjects\\hello\\test\\33";
try:
    # f = open('myfile.txt')
    f = open(existFile)

    s = f.readline()
    i = int(s.strip())
except OSError as  err:
    print("OS ERROR:{0}".format(err))  # 文件不存在,捕获这个异常
except ValueError:
    print("Could not convert data to an integer")
except:
    print("Unexpected error:", sys.exc_info()[0])  # 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出
    raise

# try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


# 定义除0函数
def this_fails():
    x = 1 / 0


# 测试除0函数
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)


# 抛出异常  Python 使用 raise 语句抛出一个指定的异常。
'''
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
'''


# try:
#     raise NameError('HiThere')  # 这个是定义的异常
# except NameError:
#     print('An exception flew by!')
#     raise  # 抛出上面的异常


# -->An exception flew by!   NameError: HiThere


# 用户自定义异常  你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承，例如:
# 自定义的异常类
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


# 测试自定义的异常
try:
    raise MyError(2 * 2)
except MyError as e:
    print('测试自定义的异常-My exception occurred, value:', e.value)  # -->测试自定义的异常-My exception occurred, value: 4


# 当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类:
# 大多数的异常的名字都以"Error"结尾，就跟标准的异常命名一样。
class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


# 定义清理行为(finally) ,try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。 例如:
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# 预定义的清理行为
