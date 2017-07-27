from ninjaopenfoam import BlockMesh, CutCellMesh, SlantedCellMesh
import os

class MountainAdvect:
    def __init__(self, parallel, fast):
        meshNoOrography1000 = BlockMesh('mountainAdvect-mesh-noOrography-1000', os.path.join('src/mountainAdvect/mesh-noOrography-1000'))

        createPatchDict = os.path.join('src/mountainAdvect/createPatchDict')
        meshCutCell1000_3000m = CutCellMesh('mountainAdvect-mesh-cutCell-1000-3000m', os.path.join('src/mountainAdvect/mesh-cutCell-1000-3000m'), createPatchDict)

        meshSlantedCell1000_3000m = SlantedCellMesh('mountainAdvect-mesh-slantedCell-1000-3000m', meshNoOrography1000, os.path.join('src/mountainAdvect/mesh-slantedCell-3000m'))

        self.meshes = [meshNoOrography1000, meshCutCell1000_3000m, meshSlantedCell1000_3000m]

    def addTo(self, build):
        build.addAll(self.meshes)
