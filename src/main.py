import SGF_parser
import out_parser
import os
import subprocess

"""
Take in an sgf file, output all the required statistics
"""


def analyze_sgf(sgf_file):
    lz_cmd_txt = SGF_parser.get_lz_cmd(sgf_file)

    command = ['../leela-zero-0.17-win64/leelaz.exe',
               '-g', '--noponder', '-t', '4', '-w', '../leela-zero-0.17-win64/network_226.gz',
               '--playouts', '10', '-r', '0']

    lz_out_txt = subprocess.run(command,
                                input=lz_cmd_txt.encode(),
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode()

    out_parser.print_win_rate(lz_cmd_txt, lz_out_txt, write_to_file=True)


analyze_sgf("../sgf-files/alphago_kejie_2.sgf")
