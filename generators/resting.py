from ninjaopenfoam import BlockMesh, CutCellMesh, RestingBuilder, RestingCollated, \
        SlantedCellMesh, TerrainFollowingMesh
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

        self.meshes = [
                meshNoOrography,
                meshBtf1000m, meshBtf2000m, meshBtf3000m,
                meshSleve1000m, meshSleve2000m, meshSleve3000m,
                meshCutCell1000m, meshCutCell2000m, meshCutCell3000m,
                meshSlantedCell1000m, meshSlantedCell2000m, meshSlantedCell3000m
        ]

        # maxwByMountainHeight

        resting = RestingBuilder(parallel, fast, fastMesh=meshNoOrography)

        self.btfLinearUpwind = resting.collateByMountainHeight(
                'resting-btf-linearUpwind-collated',
                fvSchemes=os.path.join('src/resting/linearUpwind'),
                tests=[
                    RestingCollated.Test('resting-btf-0m-linearUpwind', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-btf-1000m-linearUpwind', 1000, meshBtf1000m, timestep=25),
                    RestingCollated.Test('resting-btf-2000m-linearUpwind', 2000, meshBtf2000m, timestep=25),
                    RestingCollated.Test('resting-btf-3000m-linearUpwind', 3000, meshBtf3000m, timestep=25),
        ])

        self.sleveLinearUpwind = resting.collateByMountainHeight(
                'resting-sleve-linearUpwind-collated',
                fvSchemes=os.path.join('src/resting/linearUpwind'),
                tests=[
                    RestingCollated.Test('resting-sleve-0m-linearUpwind', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-sleve-1000m-linearUpwind', 1000, meshSleve1000m, timestep=25),
                    RestingCollated.Test('resting-sleve-2000m-linearUpwind', 2000, meshSleve2000m, timestep=25),
                    RestingCollated.Test('resting-sleve-3000m-linearUpwind', 3000, meshSleve3000m, timestep=25),
        ])

        self.cutCellLinearUpwind = resting.collateByMountainHeight(
                'resting-cutCell-linearUpwind-collated',
                fvSchemes=os.path.join('src/resting/linearUpwind'),
                tests=[
                    RestingCollated.Test('resting-cutCell-0m-linearUpwind', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-cutCell-1000m-linearUpwind', 1000, meshCutCell1000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-2000m-linearUpwind', 2000, meshCutCell2000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-3000m-linearUpwind', 3000, meshCutCell3000m, timestep=25),
        ])

        self.slantedCellLinearUpwind = resting.collateByMountainHeight(
                'resting-slantedCell-linearUpwind-collated',
                fvSchemes=os.path.join('src/resting/linearUpwind'),
                tests=[
                    RestingCollated.Test('resting-slantedCell-0m-linearUpwind', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-slantedCell-1000m-linearUpwind', 1000, meshSlantedCell1000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-2000m-linearUpwind', 2000, meshSlantedCell2000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-3000m-linearUpwind', 3000, meshSlantedCell3000m, timestep=25),
        ])

    def addTo(self, build):
        build.addAll(self.meshes)
        build.add(self.btfLinearUpwind)
        build.addAll(self.btfLinearUpwind.tests)
        build.add(self.sleveLinearUpwind)
        build.addAll(self.sleveLinearUpwind.tests)
        build.add(self.cutCellLinearUpwind)
        build.addAll(self.cutCellLinearUpwind.tests)
        build.add(self.slantedCellLinearUpwind)
        build.addAll(self.slantedCellLinearUpwind.tests)
