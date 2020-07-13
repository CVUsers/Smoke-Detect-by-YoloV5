import os
import random

trainval_percent = 0.1  # 可自行进行调节
train_percent = 1
xmlfilepath = './data/Annotations'
txtsavepath = './data/ImageSets\Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

# ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('./data/ImageSets/Main/test.txt', 'w')
ftrain = open('./data/ImageSets/Main/train.txt', 'w')
# fval = open('ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        # ftrainval.write(name)
        if i in train:
            ftest.write(name)
        # else:
        # fval.write(name)
    else:
        ftrain.write(name)

# ftrainval.close()
ftrain.close()
# fval.close()
ftest.close()

# import os
# import cv2
#
# for file in os.listdir(r'D:\Memory_Demo\something_to_use\yolov5\data\images'):
#     # print(file)
#     img = cv2.imread(r'D:/Memory_Demo/something_to_use/yolov5/data/images/{}'.format(file))
#     try:
#         cv2.imshow('s', img)
#         # cv2.waitKey()
#     except:
#         print(file)