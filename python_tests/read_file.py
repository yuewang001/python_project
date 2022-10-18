import os

sourcepath='/home/yuewang/tmp1'
for file in os.listdir(sourcepath):
    f = open(file,"r")
    data2 = f.readlines()
    print(data2)

