import numpy as np
import cv2
from matplotlib import pyplot as plt


"""
Get the color of the stone on the specific square.
Could be black stone, white stone or no stone.
TODO This function definitely needs further improvements.
1 means black, -1 means white, 0 means no stone.
"""


def get_stone_color(square):
    mean_color = np.mean(square)
    if mean_color >= 200:
        return -1
    if mean_color <= 90:
        return 1
    return 0


"""
Get game position a Go board image, return an 2d array of numbers(-1, 0 or 1).
Each square could contain black stone, white stone or no stone.
"""


def get_game_position(go_board, edge_len_x, edge_len_y, stone_len, board_size=19):
    rows = cols = board_size
    pos_array = [[0 for i in range(cols)] for j in range(rows)]
    for y in range(board_size):
        for x in range(board_size):
            piece = go_board[edge_len_y + stone_len * y:edge_len_y + stone_len * (y + 1),
                             edge_len_x + stone_len * x:edge_len_x + stone_len * (x + 1)]
            pos_array[y][x] = get_stone_color(piece)
            # print(square_array[y])
            # cv2.imshow('image', piece)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
    return pos_array


"""
Get Go board from an image.
"""


def get_go_board(game_image):
    return None



"""
Generate sgf string according to the game position array.
"""


def get_sgf_txt(pos_array, board_size=19):
    black_pos = []
    white_pos = []
    sgf_txt = "(;"
    for i in range(board_size):
        for j in range(board_size):
            if pos_array[i][j] == 1:
                black_pos.append(num_to_letter(j)+num_to_letter(i))
            if pos_array[i][j] == -1:
                white_pos.append(num_to_letter(j)+num_to_letter(i))
    sgf_txt += "AB"
    for pos in black_pos:
        sgf_txt += "[" + pos + "]"
    sgf_txt += "AW"
    for pos in white_pos:
        sgf_txt += "[" + pos + "]"
    sgf_txt += ")"
    return sgf_txt


"""
Transform coordinate(number) to coordinate(letter).
Number should be from 0-18, letter should be a-s.
"""


def num_to_letter(num):
    diff = ord('a') - 0
    return chr(num + diff)



"""
Convert Go game image to an sgf file.
"""


def img_to_sgf(game_image, sgf_file):
    return None


"""
Show RGB histogram of an image.
"""


def plot_histogram(square):
    color = ('b', 'g', 'r')
    for k, col in enumerate(color):
        hist = cv2.calcHist([square], [k], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()


img = cv2.imread('../images/13.PNG')


# mean_color_list = np.array([])
#
# for i in range(19):
#     for j in range(19):
#         # ret, piece = cv2.threshold(img[79 * i:79 * (i + 1), 79 * j:79 * (j + 1)], 75, 255, cv2.THRESH_BINARY)
#         # cv2.imshow('image', piece)
#         piece = img[49 + 94 * i:49 + 94 * (i + 1), 49 + 94 * j:49 + 94 * (j + 1)]
#         # print(img[49 + 94 * i:49 + 94 * (i + 1), 49 + 94 * j:49 + 94 * (j + 1)].shape)
#         # cv2.imshow('image', img[49 + 94 * j:49 + 94 * (j + 1), 49 + 94 * i:49 + 94 * (i + 1)])
#         # print(img[79 * i:79 * (i + 1), 79 * j:79 * (j + 1)])
#         # print(np.mean(piece))
#         print(str(get_stone_color(piece)))
#         # mean_color_list = np.append(mean_color_list, [np.mean(piece)])
#         # print(img[79 * i:79 * (i + 1), 79 * j:79 * (j + 1)].var())
#         cv2.imshow('image', piece)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
# print(mean_color_list)
# plt.hist(mean_color_list, bins=50)
# plt.show()


game_position = get_game_position(img, 49, 49, 94)


f = open("out1.sgf", "w")
f.write(get_sgf_txt(game_position))
f.close()







