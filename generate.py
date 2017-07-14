#!/usr/bin/python3

import errno
import ninja.gen
import ninja.model
import os

if __name__ == '__main__':
    build = ninja.model.Build()

    build.add(ninja.model.BlockMesh('schaerAdvect-mesh-noOrography', os.path.join('src', 'schaerAdvect', 'mesh-noOrography')))

    build.write()
