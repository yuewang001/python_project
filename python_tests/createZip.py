import os
import sys
import zipfile

zip_file= sys.argv[1]
path_comp=sys.argv[2]

if not os.path.exists(path_comp):
    print(path_comp+"  does not exist")
    exit(-1)

f=zipfile.ZipFile(zip_file,"w")
for dirpath, dirnames, filenames in os.walk(path_comp): 
        for filename in filenames: 
            f.write(os.path.join(dirpath,filename)) 
f.close() 
