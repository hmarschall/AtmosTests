from ninjaopenfoam import BlockMesh, CutCellMesh, SlantedCellMesh, TerrainFollowingMesh

import os

class Resting:
    def __init__(self, parallel, fast):
        meshNoOrography = BlockMesh('resting-mesh-noOrography', os.path.join('src/resting/mesh-noOrography'))

        meshBtf = TerrainFollowingMesh('resting-mesh-btf', meshNoOrography, os.path.join('src/resting/mesh-btf'))

        createPatchDict = os.path.join('src/resting/createPatchDict')
        meshCutCell = CutCellMesh('resting-mesh-cutCell', os.path.join('src/resting/mesh-cutCell'), createPatchDict)

        meshSlantedCell = SlantedCellMesh('resting-mesh-slantedCell', meshNoOrography, os.path.join('src/resting/mesh-slantedCell'))

        self.meshes = [meshNoOrography, meshBtf, meshCutCell, meshSlantedCell]

    def addTo(self, build):
        build.addAll(self.meshes)
