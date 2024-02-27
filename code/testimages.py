import os
import shutil
txtfile = open('/home/csp/lzd/data/test.txt')
save_file = r'/home/csp/yolov5/testimages2'
file_path = txtfile.readlines()
for line in file_path:
    str1 = line.split(" ")
    print(str1)
    image_path = str1[0].strip()
    print(image_path)
    str2 = image_path.split("/")
    image_name = str2[len(str2)-1]
    save_path = os.path.join(save_file,image_name)
    shutil.copyfile(image_path,save_path)
