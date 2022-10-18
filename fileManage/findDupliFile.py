# 查询文件夹中所有重复的文件，通过文件名，大小进行判别

from math import fabs
import os
import shutil



#diction, key is filename, value is the list of pathes. 

file_path_dic={}

def  update_dic(_file, _path):
    if file_path_dic.get(_file)==None:
        path_list=[]
        path_list.append(_path)
        file_path_dic[_file]=path_list

        return
    
    path_list=file_path_dic.get(_file)
    path_list.append(_path)
    file_path_dic[_file]=path_list


def  list_all_file(root_path):
    if  not  os.path.exists(root_path):
        print(root_path+"  does not exit")
        exit(-1)
    
    for l in os.listdir(root_path):
        f=root_path+"\\"+l
        if(os.path.isfile(f)):
            #put the file into the dic
            #print(f+"  is a file")
            update_dic(l,root_path)


        else:
            if(os.path.isdir(f)):
                #print(f+"  is a path")
                list_all_file(f)

root_path="D:\\test"
list_all_file(root_path)

print(" to  print the dic")

result_file=open('D:\\duplicate_files.txt',mode='w')

i=0
for f,path_list in file_path_dic.items():
    i=i+1
    result_file.write(" No. "+str(i)+"\n")
    for p in path_list:
        p_file=p+"\\"+f
        _size=os.path.getsize(p_file)
        result_file.write(p_file+ "         "+str(_size)+"\n")

    result_file.write("-------------\n\n")
result_file.close()
print(" Done well")    
    


