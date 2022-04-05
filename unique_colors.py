# this file is to get all the unique colors from the file
from PIL import Image

img = Image.open('img.png', 'r')
data_tups = list(img.getdata())
data_lis = list()
for data in data_tups:
    data_lis.append(list(data))
unique_colors = []
for val in data_lis:
    if val not in unique_colors:
        unique_colors.append(val)
print(len(unique_colors), unique_colors)
