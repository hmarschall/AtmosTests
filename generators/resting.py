from ninjaopenfoam import BlockMesh, CutCellMesh, SlantedCellMesh, TerrainFollowingMesh
import ninjaopenfoam as ninja

import os

class Resting:
    def __init__(self, parallel, fast):
        meshNoOrography = BlockMesh('resting-mesh-noOrography', os.path.join('src/resting/mesh-noOrography'))

        meshBtf1000m = TerrainFollowingMesh('resting-mesh-btf-1000m', meshNoOrography, os.path.join('src/resting/mesh-btf-1000m'))
        meshBtf2000m = TerrainFollowingMesh('resting-mesh-btf-2000m', meshNoOrography, os.path.join('src/resting/mesh-btf-2000m'))
        meshBtf3000m = TerrainFollowingMesh('resting-mesh-btf-3000m', meshNoOrography, os.path.join('src/resting/mesh-btf-3000m'))

        meshSleve1000m = TerrainFollowingMesh('resting-mesh-sleve-1000m', meshNoOrography, os.path.join('src/resting/mesh-sleve-1000m'))
        meshSleve2000m = TerrainFollowingMesh('resting-mesh-sleve-2000m', meshNoOrography, os.path.join('src/resting/mesh-sleve-2000m'))
        meshSleve3000m = TerrainFollowingMesh('resting-mesh-sleve-3000m', meshNoOrography, os.path.join('src/resting/mesh-sleve-3000m'))

        createPatchDict = os.path.join('src/resting/createPatchDict')

        meshCutCell1000m = CutCellMesh('resting-mesh-cutCell-1000m', os.path.join('src/resting/mesh-cutCell-1000m'), createPatchDict)
        meshCutCell2000m = CutCellMesh('resting-mesh-cutCell-2000m', os.path.join('src/resting/mesh-cutCell-2000m'), createPatchDict)
        meshCutCell3000m = CutCellMesh('resting-mesh-cutCell-3000m', os.path.join('src/resting/mesh-cutCell-3000m'), createPatchDict)

        meshSlantedCell1000m = SlantedCellMesh('resting-mesh-slantedCell-1000m', meshNoOrography, os.path.join('src/resting/mesh-slantedCell-1000m'))
        meshSlantedCell2000m = SlantedCellMesh('resting-mesh-slantedCell-2000m', meshNoOrography, os.path.join('src/resting/mesh-slantedCell-2000m'))
        meshSlantedCell3000m = SlantedCellMesh('resting-mesh-slantedCell-3000m', meshNoOrography, os.path.join('src/resting/mesh-slantedCell-3000m'))

        self.btf1000mLinearUpwind = ninja.Resting('resting-btf-1000m-linearUpwind', meshBtf1000m, os.path.join('src/resting/linearUpwind'), parallel, fast)
        self.btf2000mLinearUpwind = ninja.Resting('resting-btf-2000m-linearUpwind', meshBtf2000m, os.path.join('src/resting/linearUpwind'), parallel, fast)
        self.btf3000mLinearUpwind = ninja.Resting('resting-btf-3000m-linearUpwind', meshBtf3000m, os.path.join('src/resting/linearUpwind'), parallel, fast)

        self.btf1000mCubicFit = ninja.Resting('resting-btf-1000m-cubicFit', meshBtf1000m, os.path.join('src/resting/cubicFit'), parallel, fast)
        self.btf2000mCubicFit = ninja.Resting('resting-btf-2000m-cubicFit', meshBtf2000m, os.path.join('src/resting/cubicFit'), parallel, fast)
        self.btf3000mCubicFit = ninja.Resting('resting-btf-3000m-cubicFit', meshBtf3000m, os.path.join('src/resting/cubicFit'), parallel, fast)

        self.sleve1000mLinearUpwind = ninja.Resting('resting-sleve-1000m-linearUpwind', meshSleve1000m, os.path.join('src/resting/linearUpwind'), parallel, fast)
        self.sleve2000mLinearUpwind = ninja.Resting('resting-sleve-2000m-linearUpwind', meshSleve2000m, os.path.join('src/resting/linearUpwind'), parallel, fast)
        self.sleve3000mLinearUpwind = ninja.Resting('resting-sleve-3000m-linearUpwind', meshSleve3000m, os.path.join('src/resting/linearUpwind'), parallel, fast)

        self.sleve1000mCubicFit = ninja.Resting('resting-sleve-1000m-cubicFit', meshSleve1000m, os.path.join('src/resting/cubicFit'), parallel, fast)
        self.sleve2000mCubicFit = ninja.Resting('resting-sleve-2000m-cubicFit', meshSleve2000m, os.path.join('src/resting/cubicFit'), parallel, fast)
        self.sleve3000mCubicFit = ninja.Resting('resting-sleve-3000m-cubicFit', meshSleve3000m, os.path.join('src/resting/cubicFit'), parallel, fast)

        self.cutCell1000mLinearUpwind = ninja.Resting('resting-cutCell-1000m-linearUpwind', meshCutCell1000m, os.path.join('src/resting/linearUpwind'), parallel, fast)
        self.cutCell2000mLinearUpwind = ninja.Resting('resting-cutCell-2000m-linearUpwind', meshCutCell2000m, os.path.join('src/resting/linearUpwind'), parallel, fast)
        self.cutCell3000mLinearUpwind = ninja.Resting('resting-cutCell-3000m-linearUpwind', meshCutCell3000m, os.path.join('src/resting/linearUpwind'), parallel, fast)

        self.cutCell1000mCubicFit = ninja.Resting('resting-cutCell-1000m-cubicFit', meshCutCell1000m, os.path.join('src/resting/cubicFit'), parallel, fast)
        self.cutCell2000mCubicFit = ninja.Resting('resting-cutCell-2000m-cubicFit', meshCutCell2000m, os.path.join('src/resting/cubicFit'), parallel, fast)
        self.cutCell3000mCubicFit = ninja.Resting('resting-cutCell-3000m-cubicFit', meshCutCell3000m, os.path.join('src/resting/cubicFit'), parallel, fast)

        self.slantedCell1000mLinearUpwind = ninja.Resting('resting-slantedCell-1000m-linearUpwind', meshSlantedCell1000m, os.path.join('src/resting/linearUpwind'), parallel, fast)
        self.slantedCell2000mLinearUpwind = ninja.Resting('resting-slantedCell-2000m-linearUpwind', meshSlantedCell2000m, os.path.join('src/resting/linearUpwind'), parallel, fast)
        self.slantedCell3000mLinearUpwind = ninja.Resting('resting-slantedCell-3000m-linearUpwind', meshSlantedCell3000m, os.path.join('src/resting/linearUpwind'), parallel, fast)

        self.slantedCell1000mCubicFit = ninja.Resting('resting-slantedCell-1000m-cubicFit', meshSlantedCell1000m, os.path.join('src/resting/cubicFit'), parallel, fast)
        self.slantedCell2000mCubicFit = ninja.Resting('resting-slantedCell-2000m-cubicFit', meshSlantedCell2000m, os.path.join('src/resting/cubicFit'), parallel, fast)
        self.slantedCell3000mCubicFit = ninja.Resting('resting-slantedCell-3000m-cubicFit', meshSlantedCell3000m, os.path.join('src/resting/cubicFit'), parallel, fast)

        self.meshes = [
                meshNoOrography,
                meshBtf1000m, meshBtf2000m, meshBtf3000m,
                meshSleve1000m, meshSleve2000m, meshSleve3000m,
                meshCutCell1000m, meshCutCell2000m, meshCutCell3000m,
                meshSlantedCell1000m, meshSlantedCell2000m, meshSlantedCell3000m
        ]

    def addTo(self, build):
        build.addAll(self.meshes)
        build.add(self.btf1000mLinearUpwind)
        build.add(self.btf2000mLinearUpwind)
        build.add(self.btf3000mLinearUpwind)
        build.add(self.btf1000mCubicFit)
        build.add(self.btf2000mCubicFit)
        build.add(self.btf3000mCubicFit)
        build.add(self.sleve1000mLinearUpwind)
        build.add(self.sleve2000mLinearUpwind)
        build.add(self.sleve3000mLinearUpwind)
        build.add(self.sleve1000mCubicFit)
        build.add(self.sleve2000mCubicFit)
        build.add(self.sleve3000mCubicFit)
        build.add(self.sleve1000mLinearUpwind)
        build.add(self.cutCell1000mLinearUpwind)
        build.add(self.cutCell2000mLinearUpwind)
        build.add(self.cutCell3000mLinearUpwind)
        build.add(self.cutCell1000mCubicFit)
        build.add(self.cutCell2000mCubicFit)
        build.add(self.cutCell3000mCubicFit)
        build.add(self.slantedCell1000mLinearUpwind)
        build.add(self.slantedCell2000mLinearUpwind)
        build.add(self.slantedCell3000mLinearUpwind)
        build.add(self.slantedCell1000mCubicFit)
        build.add(self.slantedCell2000mCubicFit)
        build.add(self.slantedCell3000mCubicFit)
