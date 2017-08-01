from ninjaopenfoam import CutCellMesh, MountainAdvectBuilder, \
        MountainAdvectCollatedByMeshSpacing, MountainAdvectCollatedByMountainHeight, \
        SlantedCellMesh, TerrainFollowingMesh
import os

class MountainAdvect:
    def __init__(self, advect, parallel, fast):

        meshBtf1000_3000m = TerrainFollowingMesh('mountainAdvect-mesh-btf-1000-3000m', advect.meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-btf-3000m'))
        meshBtf1000_4000m = TerrainFollowingMesh('mountainAdvect-mesh-btf-1000-4000m', advect.meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-btf-4000m'))
        meshBtf1000_5000m = TerrainFollowingMesh('mountainAdvect-mesh-btf-1000-5000m', advect.meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-btf-5000m'))

        meshCutCell1000_3000m = CutCellMesh('mountainAdvect-mesh-cutCell-1000-3000m', os.path.join('src/mountainAdvect/mesh-cutCell-1000-3000m'), advect.createPatchDict)
        meshCutCell1000_4000m = CutCellMesh('mountainAdvect-mesh-cutCell-1000-4000m', os.path.join('src/mountainAdvect/mesh-cutCell-1000-4000m'), advect.createPatchDict)
        meshCutCell1000_5000m = CutCellMesh('mountainAdvect-mesh-cutCell-1000-5000m', os.path.join('src/mountainAdvect/mesh-cutCell-1000-5000m'), advect.createPatchDict)

        meshSlantedCell1000_3000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-1000-3000m', advect.meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-slantedCell-3000m'))
        meshSlantedCell1000_4000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-1000-4000m', advect.meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-slantedCell-4000m'))
        meshSlantedCell1000_5000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-1000-5000m', advect.meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-slantedCell-5000m'))
        meshSlantedCell1000_6000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-1000-6000m', advect.meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-slantedCell-6000m'))

        meshSlantedCell5000_6000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-5000-6000m', advect.meshNoOrography5000, os.path.join('src/mountainAdvect/mesh-slantedCell-6000m'))
        meshSlantedCell2500_6000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-2500-6000m', advect.meshNoOrography2500, os.path.join('src/mountainAdvect/mesh-slantedCell-6000m'))
        meshSlantedCell2000_6000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-2000-6000m', advect.meshNoOrography2000, os.path.join('src/mountainAdvect/mesh-slantedCell-6000m'))
        meshSlantedCell1250_6000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-1250-6000m', advect.meshNoOrography1250, os.path.join('src/mountainAdvect/mesh-slantedCell-6000m'))
        meshSlantedCell667_6000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-667-6000m', advect.meshNoOrography667, os.path.join('src/mountainAdvect/mesh-slantedCell-6000m'))
        meshSlantedCell500_6000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-500-6000m', advect.meshNoOrography500, os.path.join('src/mountainAdvect/mesh-slantedCell-6000m'))
        meshSlantedCell333_6000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-333-6000m', advect.meshNoOrography333, os.path.join('src/mountainAdvect/mesh-slantedCell-6000m'))
        meshSlantedCell250_6000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-250-6000m', advect.meshNoOrography250, os.path.join('src/mountainAdvect/mesh-slantedCell-6000m'))

        self.meshes = [
                meshBtf1000_3000m, meshBtf1000_4000m, meshBtf1000_5000m,
                meshCutCell1000_3000m, meshCutCell1000_4000m, meshCutCell1000_5000m,
                meshSlantedCell1000_3000m, meshSlantedCell1000_4000m, meshSlantedCell1000_5000m,
                meshSlantedCell5000_6000m, meshSlantedCell2500_6000m, meshSlantedCell2000_6000m,
                meshSlantedCell1250_6000m, meshSlantedCell1000_6000m, meshSlantedCell667_6000m,
                meshSlantedCell500_6000m, meshSlantedCell333_6000m, meshSlantedCell250_6000m
        ]

        mountainAdvect = MountainAdvectBuilder(parallel, fast, fastMesh=advect.meshNoOrography1000)

        # l2ByMountainHeight

        velocityField0m = os.path.join('src/mountainAdvect/velocityField-0m')
        velocityField3000m = os.path.join('src/mountainAdvect/velocityField-3000m')
        velocityField4000m = os.path.join('src/mountainAdvect/velocityField-4000m')
        velocityField5000m = os.path.join('src/mountainAdvect/velocityField-5000m')
        velocityField6000m = os.path.join('src/mountainAdvect/velocityField-6000m')

        self.btfLinearUpwind = mountainAdvect.collateByMountainHeight(
                'mountainAdvect-h0-btf-1000-linearUpwind-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-btf-1000-0m-linearUpwind', 0, advect.meshNoOrography1000, velocityField0m, timestep=40),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-btf-1000-3000m-linearUpwind', 3000, meshBtf1000_3000m, velocityField3000m, timestep=16),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-btf-1000-4000m-linearUpwind', 4000, meshBtf1000_4000m, velocityField4000m, timestep=10),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-btf-1000-5000m-linearUpwind', 5000, meshBtf1000_5000m, velocityField5000m, timestep=8),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-btf-1000-6000m-linearUpwind', 6000, advect.meshBtf1000_6000m, velocityField6000m, timestep=5)
        ])

        self.btfCubicFit = mountainAdvect.collateByMountainHeight(
                'mountainAdvect-h0-btf-1000-cubicFit-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-btf-1000-0m-cubicFit', 0, advect.meshNoOrography1000, velocityField0m, timestep=40),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-btf-1000-3000m-cubicFit', 3000, meshBtf1000_3000m, velocityField3000m, timestep=16),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-btf-1000-4000m-cubicFit', 4000, meshBtf1000_4000m, velocityField4000m, timestep=10),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-btf-1000-5000m-cubicFit', 5000, meshBtf1000_5000m, velocityField5000m, timestep=8),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-btf-1000-6000m-cubicFit', 6000, advect.meshBtf1000_6000m, velocityField6000m, timestep=5)
        ])

        self.cutCellLinearUpwind = mountainAdvect.collateByMountainHeight(
                'mountainAdvect-h0-cutCell-1000-linearUpwind-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-cutCell-1000-0m-linearUpwind', 0, advect.meshNoOrography1000, velocityField0m, timestep=40),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-cutCell-1000-3000m-linearUpwind', 3000, meshCutCell1000_3000m, velocityField3000m, timestep=1.6),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-cutCell-1000-4000m-linearUpwind', 4000, meshCutCell1000_4000m, velocityField4000m, timestep=1.6),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-cutCell-1000-5000m-linearUpwind', 5000, meshCutCell1000_5000m, velocityField5000m, timestep=0.5),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-cutCell-1000-6000m-linearUpwind', 6000, advect.meshCutCell1000_6000m, velocityField6000m, timestep=1.6)
        ])

        self.cutCellCubicFit = mountainAdvect.collateByMountainHeight(
                'mountainAdvect-h0-cutCell-1000-cubicFit-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-cutCell-1000-0m-cubicFit', 0, advect.meshNoOrography1000, velocityField0m, timestep=40),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-cutCell-1000-3000m-cubicFit', 3000, meshCutCell1000_3000m, velocityField3000m, timestep=1.6),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-cutCell-1000-4000m-cubicFit', 4000, meshCutCell1000_4000m, velocityField4000m, timestep=1.6),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-cutCell-1000-5000m-cubicFit', 5000, meshCutCell1000_5000m, velocityField5000m, timestep=0.5),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-cutCell-1000-6000m-cubicFit', 6000, advect.meshCutCell1000_6000m, velocityField6000m, timestep=1.6)
        ])

        self.slantedCellLinearUpwind = mountainAdvect.collateByMountainHeight(
                'mountainAdvect-h0-slantedCell-1000-linearUpwind-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-slantedCell-1000-0m-linearUpwind', 0, advect.meshNoOrography1000, velocityField0m, timestep=40),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-slantedCell-1000-3000m-linearUpwind', 3000, meshSlantedCell1000_3000m, velocityField3000m, timestep=8),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-slantedCell-1000-4000m-linearUpwind', 4000, meshSlantedCell1000_4000m, velocityField4000m, timestep=6.25),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind', 5000, meshSlantedCell1000_5000m, velocityField5000m, timestep=5),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-slantedCell-1000-6000m-linearUpwind', 6000, meshSlantedCell1000_6000m, velocityField6000m, timestep=4)
        ])

        self.slantedCellCubicFit = mountainAdvect.collateByMountainHeight(
                'mountainAdvect-h0-slantedCell-1000-cubicFit-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-slantedCell-1000-0m-cubicFit', 0, advect.meshNoOrography1000, velocityField0m, timestep=40),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-slantedCell-1000-3000m-cubicFit', 3000, meshSlantedCell1000_3000m, velocityField3000m, timestep=8),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-slantedCell-1000-4000m-cubicFit', 4000, meshSlantedCell1000_4000m, velocityField4000m, timestep=6.25),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-slantedCell-1000-5000m-cubicFit', 5000, meshSlantedCell1000_5000m, velocityField5000m, timestep=5),
                    MountainAdvectCollatedByMountainHeight.Test('mountainAdvect-h0-slantedCell-1000-6000m-cubicFit', 6000, meshSlantedCell1000_6000m, velocityField6000m, timestep=4)
        ])

        # maxdt/maxco

        self.maxdtBtf = mountainAdvect.collateByMeshSpacing(
                'mountainAdvect-maxdt-btf-6000m-cubicFit-collated',
                mountainHeight=6000,
                velocityField=os.path.join('src/mountainAdvect/velocityField-6000m'),
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-btf-5000-6000m-cubicFit', 5000, advect.meshBtf5000_6000m, timestep=500),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-btf-2500-6000m-cubicFit', 2500, advect.meshBtf2500_6000m, timestep=170),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-btf-2000-6000m-cubicFit', 2000, advect.meshBtf2000_6000m, timestep=90),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-btf-1250-6000m-cubicFit', 1250, advect.meshBtf1250_6000m, timestep=40),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-btf-1000-6000m-cubicFit', 1000, advect.meshBtf1000_6000m, timestep=30.395),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-btf-667-6000m-cubicFit', 667, advect.meshBtf667_6000m, timestep=14),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-btf-500-6000m-cubicFit', 500, advect.meshBtf500_6000m, timestep=9),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-btf-333-6000m-cubicFit', 333, advect.meshBtf333_6000m, timestep=5.5),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-btf-250-6000m-cubicFit', 250, advect.meshBtf250_6000m, timestep=4)
        ])

        self.maxdtCutCell = mountainAdvect.collateByMeshSpacing(
                'mountainAdvect-maxdt-cutCell-6000m-cubicFit-collated',
                mountainHeight=6000,
                velocityField=os.path.join('src/mountainAdvect/velocityField-6000m'),
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-cutCell-5000-6000m-cubicFit', 5000, advect.meshCutCell5000_6000m, timestep=400),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-cutCell-2500-6000m-cubicFit', 2500, advect.meshCutCell2500_6000m, timestep=36),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-cutCell-2000-6000m-cubicFit', 2000, advect.meshCutCell2000_6000m, timestep=12),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-cutCell-1250-6000m-cubicFit', 1250, advect.meshCutCell1250_6000m, timestep=4.5),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-cutCell-1000-6000m-cubicFit', 1000, advect.meshCutCell1000_6000m, timestep=10),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-cutCell-667-6000m-cubicFit', 667, advect.meshCutCell667_6000m, timestep=0.85),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-cutCell-500-6000m-cubicFit', 500, advect.meshCutCell500_6000m, timestep=0.85),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-cutCell-333-6000m-cubicFit', 333, advect.meshCutCell333_6000m, timestep=0.35),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-cutCell-250-6000m-cubicFit', 250, advect.meshCutCell250_6000m, timestep=0.32)
        ])

        self.maxdtSlantedCell = mountainAdvect.collateByMeshSpacing(
                'mountainAdvect-maxdt-slantedCell-6000m-cubicFit-collated',
                mountainHeight=6000,
                velocityField=os.path.join('src/mountainAdvect/velocityField-6000m'),
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-slantedCell-5000-6000m-cubicFit', 5000, meshSlantedCell5000_6000m, timestep=400),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-slantedCell-2500-6000m-cubicFit', 2500, meshSlantedCell2500_6000m, timestep=90),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-slantedCell-2000-6000m-cubicFit', 2000, meshSlantedCell2000_6000m, timestep=55),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-slantedCell-1250-6000m-cubicFit', 1250, meshSlantedCell1250_6000m, timestep=30),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-slantedCell-1000-6000m-cubicFit', 1000, meshSlantedCell1000_6000m, timestep=20),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-slantedCell-667-6000m-cubicFit', 667, meshSlantedCell667_6000m, timestep=12),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-slantedCell-500-6000m-cubicFit', 500, meshSlantedCell500_6000m, timestep=8),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-slantedCell-333-6000m-cubicFit', 333, meshSlantedCell333_6000m, timestep=5),
                    MountainAdvectCollatedByMeshSpacing.Test('mountainAdvect-maxdt-slantedCell-250-6000m-cubicFit', 250, meshSlantedCell250_6000m, timestep=3.5)
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
        build.add(self.maxdtBtf)
        build.addAll(self.maxdtBtf.tests)
        build.add(self.maxdtCutCell)
        build.addAll(self.maxdtCutCell.tests)
        build.add(self.maxdtSlantedCell)
        build.addAll(self.maxdtSlantedCell.tests)
