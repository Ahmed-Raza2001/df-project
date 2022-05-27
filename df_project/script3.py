import yara
import argparse

parser=argparse.ArgumentParser(description='compare YARA signs with a file')
parser.add_argument('file',help='the file from which signatures are matched')
parser.add_argument('-r',help='yara rule')
arg=parser.parse_args()
rules=yara.compile(filepath=arg.r)
print(rules.match(arg.file))
