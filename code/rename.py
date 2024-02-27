import os
file_name = r'/home/csp/zxy/mouse/kmeansmouse'

for i in range(0,8):
    file_path = file_name + "/" + "cluster" + str(i)
    file_list = os.listdir(file_path)
    count = 0
    for name in file_list:
        if name.endswith('.xml'):
            count = count + 1
            old_xmlname = os.path.join(file_path,name)
            new_xmlname = os.path.join(file_path,f'csp_mouse_{i}_{"%04d" % count}.xml')
            xml_name = os.path.splitext(name)[0]
            for name in file_list:
                if name.endswith('.jpg'):
                    old_jpgname = os.path.join(file_path,name)
                    new_jpgname = os.path.join(file_path,f'csp_mouse_{i}_{"%04d" % count}.jpg')
                    pic_name = os.path.splitext(name)[0]
                    if pic_name == xml_name:
                        os.rename(old_xmlname,new_xmlname)
                        os.rename(old_jpgname,new_jpgname)
                    else:
                        continue
                else:
                    continue
        else:
            continue
