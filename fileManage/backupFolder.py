#从 目录A  备份所有文件到B， 对比相应的目录和文件，如果文件名相同，比较大小以及最后修改的时间。
from genericpath import isdir
import os
from posixpath import dirname
import shutil
import time

source_folder="D:\\我的工作"
target_folder="I:\\工作"
source_list=[]
target_list=[]


def do_file(sf,tf):
    if not os.path.exists(tf):
        source_list.append(sf)
        target_list.append(tf)
        return 
    
    sf_mtime = time.ctime(os.path.getmtime(sf))
    tf_mtime = time.ctime(os.path.getmtime(tf))

    if sf_mtime!=tf_mtime:
        source_list.append(sf)
        target_list.append(tf)

def do_folder(sp,tp):
    for l in os.listdir(sp):
        sf=sp+"\\"+l
        tf=tp+"\\"+l
        if(os.path.isfile(sf)):
            do_file(sf,tf)
            continue

        if(os.path.isdir(sf)):

            if not os.path.exists(tf):
                source_list.append(sf)
                target_list.append(tf)
                continue

            do_folder(sf,tf)

def copy_all(s,t):
    for i in range(len(s)):
        print(s[i]+" to  " +t[i] )
        if os.path.isdir(s[i]):
            shutil.copytree(s[i],t[i])
            continue

        shutil.copy(s[i],t[i] )

if not os.path.exists(source_folder):
    print(source_folder+" does not exist")
    exit()

if not os.path.exists(target_folder):
    print(target_folder+" does not exist")
    exit()


do_folder(source_folder,target_folder)
copy_all(source_list,target_list)
print("well done")
