import xml.etree.ElementTree as ET

#train = open("../dataset/train.txt", "r")
test = open("../dataset/test.txt", "r")

#train_csv = open("../dataset/train_csv.csv", "w")
test_csv = open("../dataset/test_csv.csv", "w")

for image in test:
    root = ET.parse('../dataset/annotations/' + image[:-1] + '.xml').getroot()
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
                
    #train_csv.write(image[:-1] + ',' + name + '\n')
    test_csv.write(image[:-1] + ',' + name + '\n')

#train.close()
test.close()

#train_csv.close()
test_csv.close()