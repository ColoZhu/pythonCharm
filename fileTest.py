import os, sys

'''
os.remove(path)
删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。

os.removedirs(path)
递归删除目录。

os.rmdir(path)
删除path指定的空目录，如果目录非空，则抛出一个OSError异常。

'''

# 打开文件
fileTestPath = "C:\\Users\\600336\\PycharmProjects\\hello\\test";
fileTestPath1 = "C:\\Users\\600336\\PycharmProjects\\hello\\test\\3";

fileTestPath2 = "C:\\Users\\600336\\PycharmProjects\\hello\\tmp";
fileTestPath3 = "C:\\Users\\600336\\PycharmProjects\\hello\\tmp";

# 删除文件夹和删除文件
# 列出目录
print("目录为: %s" % os.listdir(os.getcwd()))

# 移除 os.removedirs(path)  递归删除目录。
os.removedirs(fileTestPath2)  # 文件夹为空 ,会被删除
os.removedirs(fileTestPath)   # 文件夹不为空,报错目录不是空的

# os.remove(path)  删除一个文件 3.txt
os.remove(fileTestPath1)

# 删除指定空目录
os.rmdir(fileTestPath3)
