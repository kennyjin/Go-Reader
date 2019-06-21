# import out_parser
#
# f = open("../text-sample/sample_out2.txt")
# txt = f.read()
# blks = out_parser.get_text_blocks(txt)
# blk = blks[2]
# print(out_parser.get_next_moves(blk))

import re

"""
lz_all_next_moves might be in this form:
Q16 D16 Q4 D4 Q17 D17 Q3 R16 D3 C16 C4 R4
In this case 12 moves have been suggested. We could specify the number of moves being considered matched.
For example we want 2 moves being considered matched with Leela Zero. Then we return 'Q16 D16 '.
In the cases when num_moves is larger than the number of moves suggested by Leela Zero,
return the original lz_all_next_moves string.
"""


def get_lz_next_moves(lz_all_next_moves, num_moves=2):
    out_str = ""
    moves = re.split(r" ", lz_all_next_moves)
    if len(moves) >= num_moves:
        for i in range(num_moves):
            out_str += moves[i] + " "
    else:
        out_str = lz_all_next_moves
    return out_str


next_moves_str = "Q16 D16 Q4 D4 Q17 D17 Q3 R16 D3 C16 C4 R4 "
print(get_lz_next_moves(next_moves_str, num_moves=11))
