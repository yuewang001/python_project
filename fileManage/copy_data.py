#用来场站测试数据的，复制和移动
import os
from re import X
import sys
import shutil


if len(sys.argv)<2:
    print("未有输入参数，第一个参数为数据的根目录，第二个参数为set的起始数字，第三个参数为set的结尾数字，第四个参数为将要复制的文件")
    print("例如： copy_data.exe  D://test/data   5 100  D://V2.txt")
    sys.exit()

root_path=sys.argv[1]
set_begin=int(sys.argv[2])
set_end=int(sys.argv[3])
f=sys.argv[4]

if not os.path.exists(f):
    print("file does not exit: "+f)
    sys.exit()

if not os.path.exists(root_path):
    print("path does not exit: "+root_path)
    sys.exit()

for  i  in range(set_begin,set_end,1):
    x="set"+str(i)
    x=root_path+'\\'+x
    
    if  os.path.exists(x)  and os.path.isdir(x):
        print(x)
        shutil.copy(f,x)
print(" all are done")





