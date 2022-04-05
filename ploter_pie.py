# this file is to plot everything in the form of a piechart
import matplotlib.pyplot as plt
import webcolors

colors_count = [11142, 524141, 168168, 936615, 275851, 140285, 66998, 32090, 228688, 167448, 237540, 68894, 65503, 36362, 21801,
                62111, 126053, 138652, 65606, 59954, 93951, 110377, 43814, 33511, 24212, 14230, 124059, 46802, 40886, 6724, 16636, 10896]  # output from running plotter.py
all_colors_rgb = [[222, 16, 127], [255, 255, 255], [255, 168, 0], [0, 0, 0], [255, 69, 0], [54, 144, 234], [129, 30, 159], [180, 74, 192], [255, 214, 53], [190, 0, 57], [36, 80, 164], [109, 72, 47], [255, 153, 170], [0, 117, 111], [73, 58, 193], [81, 82, 82], [137, 141, 144], [212, 215, 217], [126, 237, 86], [255, 180, 112], [156, 105, 38], [0, 163, 104], [0, 204, 120], [255, 56, 129], [148, 179, 255], [0, 158, 170], [81, 233, 244], [255, 248, 184],
                  [109, 0, 26], [0, 204, 192], [106, 92, 255], [228, 171, 255]]  # output from running unique_colors.py
all_colors_hex = []
for color in all_colors_rgb:
    all_colors_hex.append(webcolors.rgb_to_hex(tuple(color)))
print(all_colors_hex)
plt.pie(colors_count, colors=all_colors_hex,
        wedgeprops={"edgecolor": "0", 'linewidth': 1})
plt.title('proportion of colors in r/place 2022')
plt.savefig('2022.png')
