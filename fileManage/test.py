


import os
import shutil


root_path="D:\\空间照片\\630776347"
tmp_path="D:\\tmp\\"

def move_file(suffix_dir, dpath,filenamelist,ite):
    #new folder 
    if ite>0:
        new_path=tmp_path+"\\"+dpath+"_"+str(ite)
    else:
        new_path=tmp_path+"\\"+dpath

    print("new path:"+new_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    
    for f in filenamelist:
        #shutil.move(f,new_path)
        fn=os.path.basename(f)
        shutil.copyfile(f, new_path+"\\"+fn )
        print("processing: "+new_path+": " +fn)
     


if  not  os.path.exists(root_path):
    print(root_path+"  does not exit")
    exit(-1)

print("start to work on :"+root_path)

for d in os.listdir(root_path):
    print(d)
    num=0
    file_list=[]
    print("--------------")
    ite=0
    for f in  os.listdir(root_path+"\\"+d):
        #print(f)
        num=num+1
        file_list.append(root_path+"\\"+d+"\\"+f)
        if num==499:
            ite=ite+1
            num=0
            move_file(root_path,d, file_list,ite)
            file_list.clear()

    if ite>0:
        ite=ite+1
    move_file(root_path,d, file_list,ite)



    
    print("---------------\n")




