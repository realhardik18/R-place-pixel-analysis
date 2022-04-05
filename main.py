import cv2
all_colors = list()
data = cv2.imread('img.png')
count = 0
for segments in data:
    for pixel_data in segments:
        vals = list(pixel_data)
        if vals not in all_colors:
            all_colors.append(vals)
print(count)
print(set)
