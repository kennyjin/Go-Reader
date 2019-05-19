"""
This module parses Leela Zero output to a csv file containing win rate and other information.
"""

import re


def get_text_blocks(lz_out_txt):
    blks = re.split(r"Thinking at most", lz_out_txt)
    return blks[1:]


def get_win_rate(txt_blk):
    x = re.search(r"V:\s{1,2}\d{1,3}\.\d\d%", txt_blk)
    end_index = x.group().find("%")
    win_rate = float(x.group()[3:end_index])  # get the number part
    return win_rate


def get_next_move(txt_blk):
    x = re.search(r"[A-T]\d{1,2} ->", txt_blk)
    end_index = x.group().find(" ")
    next_move = x.group()[0:end_index]
    return next_move


def get_variation(txt_blk):
    x = re.search(r"PV: .*\n", txt_blk)
    variation = x.group()[4:-1]
    return variation


def read_lz_out(lz_out_file):
    f = open(lz_out_file, "r")
    lz_out_txt = f.read()
    f.close()
    return lz_out_txt


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


def print_data(lz_out_txt, show_next_move=True, show_win_rate=True, show_variation=False):
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


def read_actual_moves(lz_cmd_txt):
    move_list = re.findall(r"play [BW] [A-T]\d{1,2}", lz_cmd_txt)
    color_list = []
    pos_list = []
    for i in range(len(move_list)):
        color_list.append(move_list[i][5])
        pos_list.append(move_list[i][7:])

    return color_list, pos_list


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






