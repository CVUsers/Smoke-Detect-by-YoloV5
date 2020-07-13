# 缺陷坐标xml转txt
import os
import xml.etree.ElementTree as ET
def rename_func(path, path2):
    num = 0

    for file in os.listdir(path):
        # fileNew = 'smoke'+file.lower()
        # print("Old:", file, "New", fileNew)
        filename = file.split('.')[0]
        flag = 0
        for file2 in os.listdir(path2):
            filename2 = file2.split('.')[0]
            # if(fileNew != file):
                # os.rename(path + file, path + fileNew)
            if filename == filename2:
                # print(file, file2)
                flag = 1
                num +=1
                break
        if flag == 0:
            print('***'*4, file)
    print(num, os.listdir(path2).__len__(), os.listdir(path).__len__())

path = r'D:\Memory_Demo\something_to_use\yolov5\labels/'
path2 = r"D:\Memory_Demo\something_to_use\yolov5\data\Annotations/"


# rename_func(path2, path)

def rename_funcs(path):
    i = 187
    for file in os.listdir(path):
        # fileNew = 'smoke_a'+ str(i) + '.xml'
        # i += 1
        # print("Old:", file, "New", fileNew)
        # if(fileNew != file):
            # os.rename(path + file, path + fileNew)
        print(file.split('.')[0])
path = './data/Annotations'
# path2 = r"F:\firefox\smoke_demo\Smoke_detection-master\Smoke_detection-master\YOLOv3_TensorFlow-master\data\xml/"
print(os.listdir(path).__len__())
# rename_funcs(path)

# classes = ["smoke"]  # 输入缺陷名称，必须与xml标注名称一致
#
# def convert(size, box):
#     print(size, box)
#     dw = 1. / size[0]
#     dh = 1. / size[1]
#     x = (box[0] + box[1]) / 2.0
#     y = (box[2] + box[3]) / 2.0
#     w = box[1] - box[0]
#     h = box[3] - box[2]
#     x = x * dw
#     w = w * dw
#     y = y * dh
#     h = h * dh
#     return (x, y, w, h)
#
#
# def convert_annotation(image_id):
#     print(image_id)
#     in_file = open(r'./data/Annotations/%s.xml' % (image_id), 'rb')  # 读取xml文件路径
#
#     out_file = open('./labels/%s.txt' % (image_id), 'w')  # 需要保存的txt格式文件路径
#     tree = ET.parse(in_file)
#     root = tree.getroot()
#     size = root.find('size')
#     w = int(size.find('width').text)
#     h = int(size.find('height').text)
#
#     for obj in root.iter('object'):
#         cls = obj.find('name').text
#         if cls not in classes:  # 检索xml中的缺陷名称
#             continue
#         cls_id = classes.index(cls)
#         xmlbox = obj.find('bndbox')
#         b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
#              float(xmlbox.find('ymax').text))
#         bb = convert((w, h), b)
#         out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
#
#
# image_ids_train = open('./ImageXML.txt').read().strip().split()  # 读取xml文件名索引
#
# for image_id in image_ids_train:
#     print(image_id)
#     convert_annotation(image_id)

