from ninjaopenfoam import BlockMesh, CutCellMesh, MountainAdvectBuilder, MountainAdvectCollated, SlantedCellMesh, TerrainFollowingMesh
import os

class MountainAdvect:
    def __init__(self, parallel, fast):
        createPatchDict = os.path.join('src/mountainAdvect/createPatchDict')

        meshNoOrography1000 = BlockMesh('mountainAdvect-mesh-noOrography-1000', os.path.join('src/mountainAdvect/mesh-noOrography-1000'))

        meshBtf1000_3000m = TerrainFollowingMesh('mountainAdvect-mesh-btf-1000-3000m', meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-btf-3000m'))

        meshCutCell1000_3000m = CutCellMesh('mountainAdvect-mesh-cutCell-1000-3000m', os.path.join('src/mountainAdvect/mesh-cutCell-1000-3000m'), createPatchDict)

        meshSlantedCell1000_3000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-1000-3000m', meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-slantedCell-3000m'))

        self.meshes = [meshNoOrography1000, meshBtf1000_3000m, meshCutCell1000_3000m, meshSlantedCell1000_3000m]

        mountainAdvect = MountainAdvectBuilder(parallel, fast, fastMesh=meshNoOrography1000)

        self.btfLinearUpwind = mountainAdvect.collated(
                'mountainAdvect-btf-1000-linearUpwind-collated',
                dx=1000,
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    MountainAdvectCollated.Test('mountainAdvect-btf-1000-0m-linearUpwind', 0, meshNoOrography1000, timestep=40)
        ])

    def addTo(self, build):
        build.addAll(self.meshes)
        build.add(self.btfLinearUpwind)
        build.addAll(self.btfLinearUpwind.tests)
