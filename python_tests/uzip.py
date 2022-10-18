#!/usr/bin/env python
import os
import sys
import zipfile

file=zipfile.ZipFile(sys.argv[1],"r");
os.chdir(sys.argv[2])
for name in file.namelist():
	utf8name=name.decode('gbk')
	#pathname=sys.argv[2]+os.path.dirname(utf8name)
	pathname=os.path.dirname(utf8name)
	if not os.path.exists(pathname) and pathname!="":
		os.makedirs(pathname)
	data=file.read(name)
	#utf8name=sys.argv[2]+utf8name
	if not os.path.exists(utf8name):
		fo=open(utf8name,"w")
		fo.write(data)
		fo.close()
file.close()
