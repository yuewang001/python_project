# 将图文件按照文件名提示的日期进行归类， 例如2011年的文件，存放在创建的2011文件夹中
import os
import shutil


def  isStartwith(_file, _str):
    if _file.startswith(_str):
        return True
    else:
        return False


def iswhileYear(_file):

    for year in range(2022,1980,-1):
        _str="IMG_"+str(year)
        if isStartwith(_file,_str):
            return year
        _str="VID_"+str(year)
        if isStartwith(_file,_str):
            return year
    return 0

root_path="F:\\百度网盘个人\\家庭\\照片视频\\视频"
result_path="F:\\picture_sort_result8"


def move_file(_path_file):
    fn=os.path.basename(_path_file)
    _year=iswhileYear(fn)

    if _year==0:
        print(_path_file +"    is not moved")
        return

    if not os.path.exists(result_path):
        os.makedirs(result_path)

    new_path=result_path+"\\"+str(_year)

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    if os.path.exists(new_path+"\\"+fn):
        print(new_path+"\\"+fn + " is existed")
        return
    
    shutil.move(_path_file, new_path+"\\"+fn )
    print(fn+"  done")



def do_it(root_path):
    for l in os.listdir(root_path):
        f=root_path+"\\"+l
        if(os.path.isfile(f)):
            move_file(f)
            continue

        if(os.path.isdir(f)):
            do_it(f)

do_it(root_path)
print(" well done ")

    
 