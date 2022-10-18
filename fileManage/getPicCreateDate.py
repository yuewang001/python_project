
import os
import time
import exifread

imgPath = 'F:\\百度网盘个人\\家庭\\照片视频\\视频2\\18415703051672f124d789228.mp4'
MY_DATE_FORMAT = '%Y%m%d_%H%M%S'
VIDEO_LIST = ['.mp4', '.avi', '.mov']
IMAGE_LIST = ['.jpg', '.png', '.mpg', '.thm', '.bmp', '.jpeg']
SUFFIX_FILTER = ['.mp4']

def generateNewFileName(filename):
     #根据照片的拍照时间生成新的文件名（如果获取不到拍照时间，则使用文件的创建时间）
     try :
         if os.path.isfile(filename):
             fd = open(filename, 'rb')
         else :
             raise "[%s] is not a file!\n" % filename
     except :
         raise "unopen file [%s]\n" % filename

     
     data = exifread.process_file(fd)
     print(data)
     print(data.get('Image DateTime', '0'))
     if data :
         #取得照片的拍摄日期
         try :
             t = data['EXIF DateTimeOriginal']
             #转换成 yyyymmdd_hhmmss的格式
             dateStr = str(t).replace(":", "")[: 10] + "_" + str(t)[11:].replace(":", "")
         except :
             pass

     #如果没有取得exif信息，则用图像文件的创建日期作为拍摄日期
     state = os.stat(filename)
     dateStr = time.strftime(MY_DATE_FORMAT, time.localtime(state[-2]))
     dirname = os.path.dirname(filename)
     filename_nopath = os.path.basename(filename)
     f, e = os.path.splitext(filename_nopath)
     if e.lower() in VIDEO_LIST:
         dateStr = 'VID_' + dateStr
     elif e.lower() in IMAGE_LIST:
         dateStr = 'IMG_' + dateStr
     newFileName = os.path.join(dirname, dateStr + e)
     print(newFileName)
     return newFileName
generateNewFileName(imgPath)

