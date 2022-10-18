import os
from posixpath import dirname
import shutil
import time

#获取微信图片的创建时间。
#root_path="F:\\整理2022\\按年份分类"
root_path="C:\\Users\wangy\\Desktop\\新建文件夹 (4)\\WeiXin"
result_path="C:\\Users\wangy\\Desktop\\result"
str_tmp="mmexport"
#str_tmp=""
def  isStartwith(_file, _str):
    if _file.startswith(_str):
        return True
    else:
        return False

def  timestampToRealDate(s_Timestamp):
    tre_timeArray = time.localtime(float(s_Timestamp)/1000)
    tre_otherStyleTime = time.strftime("%Y%m%d_%H%M%S", tre_timeArray)
    return tre_otherStyleTime

def  do_wx_file_date_cal(_file):
       
    len_str_tmp=len(str_tmp)
    pos=_file.find(str_tmp)

    suffix_name=os.path.splitext(_file)[-1]

    end_pos=_file.find(suffix_name)
    
    s_Timestamp=_file[pos+len_str_tmp:end_pos]
    new_file_date=timestampToRealDate(s_Timestamp)
    return new_file_date

def  do_file(_file):
    
    _base_name=os.path.basename(_file)
    _path=os.path.dirname(_file)
    if not isStartwith(_base_name, str_tmp):
        print(_file+"  ignored")
        return 
    
    _dateofFile=do_wx_file_date_cal(_base_name)
    target_path=result_path+"\\"+_dateofFile[0:4]
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    new_file_date=target_path+"\\"+_dateofFile+"_"+_base_name
    #print("new file:"+new_file_date)
    #创建新的文件，将源文件删除


    shutil.move(_file, new_file_date )
    print("done    "+ _file+"  :  "+new_file_date)


def do_folder(root_path):
    if not os.path.exists(root_path):
        print("error the path does not existed:  "+root_path)
        return 

    if not os.path.exists(result_path):
        os.makedirs(result_path)
    for l in os.listdir(root_path):
        f=root_path+"\\"+l
        if(os.path.isfile(f)):
            do_file(f)
            continue

        if(os.path.isdir(f)):
            do_folder(f)

#os.path.splitext(path)[-1]
#do_wx_file_date_cal("wx_camera_1498349112443")
do_folder(root_path)

