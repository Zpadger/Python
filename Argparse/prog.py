#练习使用argparse
#基础

import argparse

parser=argparse.ArgumentParser()
parser.parse_args()

# $ python3 prog.py
# $ python3 prog.py --help
# usage: prog.py [-h]

# optional arguments:
#   -h, --help  show this help message and exit
# $ python3 prog.py --verbose
# usage: prog.py [-h]
# prog.py: error: unrecognized arguments: --verbose
# $ python3 prog.py foo
# usage: prog.py [-h]
# prog.py: error: unrecognized arguments: foo
