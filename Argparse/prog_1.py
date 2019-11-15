#位置参数

import argparse

parser=argparse.ArgumentParser()
parser.add_argument("echo") #添加了add_argument()方法
args=parser.parse_args()

print(args.echo)

# $ python3 prog.py
# usage: prog.py [-h] echo
# prog.py: error: the following arguments are required: echo
# $ python3 prog.py --help
# usage: prog.py [-h] echo

# positional arguments:
#   echo

# optional arguments:
#   -h, --help  show this help message and exit
# $ python3 prog.py foo
# foo
