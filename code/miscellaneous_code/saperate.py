import os
import shutil
file_path = r'/home/csp/zxy/mouse/allmouse(1)'
save_path = r'/home/csp/zxy/mouse/xml'
filelist = os.listdir(file_path)
for file in filelist:
    file_in = os.path.join(file_path,file)
    if file.endswith('.xml'):
        shutil.move(file_in,save_path)
    else:
        continue