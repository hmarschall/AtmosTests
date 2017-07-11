#!/usr/bin/python3

import argparse
import ninja_gen
import os

def write(blockMeshCase, sourceMountainDict, case, sourceControlDict=os.path.join("src", "controlDict")):
    g = ninja_gen.Generator()
    g.header()

    g.n.build \
    ( \
            outputs=case.polyMesh, \
            rule="terrainFollowingMesh", \
            inputs=case.mountainDict, \
            implicit=blockMeshCase.polyMesh + [case.controlDict], \
            variables={"blockMeshCase": blockMeshCase, "terrainFollowingMeshCase": case} \
    )
    g.n.newline()

    g.copy(sourceMountainDict, case.mountainDict)
    g.copy(sourceControlDict, case.controlDict)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a terrainFollowingMesh .ninja file.')
    parser.add_argument('case', help="Target terrainFollowingMesh case directory")
    parser.add_argument('blockMeshCase', help="Case directory of the block mesh")
    parser.add_argument('mountainDict', help="Location of the mountainDict file")
    args = parser.parse_args()

    write(ninja_gen.Case(args.blockMeshCase), args.mountainDict, ninja_gen.Case(args.case))
