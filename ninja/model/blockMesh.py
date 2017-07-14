import os

from .case import Case
from .. import gen

class BlockMesh:
    def __init__(self, root, blockMeshDict, controlDict=os.path.join("src", "controlDict")):
        self.root = root
        self.case = Case(root)
        self.blockMeshDict = blockMeshDict
        self.controlDict = controlDict

    def write(self, generator):
        g = generator
        case = self.case

        g.w.build(
                outputs=case.polyMesh,
                rule="blockMesh",
                inputs=case.blockMeshDict,
                implicit=case.controlDict,
                variables={"case": case}
        )
        g.w.newline()

        g.copy(self.blockMeshDict, case.blockMeshDict)
        g.copy(self.controlDict, case.controlDict)

    def __str__(self):
        return self.root

