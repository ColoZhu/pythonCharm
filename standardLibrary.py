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
sys.exit()


# 6.字符串正则匹配
