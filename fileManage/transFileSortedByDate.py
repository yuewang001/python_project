
import os
import shutil

root_path="C:\\Users\\wangy\\Desktop\\新建文件夹 (4)\\WeiXin"
#root_path="G:\\pic2"
result_path="C:\\Users\\wangy\\Desktop\\picture_sort_result8"

file_todo_list=[]
newft_list=[]

def judge_file(f):
    dname=os.path.dirname(f)
    bname=os.path.basename(f)
    suffix_name=os.path.splitext(f)[-1]
    if (len(bname)-len(suffix_name)<12):
        return

    try:
        stimestamp=bname[0:12]

        i=11
        f_fm="20"
        while(i>0):
            f_fm=f_fm+stimestamp[i-1:i+1]
            i=i-2
            if(i==5):
                f_fm=f_fm+"_"

        
        #print(f_fm)

        s_year=f_fm[0:4]
        s_mon=f_fm[4:6]
        s_day=f_fm[6:8]
        s_sec=f_fm[9:11]
        s_min=f_fm[11:13]
        s_h=f_fm[13:]
    except:
        pass

        

        if  int(s_year)>2023 or int(s_year)<2005:
            return
        if  int(s_mon)>12 or int(s_mon)<1:
            return
        if  int(s_day)>31 or int(s_day)<1:
            return

        if  int(s_h)>23 or int(s_h)<0:
            return
        
        if  int(s_min)>59 or int(s_min)<0:
            return
        if  int(s_sec)>59 or int(s_min)<0:
            return

    newf=s_year+s_mon+s_day+"_"+s_h+s_min+s_sec
    file_todo_list.append(f)
    #print(dname+"\\"+f_fm+suffix_name)
    newft_list.append(dname+"\\"+newf+suffix_name)




#寻找满足文件名称为12位开头有时间信息的。 
def search_list(root_path):
    for l in os.listdir(root_path):
        f=root_path+"\\"+l
        if(os.path.isfile(f)):
            judge_file(f)
            continue

        if(os.path.isdir(f)):
            search_list(f)

def  renameAllfile(_flist,_newlist):

    if(len(_flist) != len(_newlist)):
        print("error: length of file not equall")
        return 
    leth=len(_flist)

    for i in range(leth):
        l=_flist[i]
        n=_newlist[i]
        print(l+"    to   "+n)
        shutil.move(l, n )



search_list(root_path)
renameAllfile(file_todo_list,newft_list)
print(" well done ")