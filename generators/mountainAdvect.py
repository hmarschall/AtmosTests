from ninjaopenfoam import CutCellMesh
import os

class MountainAdvect:
    def __init__(self, parallel, fast):
        pass

    def addTo(self, build):
        createPatchDict = os.path.join('src/mountainAdvect/createPatchDict')
        build.add(CutCellMesh('mountainAdvect-mesh-cutCell-1000-3000m', os.path.join('src/mountainAdvect/mesh-cutCell-1000-3000m'), createPatchDict))
