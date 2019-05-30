import SGF_parser
import out_parser
import subprocess
import stat_generater
import pandas as pd

"""
Take in an sgf file, output all the required statistics
TODO Improvement: show analysis progress in real time
"""


def analyze_sgf(sgf_file, out_file):
    lz_cmd_txt = SGF_parser.get_lz_cmd(sgf_file)

    command = ['../leela-zero-0.17-win64/leelaz.exe',
               '-g', '--noponder', '-t', '4', '-w', '../leela-zero-0.17-win64/network_226.gz',
               '--playouts', '1600', '-r', '0']

    lz_out_txt = subprocess.run(command,
                                input=lz_cmd_txt.encode(),
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode()

    # print(lz_cmd_txt)

    # out_parser.print_win_rate(lz_cmd_txt, lz_out_txt, out_file=out_file)
    out_parser.print_data(lz_cmd_txt, lz_out_txt, out_file)


sgf_input = "../sgf-files/alphago_teamgo.sgf"
csv_output = "../csv_files/1600po/alphago_teamgo_1600po.csv"
stat_output = "../csv_files/1600po/alphago_teamgo_stats.txt"

analyze_sgf(sgf_input, csv_output)
df = pd.read_csv(csv_output)
stat_generater.write_stats(df, stat_output, 5)

