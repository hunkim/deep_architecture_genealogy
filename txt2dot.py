#!/usr/bin/python3
# usage:
#    python3 txt2dot.py 'Neural Net Arch Genealogy.txt' > Neural_Net_Arch_Genealogy.dot
# then, if graphviz is installed in your system:
#    dot -Tsvg Neural_Net_Arch_Genealogy.dot > Neural_Net_Arch_Genealogy.svg

import re, fileinput

head= '''
digraph "Neural_Net_Arch_Genealogy" {
    rankdir = LR;
    overlap = scale;
'''

tail = '}\n'

ancestors = [''] * 9

print(head)
for line in fileinput.input():
    name = re.match('^(\t*)(\S.*\S)', line)
    n = len(name.group(1))
    m2 = re.match('\[(\w[-\w\s]+)(.*?)\s*\]', name.group(2))
    if m2:
        name = m2.group(1)
    else:
        name = name.group(2)
    if n>0:
        print('    "{}" -> "{}";'.format(ancestors[n-1], name))
    ancestors[n] = name

print(tail)

