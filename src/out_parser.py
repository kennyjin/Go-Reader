"""
This module parses Leela Zero output to a csv file containing win rate and other information.
"""

import re
# import csv
import pandas as pd


"""
Returns text blocks from Leela Zero output.
"""


def get_text_blocks(lz_out_txt):
    blks = re.split(r"Thinking at most", lz_out_txt)
    return blks[1:]


"""
Returns win rate from a text block
"""


def get_win_rate(txt_blk):
    x = re.search(r"V:\s{1,2}\d{1,3}\.\d\d%", txt_blk)
    end_index = x.group().find("%")
    win_rate = float(x.group()[3:end_index])  # get the number part
    return win_rate


"""
Returns the 'best' next move suggested by Leela Zero
"""


def get_next_move(txt_blk):
    x = re.search(r"[A-T]\d{1,2} ->", txt_blk)
    end_index = x.group().find(" ")
    next_move = x.group()[0:end_index]
    return next_move


"""
Returns all the next moves suggested by Leela Zero
"""


def get_next_move_list(txt_blk):
    next_move_list = re.findall(r"([A-T]\d{1,2}) ->", txt_blk)
    return next_move_list


"""
Convert the next move list to a space separated string
"""


def get_next_moves(txt_blk):
    next_move_list = get_next_move_list(txt_blk)
    out_str = ""
    for i in range(len(next_move_list)):
        out_str += next_move_list[i]
        out_str += " "
    return out_str


"""
Returns the variation suggested by Leela Zero
"""


def get_variation(txt_blk):
    x = re.search(r"PV: .*\n", txt_blk)
    variation = x.group()[4:-1]
    return variation


"""
Reads Leela Zero output file and generate output text
"""


def read_lz_out(lz_out_file):
    f = open(lz_out_file, "r")
    lz_out_txt = f.read()
    f.close()
    return lz_out_txt


"""
Print next move, win rate and variation from Leela Zero output file
"""


def print_data_from_file(lz_out_file, show_next_move=True, show_win_rate=True, show_variation=False):
    lz_out_txt = read_lz_out(lz_out_file)
    blks = get_text_blocks(lz_out_txt)
    print(len(blks))
    for i in range(len(blks)):
        outstr = ""
        if show_next_move:
            outstr += get_next_move(blks[i])
        if show_win_rate:
            outstr += " " + "{0:.2f}".format(get_win_rate(blks[i]))
        if show_variation:
            outstr += " " + get_variation(blks[i])
        print(outstr)


"""
Print next move, win rate and variation from Leela Zero output text(string)
This just prints raw win rate without modification. 
"""


def print_data_simple(lz_out_txt, show_next_move=True, show_win_rate=True, show_variation=False):
    blks = get_text_blocks(lz_out_txt)
    print(len(blks))
    for i in range(len(blks)):
        outstr = ""
        if show_next_move:
            outstr += get_next_move(blks[i])
        if show_win_rate:
            outstr += " " + "{0:.2f}".format(get_win_rate(blks[i]))
        if show_variation:
            outstr += " " + get_variation(blks[i])
        print(outstr)


"""
Read actual moves from the Leela Zero command file.
"""


def read_actual_moves_from_file(lz_cmd_file):
    f = open(lz_cmd_file, "r")
    lz_cmd_txt = f.read()
    f.close()
    move_list = re.findall(r"play [BW] [A-T]\d{1,2}", lz_cmd_txt)
    color_list = []
    pos_list = []
    for i in range(len(move_list)):
        color_list.append(move_list[i][5])
        pos_list.append(move_list[i][7:])
    
    return color_list, pos_list


"""
Read actual moves from the Leela Zero command text.
"""


def read_actual_moves(lz_cmd_txt):
    move_list = re.findall(r"play [BW] (?:(?:[A-T]\d{1,2})|(?:pass))", lz_cmd_txt)
    color_list = []
    pos_list = []
    for i in range(len(move_list)):
        # print(move_list[i])
        color_list.append(move_list[i][5])
        pos_list.append(move_list[i][7:])

    return color_list, pos_list


"""
Print win rate from Leela Zero command and output file
"""


def print_win_rate_from_file(lz_cmd_file, lz_out_file, black=True, show_move_number=True):
    color_list, pos_list = read_actual_moves_from_file(lz_cmd_file)
    lz_out_txt = read_lz_out(lz_out_file)
    blks = get_text_blocks(lz_out_txt)
    print(len(blks))
    for i in range(len(blks)):
        if black:
            if color_list[i] == "B":
                # Keep 2 decimal places
                outstr = "{0:.2f}".format(get_win_rate(blks[i]))
            else:
                outstr = "{0:.2f}".format(100.00 - get_win_rate(blks[i]))
        else:
            if color_list[i] == "W":
                outstr = "{0:.2f}".format(get_win_rate(blks[i]))
            else:
                outstr = "{0:.2f}".format(100.00 - get_win_rate(blks[i]))
        if show_move_number:
            outstr = str(i) + " " + outstr
        print(outstr)


"""
Print win rate from Leela Zero command and output texts. With modification regarding color.
"""


def print_win_rate(lz_cmd_txt, lz_out_txt, black=True, show_move_number=True,
                   out_file=None, show_on_console=False):
    color_list, pos_list = read_actual_moves(lz_cmd_txt)
    blks = get_text_blocks(lz_out_txt)
    # print(len(blks))
    outstr_full = ""
    for i in range(len(blks)):
        if black:
            if color_list[i] == "B":
                # Keep 2 decimal places
                outstr = "{0:.2f}".format(get_win_rate(blks[i]))
            else:
                outstr = "{0:.2f}".format(100.00 - get_win_rate(blks[i]))
        else:
            if color_list[i] == "W":
                outstr = "{0:.2f}".format(get_win_rate(blks[i]))
            else:
                outstr = "{0:.2f}".format(100.00 - get_win_rate(blks[i]))
        if show_move_number:
            outstr = str(i) + " " + outstr
        # print(outstr)
        outstr_full += outstr + "\n"
    if show_on_console:
        print(outstr_full)
    if out_file is not None:
        f = open(out_file, "w")
        f.write(outstr_full)


"""
Prints all the statistics to a csv file
"""


def print_data(lz_cmd_txt, lz_out_txt, out_file):
    color_list, actual_next_list = read_actual_moves(lz_cmd_txt)
    blks = get_text_blocks(lz_out_txt)
    move_num_list = []
    win_rate_list_b = []
    win_rate_list_w = []
    lz_next_list = []
    variation_list = []
    lz_next_moves_list = []  # All possible next moves suggested by Leela Zero
    for i in range(len(blks)):
        move_num_list.append(str(i))
        if color_list[i] == "B":
            # Keep 2 decimal places
            win_rate_list_b.append("{0:.2f}".format(get_win_rate(blks[i])))
            win_rate_list_w.append("{0:.2f}".format(100.00 - get_win_rate(blks[i])))
        else:
            # Keep 2 decimal places
            win_rate_list_b.append("{0:.2f}".format(100.00 - get_win_rate(blks[i])))
            win_rate_list_w.append("{0:.2f}".format(get_win_rate(blks[i])))
        lz_next_list.append(get_next_move(blks[i]))
        variation_list.append(get_variation(blks[i]))
        lz_next_moves_list.append(get_next_moves(blks[i]))

    # Write to csv file, might be better using pandas
    data = {"move_num": move_num_list, "color_next": color_list, "winrate_B": win_rate_list_b,
            "winrate_W": win_rate_list_w, "LZ_next_move": lz_next_list, "variation": variation_list,
            "actual_next_move": actual_next_list, "LZ_all_next_moves": lz_next_moves_list}
    df = pd.DataFrame(data)
    df.to_csv(out_file, index=False)

    # mapped = zip(move_num_list, color_list, win_rate_list_b, win_rate_list_w, lz_next_list,
    #              variation_list, actual_next_list)
    # mapped = list(mapped)
    #
    #
    # with open(out_file, "w") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["move_num", "color_next", "winrate_B", "winrate_W", "LZ_next_move",
    #                      "variation", "actual_next_move"])
    #     writer.writerows(mapped)


"""
Return a data frame containing the raw statistics
"""


def get_raw_stats(lz_cmd_txt, lz_out_txt):
    color_list, actual_next_list = read_actual_moves(lz_cmd_txt)
    blks = get_text_blocks(lz_out_txt)
    move_num_list = []
    win_rate_list_b = []
    win_rate_list_w = []
    lz_next_list = []
    variation_list = []
    lz_next_moves_list = []  # All possible next moves suggested by Leela Zero
    for i in range(len(blks)):
        move_num_list.append(str(i))
        if color_list[i] == "B":
            # Keep 2 decimal places
            win_rate_list_b.append("{0:.2f}".format(get_win_rate(blks[i])))
            win_rate_list_w.append("{0:.2f}".format(100.00 - get_win_rate(blks[i])))
        else:
            # Keep 2 decimal places
            win_rate_list_b.append("{0:.2f}".format(100.00 - get_win_rate(blks[i])))
            win_rate_list_w.append("{0:.2f}".format(get_win_rate(blks[i])))
        lz_next_list.append(get_next_move(blks[i]))
        variation_list.append(get_variation(blks[i]))
        lz_next_moves_list.append(get_next_moves(blks[i]))

    # Write to csv file, might be better using pandas
    data = {"move_num": move_num_list, "color_next": color_list, "winrate_B": win_rate_list_b,
            "winrate_W": win_rate_list_w, "LZ_next_move": lz_next_list, "variation": variation_list,
            "actual_next_move": actual_next_list, "LZ_all_next_moves": lz_next_moves_list}
    df = pd.DataFrame(data)
    return df



