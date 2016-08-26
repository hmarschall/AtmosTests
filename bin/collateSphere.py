#!/usr/bin/env python3
import os
import sys

if len(sys.argv) < 4:
    print("Usage: collateSphere.py <prefix> <suffix> <NGRIDs>", file=sys.stderr)
    sys.exit(1)

prefix = sys.argv[1]
suffix = sys.argv[2]
ngrids = sys.argv[3:]

for ngrid in ngrids:
    with open(os.path.join(prefix + ngrid, suffix), 'r') as fin:
        with open(os.path.join(prefix + ngrid, "meshAverageEquatorialSpacing.txt"), 'r') as dxf:
            dx = dxf.read()[:-1]
            print(dx + " " + fin.read(), end="")
