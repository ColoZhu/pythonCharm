# 文件路径
filePath = 'I:\\pythonWorkPace\\py3.txt'

f = open(filePath, 'w')
s = f.read()  # 读取文件内容,如果是不识别的encoding格式（识别的encoding类型跟使用的系统有关），这里将读取失败
'''假设文件保存时以gb2312编码保存'''
# u = s.decode('gb2312') #以文件保存格式对内容进行解码，获得unicode字符串
# u = s.decode('utf-8')
'''下面我们就可以对内容进行各种编码的转换了'''
print(s)
