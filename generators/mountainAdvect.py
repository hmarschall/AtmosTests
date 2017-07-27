from ninjaopenfoam import BlockMesh, CutCellMesh, MountainAdvectBuilder, MountainAdvectCollated, SlantedCellMesh, TerrainFollowingMesh
import os

class MountainAdvect:
    def __init__(self, parallel, fast):
        createPatchDict = os.path.join('src/mountainAdvect/createPatchDict')

        meshNoOrography1000 = BlockMesh('mountainAdvect-mesh-noOrography-1000', os.path.join('src/mountainAdvect/mesh-noOrography-1000'))

        meshBtf1000_3000m = TerrainFollowingMesh('mountainAdvect-mesh-btf-1000-3000m', meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-btf-3000m'))
        meshBtf1000_4000m = TerrainFollowingMesh('mountainAdvect-mesh-btf-1000-4000m', meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-btf-4000m'))
        meshBtf1000_5000m = TerrainFollowingMesh('mountainAdvect-mesh-btf-1000-5000m', meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-btf-5000m'))
        meshBtf1000_6000m = TerrainFollowingMesh('mountainAdvect-mesh-btf-1000-6000m', meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-btf-6000m'))

        meshCutCell1000_3000m = CutCellMesh('mountainAdvect-mesh-cutCell-1000-3000m', os.path.join('src/mountainAdvect/mesh-cutCell-1000-3000m'), createPatchDict)
        meshCutCell1000_4000m = CutCellMesh('mountainAdvect-mesh-cutCell-1000-4000m', os.path.join('src/mountainAdvect/mesh-cutCell-1000-4000m'), createPatchDict)
        meshCutCell1000_5000m = CutCellMesh('mountainAdvect-mesh-cutCell-1000-5000m', os.path.join('src/mountainAdvect/mesh-cutCell-1000-5000m'), createPatchDict)
        meshCutCell1000_6000m = CutCellMesh('mountainAdvect-mesh-cutCell-1000-6000m', os.path.join('src/mountainAdvect/mesh-cutCell-1000-6000m'), createPatchDict)

        meshSlantedCell1000_3000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-1000-3000m', meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-slantedCell-3000m'))
        meshSlantedCell1000_4000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-1000-4000m', meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-slantedCell-4000m'))
        meshSlantedCell1000_5000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-1000-5000m', meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-slantedCell-5000m'))
        meshSlantedCell1000_6000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-1000-6000m', meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-slantedCell-6000m'))

        self.meshes = [meshNoOrography1000, 
                meshBtf1000_3000m, meshBtf1000_4000m, meshBtf1000_5000m, meshBtf1000_6000m,
                meshCutCell1000_3000m, meshCutCell1000_4000m, meshCutCell1000_5000m, meshCutCell1000_6000m,
                meshSlantedCell1000_3000m, meshSlantedCell1000_4000m, meshSlantedCell1000_5000m, meshSlantedCell1000_6000m]

        mountainAdvect = MountainAdvectBuilder(parallel, fast, fastMesh=meshNoOrography1000)

        self.btfLinearUpwind = mountainAdvect.collated(
                'mountainAdvect-h0-btf-1000-linearUpwind-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    MountainAdvectCollated.Test('mountainAdvect-h0-btf-1000-0m-linearUpwind', 0, meshNoOrography1000, timestep=40),
                    MountainAdvectCollated.Test('mountainAdvect-h0-btf-1000-3000m-linearUpwind', 3000, meshBtf1000_3000m, timestep=16),
                    MountainAdvectCollated.Test('mountainAdvect-h0-btf-1000-4000m-linearUpwind', 4000, meshBtf1000_4000m, timestep=10),
                    MountainAdvectCollated.Test('mountainAdvect-h0-btf-1000-5000m-linearUpwind', 5000, meshBtf1000_5000m, timestep=8),
                    MountainAdvectCollated.Test('mountainAdvect-h0-btf-1000-6000m-linearUpwind', 6000, meshBtf1000_6000m, timestep=5)
        ])

        self.btfCubicFit = mountainAdvect.collated(
                'mountainAdvect-h0-btf-1000-cubicFit-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    MountainAdvectCollated.Test('mountainAdvect-h0-btf-1000-0m-cubicFit', 0, meshNoOrography1000, timestep=40),
                    MountainAdvectCollated.Test('mountainAdvect-h0-btf-1000-3000m-cubicFit', 3000, meshBtf1000_3000m, timestep=16),
                    MountainAdvectCollated.Test('mountainAdvect-h0-btf-1000-4000m-cubicFit', 4000, meshBtf1000_4000m, timestep=10),
                    MountainAdvectCollated.Test('mountainAdvect-h0-btf-1000-5000m-cubicFit', 5000, meshBtf1000_5000m, timestep=8),
                    MountainAdvectCollated.Test('mountainAdvect-h0-btf-1000-6000m-cubicFit', 6000, meshBtf1000_6000m, timestep=5)
        ])

        self.cutCellLinearUpwind = mountainAdvect.collated(
                'mountainAdvect-h0-cutCell-1000-linearUpwind-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    MountainAdvectCollated.Test('mountainAdvect-h0-cutCell-1000-0m-linearUpwind', 0, meshNoOrography1000, timestep=40),
                    MountainAdvectCollated.Test('mountainAdvect-h0-cutCell-1000-3000m-linearUpwind', 3000, meshCutCell1000_3000m, timestep=1.6),
                    MountainAdvectCollated.Test('mountainAdvect-h0-cutCell-1000-4000m-linearUpwind', 4000, meshCutCell1000_4000m, timestep=1.6),
                    MountainAdvectCollated.Test('mountainAdvect-h0-cutCell-1000-5000m-linearUpwind', 5000, meshCutCell1000_5000m, timestep=0.5),
                    MountainAdvectCollated.Test('mountainAdvect-h0-cutCell-1000-6000m-linearUpwind', 6000, meshCutCell1000_6000m, timestep=1.6)
        ])

        self.cutCellCubicFit = mountainAdvect.collated(
                'mountainAdvect-h0-cutCell-1000-cubicFit-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    MountainAdvectCollated.Test('mountainAdvect-h0-cutCell-1000-0m-cubicFit', 0, meshNoOrography1000, timestep=40),
                    MountainAdvectCollated.Test('mountainAdvect-h0-cutCell-1000-3000m-cubicFit', 3000, meshCutCell1000_3000m, timestep=1.6),
                    MountainAdvectCollated.Test('mountainAdvect-h0-cutCell-1000-4000m-cubicFit', 4000, meshCutCell1000_4000m, timestep=1.6),
                    MountainAdvectCollated.Test('mountainAdvect-h0-cutCell-1000-5000m-cubicFit', 5000, meshCutCell1000_5000m, timestep=0.5),
                    MountainAdvectCollated.Test('mountainAdvect-h0-cutCell-1000-6000m-cubicFit', 6000, meshCutCell1000_6000m, timestep=1.6)
        ])

        self.slantedCellLinearUpwind = mountainAdvect.collated(
                'mountainAdvect-h0-slantedCell-1000-linearUpwind-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    MountainAdvectCollated.Test('mountainAdvect-h0-slantedCell-1000-0m-linearUpwind', 0, meshNoOrography1000, timestep=40),
                    MountainAdvectCollated.Test('mountainAdvect-h0-slantedCell-1000-3000m-linearUpwind', 3000, meshSlantedCell1000_3000m, timestep=8),
                    MountainAdvectCollated.Test('mountainAdvect-h0-slantedCell-1000-4000m-linearUpwind', 4000, meshSlantedCell1000_4000m, timestep=6.25),
                    MountainAdvectCollated.Test('mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind', 5000, meshSlantedCell1000_5000m, timestep=5),
                    MountainAdvectCollated.Test('mountainAdvect-h0-slantedCell-1000-6000m-linearUpwind', 6000, meshSlantedCell1000_6000m, timestep=4)
        ])

        self.slantedCellCubicFit = mountainAdvect.collated(
                'mountainAdvect-h0-slantedCell-1000-cubicFit-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    MountainAdvectCollated.Test('mountainAdvect-h0-slantedCell-1000-0m-cubicFit', 0, meshNoOrography1000, timestep=40),
                    MountainAdvectCollated.Test('mountainAdvect-h0-slantedCell-1000-3000m-cubicFit', 3000, meshSlantedCell1000_3000m, timestep=8),
                    MountainAdvectCollated.Test('mountainAdvect-h0-slantedCell-1000-4000m-cubicFit', 4000, meshSlantedCell1000_4000m, timestep=6.25),
                    MountainAdvectCollated.Test('mountainAdvect-h0-slantedCell-1000-5000m-cubicFit', 5000, meshSlantedCell1000_5000m, timestep=5),
                    MountainAdvectCollated.Test('mountainAdvect-h0-slantedCell-1000-6000m-cubicFit', 6000, meshSlantedCell1000_6000m, timestep=4)
        ])

    def addTo(self, build):
        build.addAll(self.meshes)
        build.add(self.btfLinearUpwind)
        build.addAll(self.btfLinearUpwind.tests)
        build.add(self.btfCubicFit)
        build.addAll(self.btfCubicFit.tests)
        build.add(self.cutCellLinearUpwind)
        build.addAll(self.cutCellLinearUpwind.tests)
        build.add(self.cutCellCubicFit)
        build.addAll(self.cutCellCubicFit.tests)
        build.add(self.slantedCellLinearUpwind)
        build.addAll(self.slantedCellLinearUpwind.tests)
        build.add(self.slantedCellCubicFit)
        build.addAll(self.slantedCellCubicFit.tests)
