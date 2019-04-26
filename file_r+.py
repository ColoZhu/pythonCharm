import os

'''
w+每次打开文件，都会清空之前的内容，若文件不存在，则会自动创建
r+会在之前的基础上追加内容，但是不会创建文件
所以两个可以一起用，用之前判断一下文件是否存在，如下：
'''
# 文件路径
filePath = 'I:\\pythonWorkPace\\py3.txt'

# f = open(filePath, 'r+', encoding='utf-8')  # 必须事先知道文件的编码格式，这里文件编码是使用的utf-8
if os.path.exists(filePath):
    f = open(filePath, 'r+', encoding='utf-8')
else:
    f = open(filePath, 'w+', encoding='utf-8')
content = f.read()  # 如果open时使用的encoding和文件本身的encoding不一致的话，那么这里将将会产生错误
f.write('你想要写入的信息2222')
f.close()
