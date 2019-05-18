"""
This module parses Leela Zero output to a csv file containing winrate and other information.
"""

import re

def getTextBlocks(lz_out_txt):
    blks = re.split(r"Thinking at most", lz_out_txt)
    return blks[1:]

def getWinRate(txt_blk):
    x = re.search(r"V:\s{1,2}\d{1,3}\.\d\d%",txt_blk)
    end_index = x.group().find("%")
    winrate = (float)(x.group()[3:end_index]) # get the number part
    return winrate

def getNextMove(txt_blk):
    x = re.search(r"[A-T]{1}\d{1,2} ->", txt_blk)
    end_index = x.group().find(" ")
    nextMove = x.group()[0:end_index]
    return nextMove

def getVariation(txt_blk):
    x = re.search(r"PV: .*\n", txt_blk)
    variation = x.group()[4:-1]
    return variation

def readLZout(lz_out_file):
    f = open(lz_out_file, "r")
    lz_out_txt = f.read()
    f.close()
    return lz_out_txt

def printData(lz_out_file, showNextMove = True, showWinRate = True, showVariation = False):
    lz_out_txt = readLZout(lz_out_file)
    blks = getTextBlocks(lz_out_txt)
    print(len(blks))
    for i in range(len(blks)):
        outstr = ""
        if showNextMove:
            outstr += getNextMove(blks[i])
        if showWinRate:
            outstr += " " + (str)(getWinRate(blks[i]))
        if showVariation:
            outstr += " " + getVariation(blks[i])
        print(outstr)


def readActualMoves(lz_cmd_file):
    f = open(lz_cmd_file, "r")
    lz_cmd_txt = f.read()
    f.close()
    move_list = re.findall(r"play [BW]{1} [A-T]{1}\d{1,2}", lz_cmd_txt)
    color_list = []
    pos_list = []
    for i in range(len(move_list)):
      color_list.append(move_list[i][5])
      pos_list.append(move_list[i][7:])
    
    return color_list, pos_list


# TODO keep 2 decimal places
def printWinRate(lz_cmd_file, lz_out_file, Black = True):
    color_list, pos_list = readActualMoves(lz_cmd_file)
    lz_out_txt = readLZout(lz_out_file)
    blks = getTextBlocks(lz_out_txt)
    print(len(blks))
    for i in range(len(blks)):
        outstr = ""
        if Black:
            if color_list[i] == "B":
                outstr += " " + (str)(getWinRate(blks[i]))
            else:
                outstr += " " + (str)(100 - getWinRate(blks[i]))
        else:
            if color_list[i] == "W":
                outstr += " " + (str)(getWinRate(blks[i]))
            else:
                outstr += " " + (str)(100 - getWinRate(blks[i]))
        print(outstr)







