"""
This module parses SGF files to input commands for LeelaZero
"""

"""
Parse sgf coordinates to LeelaZero coordinates.
For example, 'cp' --> 'C4'

@param sgf_coor: The coordinates of a Go stone in an SGF file. Should be 2 characters from a to s.
@return: The new coordinates that could be used by LeelaZero.

"""
def parseCoordinates(sgf_coor):
	x_coor = sgf_coor[0]
	y_coor = sgf_coor[1]
	# Check if x_coor and y_coor are in the range of a to s
	if x_coor
