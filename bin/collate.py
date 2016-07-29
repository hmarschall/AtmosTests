#!/usr/bin/env python3
import os
import sys

if len(sys.argv) < 4:
    print("Usage: collate.py <prefix> <suffix> <dx's>", file=sys.stderr)
    sys.exit(1)

prefix = sys.argv[1]
suffix = sys.argv[2]
dxs = sys.argv[3:]

for dx in dxs:
    with open(os.path.join(prefix + dx, suffix), 'r') as fin:
            print(dx + " " + fin.read(), end="")
