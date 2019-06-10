import numpy as np
import cv2
from matplotlib import pyplot as plt


"""
Get the color of the stone on the specific square.
Could be black stone, white stone or no stone.
TODO This function definitely needs further improvements.
1 means black, -1 means white, 0 means no stone.
These thresholds are set for fox Go server.
"""


def get_stone_color(square, black_thresh=90, white_thresh=190):
    mean_color = np.mean(square)
    # print(mean_color)
    if mean_color >= white_thresh:
        return -1
    if mean_color <= black_thresh:
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


def get_go_board(game_image, edge_top, edge_left, board_len_x, board_len_y):

    return game_image[edge_top:edge_top+board_len_y, edge_left:edge_left+board_len_x]



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
Get the color and the position of the current move
"""


def current_move_info(game_image):
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


# get sgf for image 13
# img = cv2.imread('../images/13.PNG')
#
#
# game_position = get_game_position(img, 49, 49, 94)
#
#
# f = open("out1.sgf", "w")
# f.write(get_sgf_txt(game_position))
# f.close()


# Get sgf for fox Go server images
# Still cannot identify current move yet
# Still cannot identify the black/white squares from the mouse
# img = cv2.imread('../images/12.PNG')
img = cv2.imread('E:/Go-game-record/Fox_Go_Server/images/2019-06-10 (3).png')
# print(np.shape(img))
board_img = get_go_board(img, 68, 531, 1865, 1865)
# cv2.imshow('image', board_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
game_position = get_game_position(board_img, 3, 3, 98)

# f = open("out3.sgf", "w")
f = open("E:/Go-game-record/Fox_Go_Server/2019-06-10 (3).sgf", "w")
f.write(get_sgf_txt(game_position))
f.close()


