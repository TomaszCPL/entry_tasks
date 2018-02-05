#!/usr/bin/env python
import re
import sys
import collections
from urllib.parse import urlparse

# REMARKS!!!
# I've had a problem with "today.log > report.csv" syntax. Right now the script supports "today.log report.csv".
# From what I know ">" is acted upon by shell, and duplicates the STDOUT stream (FD 1) to the second file.
# This happens before the command even runs, so I can't find a way to preserve this syntax and have the output
# file available in my script.

# I am not 100% happy with this solution. There are too many conditionals and loops.
# I feel it is a little overcomplicated.

inFile = sys.argv[1]
outFile = sys.argv[2]

invalidLines = 0

def regex(input):
    pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    match = re.search(pattern, input)
    if match:
        domain = '{url.netloc}{url.path}'.format(url=urlparse(input[match.start():match.end()])).rstrip('/')
        return domain

with open(inFile, 'r+') as input,open(outFile,'w+') as out:
    dict = {"invalid log lines":0}
    for line in input:
        if regex(line):
            if regex(line) in dict:
                dict[regex(line)] += 1
            else:
               dict[regex(line)] = 1
        else:
            dict["invalid log lines"] +=1

    sorted = collections.OrderedDict(sorted(dict.items(), key=lambda t: t[1], reverse=True))

    for k, v in sorted.items():
        out.write(str(k) + ':' + str(v) + '\n')