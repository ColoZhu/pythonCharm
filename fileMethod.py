import osTest

# file 对象
'''
file.close()
关闭文件。关闭后文件不能再进行读写操作。
file.flush()
刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
file.fileno()
返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
file.isatty()
如果文件连接到一个终端设备返回 True，否则返回 False。
file.next()
Python 3 中的 File 对象不支持 next() 方法。
返回文件下一行。
file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。
file.readline([size])
读取整行，包括 "\n" 字符。
file.readlines([sizeint])
读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
file.seek(offset[, whence])
设置文件当前位置
file.tell()
返回文件当前位置。
file.truncate([size])
从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。
file.write(str)
将字符串写入文件，返回的是写入的字符长度。
file.writelines(sequence)
向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

'''

# 1.tell()
fileTestPath = "D:\\pythonWorkspace\\pythonCharm\\fileTest3";
fo = open(fileTestPath, "r+")  # 打开一个文件用于读写。文件指针将会放在文件的开头。

print("文件名为: ", fo.name)

line = fo.readline()
print("读取的数据为: %s" % (line))  # --> 读取的数据为: 123123

# 获取当前文件位置
pos = fo.tell()
print("当前位置: %d" % (pos))  # -->当前位置: 8

# 关闭文件
fo.close()

# 2.next() ,测试到结尾会报错
'''
Python 3 的内置函数 next() 通过迭代器调用 __next__() 方法返回下一项。 在循环中，next()方法会在每次循环中调用，该方法返回文件的下一行，如果到达结尾(EOF),则触发 StopIteration

'''
fo = open(fileTestPath, "r")  # 只读方式
for index in range(5):
    line = next(fo)
    print("第 %d 行 - %s" % (index, line))

# 关闭文件
fo.close()
