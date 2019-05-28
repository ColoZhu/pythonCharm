# 模块
'''
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，
以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
'''
import sys

print("命令行参数如下:")
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')  # sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表


def print_func(par):
    print("Hello : ", par)
    return


'''
一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
    当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢？
    这就涉及到Python的----搜索路径--- ，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块。
    这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。
    搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量，
'''

# from … import 语句
'''
    
    Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
    from modname import name1[, name2[, ... nameN]]

'''
from fibo import fib, fib2
# 这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。

from fibo import *

# 可以一次性的把模块中的所有（函数，变量）名称都导入到当前模块的字符表:


# __name__属性
'''
    一个模块被另一个程序第一次引入时，其主程序将运行。
    如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
    说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
    说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格。
'''

import using_name
# -->我来自另一模块


# dir() 函数
import fibo, sys

print(" dir(fibo)")
s = dir(fibo)
print(
    s)  # fibo 中定义的 --> ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']

import fibo

fib = fibo.fib
print(" ---")
print(dir())  # 那么 dir() 函数会罗列出当前定义的所有名称
# --> ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2', 'fibo', 'i', 'print_func', 's', 'sys', 'using_name']


a = 5  # 建立一个新的变量
print(" ---")
print(dir())  # a 也会加入到
# --> ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'fib', 'fib2', 'fibo', 'i', 'print_func', 's', 'sys', 'using_name']


# 标准模块
'''  
Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。
有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没问题。
这些组件会根据不同的操作系统进行不同形式的配置，比如 winreg 这个模块就只会提供给 Windows 系统。
应该注意到这有一个特别的模块 sys ，它内置在每一个 Python 解析器中。变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串

'''

# sys.ps1 = 'C> '
#
# C > print('Runoob!')
#
# Runoob!
# C >

# 包
# 用户可以每次只导入一个包里面的特定模块，比如
import sound.effects.echo
# 还有一种导入子模块的方法是:
from sound.effects import echo
# 还有一种变化就是直接导入一个函数或者变量

from sound.effects.echo import echofilter

# 从一个包中导入
from sound.effects import *
