import out_parser

f = open("../text-sample/sample_out2.txt")
txt = f.read()
blks = out_parser.get_text_blocks(txt)
blk = blks[2]
print(out_parser.get_next_moves(blk))