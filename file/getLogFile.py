#  提取重要的日志文件,根据关键字

# C:\Users\600336\Desktop\WMS—chem_log
# fp =open("e:\\data.log")
# fp =open("C:\\Users\\600336\\Desktop\\WMS—chem_log")
#
# for line in fp.readlines():  # 遍历每一行
#     filename = line[:14]  # 每行取前14个字母，作为下面新建文件的名称
#     content = line[14:]  # 每行取第15个字符后的所有字符，作为新建文件的内容
#
#     with open("e:\\" + filename + ".txt", "w") as fp2:
#         fp2.write(content + "\n")
#
#
# fp.close()


import re, sys


# srcfile  源文件
# search  搜索目标
# decfile  新文件
def openfile(srcfile, search, decfile):
    try:
        # f = open(srcfile, 'r')
        f = open(srcfile, 'r', encoding='UTF-8')
        try:
            while True:
                lines = f.readlines()

                if not lines:
                    break
                for line in lines:
                    if (line.find(search) >= 0):
                        writenewfile(line, decfile)
        finally:
            f.close()
            print('*' * 21 + "END" + "*" * 21)
    except IOError:
        print(srcfile + " not find!")


def writenewfile(line, decfile):
    try:
        newfile = open(decfile, 'a')
        try:
            newfile.write(line)
        finally:
            newfile.close()

    except IOError:
        print
        decfile + "not find!!"


if __name__ == '__main__':
    print('*' * 20 + "START" + "*" * 20)
    # makefile(sys.argv[1], sys.argv[2])
    srcfile='C:\\Users\\600336\\Desktop\\WMS—chem_log\\chem.log.2019-08-17'
    #srcfile = 'C:\\Users\\600336\\Desktop\\WMS—chem_log\\1.txt'
    search = 'SO201908179027F'
    decfile = 'C:\\Users\\600336\\Desktop\\WMS—chem_log\\new.txt'
    openfile(srcfile, search, decfile)

