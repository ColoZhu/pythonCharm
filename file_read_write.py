# 读写文件


'''
调用 open() 函数，打开一个 File 文件对象。
调用 File 的 read() 或 write() 方法进行读取与写入操作。
调用 File 的 close() 方法，关闭文件。
要进行完整的读写操作，以上三个步骤缺一不可。
open() 函数可接受两个参数:
open(para1, para2)其中,para2可以为：
为空，则默认采取读模式打开文件。
‘r’：读模式，即只能读取文件，无法修改。
‘w’：写模式，即可以向文件中添加文本内容，会覆盖文件原有内容。
‘a’：添加模式，即在原有内容末尾添加文本内容。
当 open() 函数打开的文件不存在时，写模式和添加模式都会创建一个新的空文件。
每次读取或写入文件后，必须调用 close() 方法将其关闭，才能在此打开该文件。
'''
# 文件路径
filePath = 'I:\\pythonWorkPace\\py3.txt'

# 打开文件
# lineFile = open(filePath, 'r')
lineFile = open(filePath, 'r', encoding='utf-8')  # 这里必须事先知道文件编码格式(防止中文乱码)

# 读成行<list>
lineContent = lineFile.readlines()

# 原文读
# readContent = lineFile.read()

# 输出内容
print(lineContent)

# 输出内容
# print(readContent)

# 关闭文件
lineFile.close()
