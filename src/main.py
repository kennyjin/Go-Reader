import SGF_parser
import out_parser
import subprocess
import stat_generater
import pandas as pd
import argparse

"""
Take in an sgf file, output all the required statistics
TODO Improvement: show analysis progress in real time
"""


def analyze_sgf(sgf_file, out_file):
    lz_cmd_txt = SGF_parser.get_lz_cmd(sgf_file)

    # command = ['../leela-zero-0.17-win64/leelaz.exe',
    #            '-g', '--noponder', '-t', '4', '-w', '../leela-zero-0.17-win64/network_226.gz',
    #            '--playouts', '1600', '-r', '0']

    command = ['../leela-zero-0.17-cpuonly-win64/leelaz.exe',
               '-g', '--noponder', '-t', '4', '-w', '../leela-zero-0.17-cpuonly-win64/weights/weight-157.gz',
               '--playouts', '16', '-r', '0']

    lz_out_txt = subprocess.run(command,
                                input=lz_cmd_txt.encode(),
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode()

    # print(lz_cmd_txt)

    # out_parser.print_win_rate(lz_cmd_txt, lz_out_txt, out_file=out_file)
    out_parser.print_data(lz_cmd_txt, lz_out_txt, out_file)


# sgf_input = "../sgf-files/alphago_teamgo.sgf"
# csv_output = "../csv_files/1600po/alphago_teamgo_1600po.csv"
# stat_output = "../csv_files/1600po/alphago_teamgo_stats.txt"
# csv_output = "../csv_files/16po/alphago_teamgo_16po.csv"
# stat_output = "../csv_files/16po/alphago_teamgo_stats.txt"

parser = argparse.ArgumentParser(description="Get the locations of the SGF file and 2 output files")
parser.add_argument("sgf_location", metavar="PATH_TO_SGF_FILE", type=str, help="the location of the sgf file to be analyzed")
parser.add_argument("csv_location", metavar="PATH_TO_CSV_OUTPUT", type=str, help="the location of the output csv file, file name is required")
parser.add_argument("stat_location", metavar="PATH_TO_STAT_OUTPUT", type=str, help="the location of the output stat file, file name is required")

# Get all the file names from the args
args = parser.parse_args()
sgf_input = args.sgf_location
csv_output = args.csv_location
stat_output = args.stat_location

# Start analyzing the sgf file
analyze_sgf(sgf_input, csv_output)
df = pd.read_csv(csv_output)
stat_generater.write_stats(df, stat_output, 5)


