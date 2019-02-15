#!/usr/bin/python

def read_codes():
    key = None
    lineA = None
    for line in open('dump.log'):
        if line.startswith('QR:'):
            key = line.split()[-1]
        elif key and not lineA:
            lineA = line
        elif key and lineA:
            yield (key, (lineA, line))
            key, lineA = None, None

codes = {}
for k, v in read_codes():
    if k in codes:
        print k, v
    else:
        codes[k] = v
