#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import os


def video2JPG(videopath,jpgpath):
    file_name = os.path.basename(videopath)
    folder_name = os.path.join(jpgpath,file_name.split('.')[0])
    
    # 创建文件夹
    try:
        os.makedirs(folder_name, exist_ok=True)
    except Exception as e:
        print("failed to makedirs", folder_name, e)
    
    # 获取视频，打开cap
    cap = cv2.VideoCapture(videopath)
    n_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # 设置间隔为20帧
    framefrequency = 20
    count = 0 # 记录读取到哪一帧
    rval = cap.isOpened()
    while rval:
        if count == n_frame:
            break
        else:
            count = count + 1
        rval,frame = cap.read()
        pic_path=folder_name + "/" + str(int(count/20)) + ".jpg"
        
        
        # 每隔20帧复制一次到导出文件夹中
        if count % framefrequency == 0:
            cv2.imwrite(pic_path,frame,[cv2.IMWRITE_JPEG_QUALITY,100])
    cap.release()
    
    
    
# 视频路径   
filepath = "/home/csp/视频"

#导出图片路径
jpgfolder = "/home/csp/zxy/vido2JPG"
filelist = os.listdir(filepath)
for fileName in filelist:
    videopath = os.path.join(filepath,fileName)
    video2JPG(videopath,jpgfolder)

