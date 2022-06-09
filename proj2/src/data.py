import xml.etree.ElementTree as ET

import os

print(os.getcwd())

train = open("VC-Group4/proj2/dataset/train.txt", "r")
#test = open("VC-Group4/proj2/dataset/test.txt", "r")

train_csv = open("VC-Group4/proj2/dataset/train_csv.csv", "w")
#test_csv = open("VC-Group4/proj2/dataset/test_csv.csv", "w")

for image in train:
    root = ET.parse('VC-Group4/proj2/dataset/annotations/' + image[:-1] + '.xml').getroot()
    annotations = {}
    classArray = []
    for child in root:
        maxArea = 0
        if child.tag == "object":
            for grandchild in child:
                if grandchild.tag == "name":
                    name = grandchild.text

                if grandchild.tag == "bndbox":
                    for grandgrandchild in grandchild:
                        if grandgrandchild.tag == "xmin":
                            xmin = int(grandgrandchild.text)
                        if grandgrandchild.tag == "ymin":
                            ymin = int(grandgrandchild.text)
                        if grandgrandchild.tag == "xmax":
                            xmax = int(grandgrandchild.text)
                        if grandgrandchild.tag == "ymax":
                            ymax = int(grandgrandchild.text)
                    
                    area = (xmax-xmin)*(ymax-ymin)
                    if (area > maxArea):
                        maxArea = area
                        maxSign = name
    
    if (name == 'speedlimit'):
        num = 0
    elif (name == 'trafficlight'):
        num = 1
    elif (name == 'crosswalk'):
        num = 2
    elif (name == 'stop'):
        num = 3
                
    train_csv.write(image[:-1] + ',' + str(num) + '\n')
    #test_csv.write(image[:-1] + ',' + str(num) + '\n')

train.close()
#test.close()

train_csv.close()
#test_csv.close()