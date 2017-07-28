from ninjaopenfoam import BlockMesh, CutCellMesh, SlantedCellMesh, TerrainFollowingMesh
import ninjaopenfoam as ninja

import os

class Resting:
    def __init__(self, parallel, fast):
        meshNoOrography = BlockMesh('resting-mesh-noOrography', os.path.join('src/resting/mesh-noOrography'))

        meshBtf1000m = TerrainFollowingMesh('resting-mesh-btf-1000m', meshNoOrography, os.path.join('src/resting/mesh-btf-1000m'))
        meshBtf3000m = TerrainFollowingMesh('resting-mesh-btf-3000m', meshNoOrography, os.path.join('src/resting/mesh-btf-3000m'))

        createPatchDict = os.path.join('src/resting/createPatchDict')

        meshCutCell1000m = CutCellMesh('resting-mesh-cutCell-1000m', os.path.join('src/resting/mesh-cutCell-1000m'), createPatchDict)
        meshCutCell3000m = CutCellMesh('resting-mesh-cutCell-3000m', os.path.join('src/resting/mesh-cutCell-3000m'), createPatchDict)

        meshSlantedCell1000m = SlantedCellMesh('resting-mesh-slantedCell-1000m', meshNoOrography, os.path.join('src/resting/mesh-slantedCell-1000m'))
        meshSlantedCell3000m = SlantedCellMesh('resting-mesh-slantedCell-3000m', meshNoOrography, os.path.join('src/resting/mesh-slantedCell-3000m'))

        self.btf1000m = ninja.Resting('resting-btf-1000m', meshBtf1000m, parallel, fast)
        self.btf3000m = ninja.Resting('resting-btf-3000m', meshBtf3000m, parallel, fast)

        self.cutCell1000m = ninja.Resting('resting-cutCell-1000m', meshCutCell1000m, parallel, fast)
        self.cutCell3000m = ninja.Resting('resting-cutCell-3000m', meshCutCell3000m, parallel, fast)

        self.slantedCell1000m = ninja.Resting('resting-slantedCell-1000m', meshSlantedCell1000m, parallel, fast)
        self.slantedCell3000m = ninja.Resting('resting-slantedCell-3000m', meshSlantedCell3000m, parallel, fast)

        self.meshes = [
                meshNoOrography,
                meshBtf1000m, meshBtf3000m,
                meshCutCell1000m, meshCutCell3000m,
                meshSlantedCell1000m, meshSlantedCell3000m
        ]

    def addTo(self, build):
        build.addAll(self.meshes)
        build.add(self.btf1000m)
        build.add(self.btf3000m)
        build.add(self.cutCell1000m)
        build.add(self.cutCell3000m)
        build.add(self.slantedCell1000m)
        build.add(self.slantedCell3000m)
