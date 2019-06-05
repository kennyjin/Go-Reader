import numpy as np
import cv2
from matplotlib import pyplot as plt




"""
Get the color of the stone on the specific square.
Could be black stone, white stone or no stone.
TODO This function definitely needs further improvements.
1 means black, -1 means white, 0 means no stone.
"""


def get_stone_color(img):
    mean_color = np.mean(img)
    if mean_color >= 200:
        return -1
    if mean_color <= 90:
        return 1
    return 0


"""
Show RGB histogram of an image.
"""


def plot_histogram(img):
    color = ('b', 'g', 'r')
    for k, col in enumerate(color):
        hist = cv2.calcHist([img], [k], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()


img = cv2.imread('../images/13.PNG')
# cv2.imshow('image', img)
# cv2.waitKey(0)  # Need this other wise the window will not respond
# cv2.destroyAllWindows()
# print(img.item(10, 10))
print(img.shape)


# length_square = float(img.shape[0]) / 20
# print(length_square)
# # img_list = []
# # for i in range(1, 21):
# #     img_list.append(img[int(length_square * (i-1)): int(length_square * i), 0:int(length_square)])
# cv2.imshow('image', img[1:90, 0:76*20])
# cv2.waitKey(0)
# cv2.destroyAllWindows()


mean_color_list = np.array([])

for i in range(19):
    for j in range(19):
        # ret, piece = cv2.threshold(img[79 * i:79 * (i + 1), 79 * j:79 * (j + 1)], 75, 255, cv2.THRESH_BINARY)
        # cv2.imshow('image', piece)
        piece = img[49 + 94 * i:49 + 94 * (i + 1), 49 + 94 * j:49 + 94 * (j + 1)]
        # print(img[49 + 94 * i:49 + 94 * (i + 1), 49 + 94 * j:49 + 94 * (j + 1)].shape)
        # cv2.imshow('image', img[49 + 94 * j:49 + 94 * (j + 1), 49 + 94 * i:49 + 94 * (i + 1)])
        # print(img[79 * i:79 * (i + 1), 79 * j:79 * (j + 1)])
        # print(np.mean(piece))
        print(str(get_stone_color(piece)))
        # mean_color_list = np.append(mean_color_list, [np.mean(piece)])
        # print(img[79 * i:79 * (i + 1), 79 * j:79 * (j + 1)].var())
        cv2.imshow('image', piece)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
# print(mean_color_list)
# plt.hist(mean_color_list, bins=50)
# plt.show()





















