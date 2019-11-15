#位置参数

import argparse

parser=argparse.ArgumentParser()
parser.add_argument("echo") #添加了add_argument()方法
args=parser.parse_args()

print(args.echo)

# python prog_1.py
# usage: prog_1.py [-h] echo
# prog_1.py: error: the following arguments are required: echo

# python prog_1.py --help
# usage: prog_1.py [-h] echo
#
# positional arguments:
#   echo
#
# optional arguments:
#   -h, --help  show this help message and exit

#  python prog_1.py foo
# foo
