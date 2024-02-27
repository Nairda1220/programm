#!/usr/bin/env python3
# -*- coding:utf8 -*-
'''
将 images_path 里的所有图片划分为训练集、测试集，路径写入txt
'''

import os
import shutil
import random
from pathlib import Path

images_path = '/home/csp/zxy/mouse/yolo_B/dataset/images'

trainset_txt_file = '/home/csp/zxy/mouse/yolo_B/train.txt'
valset_txt_file   = '/home/csp/zxy/mouse/yolo_B/val.txt'

trainset_persent = 0.7
valset_persent   = 0.3

if __name__ == '__main__':

    # 获取所有图片列表
    image_files = []
    for f in Path( images_path ).rglob('*.jpg'):
        image_files.append(f)

    print('len(image_files) = ',len(image_files))
    
    # 随机打乱
    random.shuffle( image_files )    
    random.shuffle( image_files ) 
    random.shuffle( image_files ) 
    
    # 根据比例获取训练集、测试集
    trainset = image_files[ : int( len(image_files) * trainset_persent )]
    valset  = image_files[ int( len(image_files) * trainset_persent ) : ]
    print('len(trainset) = ',len(trainset),' ,len(valset) = ',len(valset))
    
    # 写入txt
    with open(trainset_txt_file,'w') as f:
        for file in trainset:
            f.write( str(file) + '\n')
    
    #with open(testset_txt_file,'w') as f:
        #for file in testset:
            #f.write( str(file) + '\n')

    with open(valset_txt_file,'w') as f:
        for file in valset:
            f.write( str(file) + '\n')
