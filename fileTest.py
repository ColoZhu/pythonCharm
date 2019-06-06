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
# os.removedirs(fileTestPath2)  # 文件夹为空 ,会被删除
# os.removedirs(fileTestPath)  # 文件夹不为空,报错目录不是空的

# os.remove(path)  删除一个文件 3.txt
# os.remove(fileTestPath1)

# 删除指定空目录
# os.rmdir(fileTestPath3)

# Python创建目录文件夹
'''
主要涉及到三个函数
1、os.path.exists(path) 判断一个目录是否存在
2、os.makedirs(path) 多层创建目录
3、os.mkdir(path) 创建目录
'''


# 定义创建文件的函数
def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


# 调用函数创建
print(mkdir(fileTestPath))  # --> False,目录已存在

fileTestPath5 = "C:\\Users\\600336\\PycharmProjects\\hello\\testqwerty";
print(mkdir(fileTestPath5))  # -->True ,创建成功
