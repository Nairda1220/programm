import os
import shutil
xml_path = r"/home/csp/zxy/mouse/Annotations_38724"
folder_name = r"/home/csp/zxy/mouse/kmeans_img_cluster_output"
listdir = os.listdir(xml_path)
for dir in listdir:
    dir_path = os.path.join(xml_path,dir)
    dirname = os.path.splitext(dir)[0]
    for i in range(0,7):
        pic_path = folder_name + "/" + "cluster" + str(i)
        listpic = os.listdir(pic_path)
        print("pic_path is...")
        for photo in listpic:
            picname = os.path.splitext(photo)[0]
            if picname == dirname:
               print("Y")
               shutil.move(dir_path,pic_path)
            else:
                continue