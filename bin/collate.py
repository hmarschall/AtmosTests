#!/usr/bin/env python3
import os
import sys

if len(sys.argv) < 5:
    print("Usage: collate.py <prefix> <suffix> <filename> <dx's>", file=sys.stderr)
    sys.exit(1)

prefix = sys.argv[1]
suffix = sys.argv[2]
filename = sys.argv[3]
dxs = sys.argv[4:]

for dx in dxs:
    with open(os.path.join(prefix + dx + suffix, filename), 'r') as fin:
            print(dx + " " + fin.read(), end="")
