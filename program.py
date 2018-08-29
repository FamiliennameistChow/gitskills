# coding:utf-8
import os
import datetime

getdir = os.getcwd()
dirlist = ["编写资料", "附件资料", "文献调研", "申请材料", "报送下载文件"]
master_dir = input("请输入项目名称")
master_time = datetime.datetime.now().strftime('%g_%m_%d_')
dir = os.path.join(getdir, master_time+master_dir+"（待做）")
for dirs in dirlist:
    mkdir = os.path.join(dir, dirs)
    os.makedirs(mkdir)
    print("已创建：", mkdir)

'''
readmestr = "文件目录结构
--编写资料（编写文件的图、表）
--附件资料（协议、证明等）
--文献调研（参考文献）
--申请资料（申请指南原稿）
--报送下载文件（报送后文件）
合稿文件
'''
readmestr = "文件目录结构\n" \
            "--编写资料（编写文件的图、表）\n" \
            "--附件资料（协议、证明等）\n" \
            "--文献调研（参考文献）\n" \
            "--申请资料（申请指南原稿）\n" \
            "--报送下载文件（报送后文件）\n" \
            "合稿文件"

f = open(os.path.join(dir, "readme.txt"), mode='w')
f.write(readmestr)
f.close()

