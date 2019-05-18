"""
This module parses SGF files to input commands for Leela Zero
"""

import re

"""
Parse sgf coordinates to Leela Zero coordinates.
For example, 'cp' --> 'C4'

@param sgf_coor: The coordinates of a Go stone in an SGF file. Should be 2 characters from a to s.
@return: The new coordinates that could be used by Leela Zero.

"""
def parseCoordinates(sgf_coor):
    if sgf_coor == "":
        return "pass"
    x_coor = sgf_coor[0]
    y_coor = sgf_coor[1]
    x_new = x_coor
    y_new = y_coor
    # Check if x_coor is in the range of a to h
    if ord(x_coor) in range(ord('a'), ord('h') + 1):
        x_new = x_coor.upper()
    # Check if x_coor is in the range of i to s
    # If so, change "i" to "J", ... , "s" to "T"
    elif ord(x_coor) in range(ord('i'), ord('s') + 1):
        x_new = chr(ord(x_coor.upper()) + 1)
    else:
        x_new = None
    diff = ord('a') - 1
    # ord(y_coor) - diff transforms a -> s to 1 -> 19
    # then we transform 1 -> 19 to 19 -> 1
    y_new = 20 - (ord(y_coor) - diff)
    return x_new + str(y_new)


"""
Parse sgf moves into Leela Zero commands
@param: the move in the File. e.g: ;B[qq] or ;W[qd]
@return: the command for Leela Zero. 
e.g: 
lz-genmove_analyze B
undo
play B R3

"""
def parseMove(str_move):
    color = str_move[1]
    # Move position (coordinates)
    move_pos = parseCoordinates(str_move[3:5])
    # Leela Zero command
    cmd_lz = "lz-genmove_analyze" + " " + color + "\n" + "undo\n" + "play"\
    + " " + color + " " + move_pos
    return cmd_lz


"""
Parse main branch of sgf and generate commands
This is basically put all commands together
TODO: This assumes that the sgf file only contains the main branch. More work is needed.
@param: the sgf text.
@return: the string of Leela Zero commands

"""
def parseMainBranch(sgf_txt):
    cmd_all = ""
    # Include the possibility of passing moves
    move_list = re.findall(";[BW]\[([a-s]{2})?\]", sgf_txt)
    for str_move in move_list:
        cmd_lz = parseMove(str_move)
        cmd_all += cmd_lz + "\n"
    return cmd_all


"""
Write Leela Zero commands to a txt file.
"""
def writeLZcmd(sgf_file, out_file):
    f = open(sgf_file, 'r')
    sgf_txt = f.read()
    f.close()
    out_str = parseMainBranch(sgf_txt)
    f = open(out_file, 'w')
    f.write(out_str)


"""
Return the main branch text from some sgf text
"""
# TODO matches seem inapropriate
def getMainBranch(sgf_txt):
    # Look for the first ")"
    #x = re.search(r"\[[\s\S]*\]\)", sgf_txt)
    x = re.search(r"\]\)", sgf_txt)
    pos = x.span()[1]
    sgf_txt_new = sgf_txt[0:pos]
    # Get rid of all the "("
    sgf_txt_new = re.sub(r"(\()(;[BW])", r"\2", sgf_txt_new)
    if sgf_txt_new[0] != "(":
        sgf_txt_new = "(" + sgf_txt_new
    return sgf_txt_new





