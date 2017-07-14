class TerrainFollowingMesh:
    def __init__(self, root, blockMesh, mountainDict):
        pass

    def write(self, build):
        g.n.build(
                outputs=case.polyMesh,
                rule="terrainFollowingMesh",
                inputs=case.mountainDict,
                implicit=blockMeshCase.polyMesh + [case.controlDict],
                variables={"blockMeshCase": blockMeshCase, "terrainFollowingMeshCase": case}
        )
        g.n.newline()

        g.copy(sourceMountainDict, case.mountainDict)
        g.copy(sourceControlDict, case.controlDict)
