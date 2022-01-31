#! /usr/bin/python3

import re
import sys

f = open('words.txt')
data = f.read()

p = re.compile(sys.argv[1]) 
candidates = p.findall(data)

print(*candidates, sep='\n')
