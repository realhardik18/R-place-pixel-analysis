# this file is to get the count of all the pixels colorwise
from PIL import Image
all_colors = [[222, 16, 127], [255, 255, 255], [255, 168, 0], [0, 0, 0], [255, 69, 0], [54, 144, 234], [129, 30, 159], [180, 74, 192], [255, 214, 53], [190, 0, 57], [36, 80, 164], [109, 72, 47], [255, 153, 170], [0, 117, 111], [73, 58, 193], [81, 82, 82], [137, 141, 144], [212, 215, 217], [126, 237, 86], [255, 180, 112], [156, 105, 38], [0, 163, 104], [0, 204, 120], [255, 56, 129], [148, 179, 255], [0, 158, 170], [81, 233, 244], [255, 248, 184],
              [109, 0, 26], [0, 204, 192], [106, 92, 255], [228, 171, 255]]  # output from running unique_colors.py
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

img = Image.open('2017/img2.png', 'r')
data_tups = list(img.getdata())
data_lis = list()
for data in data_tups:
    data_lis.append(list(data))
for c in data_lis:
    count[all_colors.index(c)] += 1
print(sum(count))
