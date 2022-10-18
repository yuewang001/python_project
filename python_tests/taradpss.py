import zipfile
import os


filename='C:\\Users\\wangy\\Desktop\\tmp.zip'
z = zipfile.ZipFile(filename, 'w') 

source_path='C:\\Users\\wangy\\Desktop\\tmp1'
if os.path.isdir(source_path):
    for d in os.listdir(source_path):
        print("filename:"+d)
        utf8name = d.encode('utf-8','strict');


        os.rename(d,utf8name)
        #print('utf8name:'+utf8name)
        #z.write(source_path+os.sep+d)
z.close()
print('done------------')
if os.path.isdir(source_path):
    for d in os.listdir(source_path):
        print("filename:"+d)


        #print('utf8name:'+utf8name)
        #z.write(source_path+os.sep+d)
z.close()