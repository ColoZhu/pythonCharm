# python3标准库

# 1 . 操作系统接口
import os

print(os.getcwd())  # 返回当前的工作目录 -->D:\pythonWorkspace\pythonCharm

filepath = 'D:\\pythonWorkspace\\pythonCharm1'
# print(os.chdir(filepath))  # 修改当前的工作目录
os.system('mkdir today')  # 执行系统命令 mkdir,创建文件夹

print(dir(os))

# 2.日常的文件和目录管理任务 mod:shutil 模块提供了一个易于使用的高级接口:  shutil(模块,主要用于复制)

import shutil

shutil.copyfile('test/33', 'test/archive.db')  # 复制文件
# shutil.move('test/123213', 'installdir')  # 移动文件到目标位置并改名

# 3.文件通配符  glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:

import glob

print(glob.glob('*.py'))  # -->当前目录的.py文件列表,不包括子目录的

# 4.命令行参数
'''
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。
例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:

'''
import sys

print("sys.argv....")

print(sys.argv)  # ['D:/pythonWorkspace/pythonCharm/standardLibrary.py']

# 5.错误输出重定向和程序终止
'''sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息。
'''
sys.stderr.write('Warning, log file not found starting a new one\n')

# 程序终止
# sys.exit()

# 6.字符串正则匹配
'''
re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:

'''

import re

a = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')  # 匹配f开头的 字符串

print('a', a)  # -->['foot', 'fell', 'fastest']

b = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

print('b', b)  # -->  cat in the hat

c = 'tea for too'.replace('too', 'two')
print('c', c)  # tea for two

# 7.数学   ,math模块为浮点运算提供了对底层C函数库的访问:
import math

print(math.cos(math.pi / 4))  # --> 0.7071067811865476

print(math.log(1024, 2))  # --> 10.0

# random提供了生成随机数的工具。
import random

random.choice(['apple', 'pear', 'banana'])
list = random.sample(range(100), 10)
print('list', list)  # -->[46, 64, 58, 49, 93, 43, 27, 8, 42, 2]

print(random.randrange(6))  # -->1

# 8.访问 互联网
'''
有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:
'''

from urllib.request import urlopen

url = "http://tycho.usno.navy.mil/cgi-bin/timer.pl"
url1 = "https://www.baidu.com/"
url_yurongtong = "http://cfs-test.yupeiholdings.com:8083/cfs-qt/home.shtml"
for line in urlopen(url_yurongtong):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if 'EST' in line or 'EDT' in line:  # 查看东部时间
        print(line)

# import smtplib
import smtplib

# 本例 需要本地有一个在运行的邮件服务器。
# server = smtplib.SMTP('localhost')
#
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
#                 """To: jcaesar@example.org
#                  From: soothsayer@example.org
#                 Beware the Ides of March.
#                  """)
# server.quit()

# 9.日期和时间
'''
datetime模块为日期和时间处理同时提供了简单和复杂的方法。
支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
该模块还支持时区处理:
'''
from datetime import date, timedelta, time

now = date.today()  # 当天日期
print("now:", now)  # --> 2019-06-20

d1 = date(2003, 12, 2)  # 格式化日期
print("d1:", d1)  # --> 2003-12-02
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))  # 格式化
# -->06-20-19. 20 Jun 2019 is a Thursday on the 20 day of June.
# 支持计算
birthday = date(1992, 4, 4)
age = now - birthday
print('已经过了天数:', age.days)  # -->9938

# 10.数据压缩
# 以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
import zlib

s = b'witch which has which witches wrist watch'
print("s.length:", len(s))  # -->41

t = zlib.compress(s)  # 压缩
print("t.length:", len(t))  # -->37
b1 = zlib.decompress(t)  # 解压
print(b1)  # -->b'witch which has which witches wrist watch'
print("b1.length:", len(b1))  # -->41

# 11.性能度量
'''
有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。
例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多,timeit 证明了现代的方法更快一些。
相对于 timeit 的细粒度，:mod:profile 和 pstats 模块提供了针对更大代码块的时间度量工具。
'''
from timeit import Timer

time1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print("time1:", time1)  # 0.022810433999999935

time2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
print("time2:", time2)  # 0.020468804000000063

# 12.测试模块
'''
doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:
'''


def average(values):
    """Computes the arithmetic mean of a list of numbers."""

    # print(average([20, 30, 70]))
    return sum(values) / len(values)


import doctest

doctest.testmod()  # 自动验证嵌入测试

# import unittest
#
#
# class TestStatisticalFunctions(unittest.TestCase):
#
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         self.assertRaises(ZeroDivisionError, average, [])
#         self.assertRaises(TypeError, average, 20, 30, 70)
#
#
# unittest.main()  # Calling from the command line invokes all tests

# 13.关于urlopen的补充
# 处理get请求，不传data，则为get请求

from urllib.request import urlopen
from urllib.parse import urlencode

url = 'http://localhost:8085/yptms/login.shtml'
data = {"username": "admin", "password": "yupei123"}
req_data = urlencode(data)  # 将字典类型的请求数据转变为url编码
res = urlopen(url + '?' + req_data)  # 通过urlopen方法访问拼接好的url
res = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
print("res")
# print(res)

# 处理post请求,如果传了data，则为post请求

print("--------------------------------")
from urllib.request import Request
from urllib.parse import urlencode

data = {"username": "admin", "password": 123456}
data = urlencode(data)  # 将字典类型的请求数据转变为url编码
data = data.encode('ascii')  # 将url编码类型的请求数据转变为bytes类型
req_data = Request(url, data)  # 将url和请求数据处理为一个Request对象，供urlopen调用
with urlopen(req_data) as res:
    res = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

# print(res)


# 14.时间和日期补充
# 常用时间处理方法
import time
import datetime

today = date.today()  # 今天  -->  2019-06-21
print(today)
yesterday = today - timedelta(days=1)  # 昨天   -->    2019-06-20
print(yesterday)

last_month = today.month - 1 if today.month - 1 else 12
print(last_month)  # 上个月    -->    5

time_stamp = time.time()

print(time_stamp)  # 当前时间戳    -->  1561077887.9176207
print(int(time.time()))  # -->  1561077887

# 时间戳转datetime
d1 = datetime.datetime.fromtimestamp(time_stamp)  # 2019-06-21 08:47:37.636591
print(d1)

#  datetime转时间戳

dti = int(time.mktime(today.timetuple()))  # 1561046400
print("dti:", dti)

# datetime转字符串
today_str = today.strftime("%Y-%m-%d")
print("today_str:", today_str)

# 字符串转datetime
today = datetime.datetime.strptime(today_str, "%Y-%m-%d")  # --> 2019-06-21

print("today:", today)  # --> 2019-06-21 00:00:00

# 补时差
tadaySuper = today + datetime.timedelta(hours=8)  #-->2019-06-21 08:00:00
print("tadaySuper:", tadaySuper)
