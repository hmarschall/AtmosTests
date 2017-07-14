#!/usr/bin/python3

import errno
import ninja.gen
import ninja.model
import os

if __name__ == '__main__':
    build = ninja.model.Build()

    meshNoOrography = ninja.model.BlockMesh(
            'schaerAdvect-mesh-noOrography',
            os.path.join('src', 'schaerAdvect', 'mesh-noOrography'))

    meshBtf = ninja.model.TerrainFollowingMesh(
            'schaerAdvect-mesh-btf',
            meshNoOrography,
            os.path.join('src', 'schaerAdvect', 'mesh-btf'))

    build.add(meshNoOrography)
    build.add(meshBtf)

    build.write()
