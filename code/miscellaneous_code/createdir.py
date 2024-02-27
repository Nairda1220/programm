import os
imagepath = r'/home/csp/zxy/v2j/images'
labelpath = r'/home/csp/zxy/v2j/labels'
filelist = os.listdir(imagepath)
for name in filelist:
    filename = os.path.splitext(name)[0]
    labelname = os.path.join(labelpath,filename)
    os.mkdir(labelname)