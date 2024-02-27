import os
from xml.etree.ElementTree import parse, Element
 
 
def changeName(xml_fold, origin_name, new_name):
    files = os.listdir(xml_fold)
    cnt = 0
    for xmlFile in files:
        if xmlFile.endswith('.xml'): # 遍历所有XML文件
            file_path = os.path.join(xml_fold, xmlFile) # 获取XML文件地址
            dom = parse(file_path)
            root = dom.getroot()
            for obj in root.iter('object'):
                tmp_name = obj.find('name').text
                if tmp_name == origin_name:
                    obj.find('name').text = new_name # 更改标签名字
                    print("change %s to %s." % (origin_name, new_name))
                    cnt += 1
            dom.write(file_path, xml_declaration=True)
        else:
            continue
        

file_name = r'/home/csp/zxy/mouse/kmeansmouse'
for i in range(0,8):
    xml_path = file_name + "/" + "cluster" + str(i)
    changeName(xml_path, 'whitemouse', 'mouse')
