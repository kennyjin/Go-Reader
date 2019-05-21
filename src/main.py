import SGF_parser
import out_parser
import subprocess

"""
Take in an sgf file, output all the required statistics
TODO Improvement: show analysis progress in real time
"""


def analyze_sgf(sgf_file, out_file):
    lz_cmd_txt = SGF_parser.get_lz_cmd(sgf_file)

    command = ['../leela-zero-0.17-win64/leelaz.exe',
               '-g', '--noponder', '-t', '4', '-w', '../leela-zero-0.17-win64/network_226.gz',
               '--playouts', '10', '-r', '0']

    lz_out_txt = subprocess.run(command,
                                input=lz_cmd_txt.encode(),
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode()

    # print(lz_cmd_txt)

    # out_parser.print_win_rate(lz_cmd_txt, lz_out_txt, out_file=out_file)
    out_parser.print_data(lz_cmd_txt, lz_out_txt, out_file)


# analyze_sgf("../sgf-files/alphago_pairgo.sgf", "winrate.txt")
analyze_sgf("../sgf-files/alphago_kejie_3.sgf", "alphago_kejie_3.csv")
# analyze_sgf("../sgf-files/test_pass.sgf", "winrate.txt")
# analyze_sgf("E:/Go-game-record/vs-vincent/2.SGF", "winrate3.txt")
