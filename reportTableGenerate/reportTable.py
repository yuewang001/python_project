import os
import commands
import time
import re

table_name="Table_Result"

def readContent(ValueFile):
    Matrix_Content=[]
    #print ValueFile
    with open(ValueFile,'r') as f:
        for line in f:
            mtmp=[]
            #line.split(",").strip()
            for eachone in line.split(","):
                #eachone.strip()
                mtmp.append(eachone.strip())
                
            Matrix_Content.append(mtmp)
            
    return Matrix_Content


            
        
def  parseRecord(record):
    tmp=record.split("-")
    return tmp


def writefile(filename, data):
    fo = open(filename, "w")
    for line in data:
        for astr in line:
            tmp=str(astr)+"   "
            fo.write(tmp)
        fo.write("\n")
            
    fo.close
    
def readKeyValue(index):
    global File_Matrix1
    global File_Matrix2
    
#     print "****************"
#     print index[0]
#     print index[1]
#     print index[2]
#     print "****************"
    File_Matrix=[]
        
    if index[0]=="R1":
        File_Matrix=File_Matrix1
  
    else:
        File_Matrix=File_Matrix2
    
    sub_index=index[2].split(".")
    x_row=int(sub_index[0])-1
    x_col=int(sub_index[1])-1     
    #print x_row
    #print x_col 
    for xx in File_Matrix:
        #print xx[0]
        if xx[0]==index[1]:
            #print  xx[1][x_row][x_col]
            #f_tmp=float(xx[1][x_row][x_col])
            #return float('%.2f' % f_tmp)
            #print "&&&&&&&&&&&&&&&&&"
            return xx[1][x_row][x_col]
            
            

def getConfig(configfile):
    with open(configfile,'r') as f1:
        table_start=0
        table_data=[]
        table_end=0
        global table_name
        for line in f1:
            if line.startswith("Table:"):
                table_start=1
                #print line
                #table_name=line[6:].strip()
                table_data.append(line)
                continue
            
            if  line.startswith("End"):
                #writefile(prepath+"\\"+table_name+".txt",table_data)
                #table_end=1
                continue

            l=line.split()
            row_data=[]
            for record  in  l:
                #print record 
                Value=parseRecord(record)
                tmp_value=readKeyValue(Value)
                
                row_data.append(tmp_value)
                
            table_data.append(row_data)
         
                
 
            

    writefile(prepath+"\\"+table_name+".txt",table_data)

prepath='c:\\Users\\wangy\\Desktop\\1102\Result1'

File_Matrix1=[]
File_Matrix2=[]
Count1_ValueFile=0
Count2_ValueFile=0

files = os.listdir(prepath)
for fi in files:
    #print fi
    
    print  prepath+"\\"+fi
    ValueFileName=prepath+"\\"+fi
    Value=readContent(ValueFileName)
    #print "-------------"
    #print Value[2][3]  #col 4, line 3
    #print Value[3][2]
    #print Value[0][3]  #col 4, line 1
    #print Value[3][0]  #col 1, line 4
    #MaxValue1.txt ->M1
    digit = re.search('\d+', fi).group()
    s_tmp="M"+digit
    print s_tmp
    File_Matrix1.append([s_tmp,Value])
    #print File_Matrix1[Count1_ValueFile][0]
    #print File_Matrix1[Count1_ValueFile][1]
    Count1_ValueFile=Count1_ValueFile+1

print Count1_ValueFile

# for xx in File_Matrix1:
#     print xx[0]
#     if xx[0]=='M11':
#         print xx[1]


prepath='c:\\Users\\wangy\\Desktop\\1102\Result2'
files = os.listdir(prepath)
for fi in files:
    #print fi
    
    print  prepath+"\\"+fi
    ValueFileName=prepath+"\\"+fi
    Value=readContent(ValueFileName)
    #print "-------------"
    #print Value[2][3]  #col 4, line 3
    #print Value[3][2]
    #print Value[0][3]  #col 4, line 1
    #print Value[3][0]  #col 1, line 4
    #MaxValue1.txt ->M1
    digit = re.search('\d+', fi).group()
    s_tmp="M"+digit
    print s_tmp
    File_Matrix2.append([s_tmp,Value])
    #print File_Matrix2[Count1_ValueFile][0]
    #print File_Matrix2[Count1_ValueFile][1]
    Count2_ValueFile=Count2_ValueFile+1

print Count2_ValueFile
prepath='c:\\Users\\wangy\\Desktop\\1102\\'

configfile='c:\\Users\\wangy\\Desktop\\1102\config.TXT'
getConfig(configfile)