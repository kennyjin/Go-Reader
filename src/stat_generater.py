"""
This module generate new statistics using the raw statistics.
New statistics include:
win rate differences for each move. (For black and white, respectively.)
The mean and the variances for the win rate differences.
Matching rate. (Exactly match or match one of the options)
"""

import pandas as pd
import numpy as np


"""
Take in a data frame and output win rate differences (in black's perspective)
"""


def get_win_rate_diff(df):
    win_rate_black = df['winrate_B'].to_numpy()
    win_rate_diff = np.array([])
    for i in range(len(win_rate_black) - 1):
        win_rate_diff = np.append(win_rate_diff, win_rate_black[i + 1] - win_rate_black[i])
    return win_rate_diff


"""
Get the color of the move being played
"""


def get_move_color(df):
    move_color = df['color_next'].to_numpy()
    move_color = move_color[:-1]  # At this time we don't analyze the last move
    return move_color


"""
Get the color of the move being played without removing the last move
"""


def get_move_color_full(df):
    move_color = df['color_next'].to_numpy()
    return move_color

"""



Get the win rate difference of black
"""


def get_black_diff(df):
    black_diff = np.empty([0, 2])
    win_rate_diff = get_win_rate_diff(df)
    move_color = get_move_color(df)
    for i in range(len(win_rate_diff)):
        if move_color[i] == "B":
            black_diff = np.append(black_diff, [[i + 1, win_rate_diff[i]]], axis=0)
    black_diff_df = pd.DataFrame(data=black_diff[0:, 0:], columns=["move_num", "winrate_diff"])
    black_diff_df = black_diff_df.astype({"move_num": "int64"})
    return black_diff_df


"""
Get the win rate difference of white
"""


def get_white_diff(df):
    white_diff = np.empty([0, 2])
    win_rate_diff = get_win_rate_diff(df)
    move_color = get_move_color(df)
    for i in range(len(win_rate_diff)):
        if move_color[i] == "W":
            white_diff = np.append(white_diff, [[i + 1, - win_rate_diff[i]]], axis=0)
    white_diff_df = pd.DataFrame(data=white_diff[0:, 0:], columns=["move_num", "winrate_diff"])
    white_diff_df = white_diff_df.astype({"move_num": "int64"})
    return white_diff_df


"""
Returns the matched (exactly) list (with Leela Zero) of each player
1 means this move matches Leela Zero next move, 0 otherwise
"""


def get_matched_list_exact(df):
    matched = df['LZ_next_move'] == df['actual_next_move']
    matched = matched.astype('int64')  # could just use astype(int)
    return matched


"""
Returns the matched list (with Leela Zero) of each player
1 means this move matches Leela Zero next move, 0 otherwise
"""


def get_matched_list(df):
    matched = np.array([])
    for i in range(len(df['LZ_next_move'])):
        matched = np.append(matched, df['actual_next_move'][i] + " " in df['LZ_all_next_moves'][i])
    matched = pd.DataFrame(data=matched[0:])
    matched = matched.astype('int64')
    return matched


"""
Return the matching rate of a player, in a move range (e.g: move 1 to 60)
"""


def get_matching_rate(df, color, range_low, range_high, exact_match=False):
    if exact_match:
        matched = get_matched_list_exact(df)
    else:
        matched = get_matched_list(df)
    move_color = get_move_color_full(df)
    total_move_num = 0
    matched_move_num = 0
    for i in range(range_low - 1, range_high):
        if move_color[i] == color:
            total_move_num += 1
            matched_move_num += matched.iloc[i]
    return float(matched_move_num) / float(total_move_num)
    #return float(total_move_num)








dtf = pd.read_csv("../csv_files/alphago_kejie_3.csv")

#print(get_white_diff(df)["move_num"])
#print(get_black_diff(df))

df_black = get_black_diff(dtf)
df_white = get_white_diff(dtf)

# print(df_black.loc[:, "winrate_diff"].mean())
# print(df_black.loc[:, "winrate_diff"].var())
# print(df_white.loc[:, "winrate_diff"].mean())
# print(df_white.loc[:, "winrate_diff"].var())
#
# print(df_black.nsmallest(5, "winrate_diff"))
# print(df_white.nsmallest(5, "winrate_diff"))

#print(get_matching_rate_exact(df))
#print(get_matched_list(df))

#print(type(df['LZ_all_next_moves'][0]))

#print(type(df['actual_next_move'][0]))

print(get_matching_rate(df=dtf, color="B", range_low=1, range_high=209))
print(get_matching_rate(df=dtf, color="W", range_low=1, range_high=209))

print(get_matching_rate(df=dtf, color="B", range_low=1, range_high=209, exact_match=True))
print(get_matching_rate(df=dtf, color="W", range_low=1, range_high=209, exact_match=True))