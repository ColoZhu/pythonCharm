import os

# os.makedirs('I:\\pythonWorkPace')  # 创建文件夹

path = 'I:\\pythonWorkPace'
filelist = os.listdir(path)  # 获取文件夹里面文件列表
print(filelist)
# 统计文件夹下面文件的所有文件大小
totalSize = 0;
for fileName in filelist:
    fileSize = os.path.getsize(os.path.join(path, fileName))
    print("当前文件的大小:%s" % (fileSize))
    totalSize = totalSize + os.path.getsize(os.path.join(path, fileName))
print("文件总大小:%s" % (totalSize))
