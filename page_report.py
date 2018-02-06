#!/usr/bin/env python
import re
import sys
import collections
from urllib.parse import urlparse

# REMARKS!!!
# I am not 100% happy with this solution. There are too many conditionals and loops.
# I feel it is a little overcomplicated.

inFile = sys.argv[1]

def regex(input):
    pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    match = re.search(pattern, input)
    if match:
        domain = '{url.netloc}{url.path}'.format(url=urlparse(input[match.start():match.end()])).rstrip('/')
        return domain

with open(inFile, 'r+') as input:
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
        print(str(k) + ':' + str(v) + '\n')
