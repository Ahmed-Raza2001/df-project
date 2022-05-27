import re
import argparse

parser=argparse.ArgumentParser(description='compare regex rule with a file')
parser.add_argument('file',help='file to run regex against')
parser.add_argument('-r',help='regex rule to match for')
arg=parser.parse_args()
content=open(arg.file,'r').read()
regex=re.compile(arg.r)
print(regex.search(content))
