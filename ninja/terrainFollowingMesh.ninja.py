#!/usr/bin/python3

import argparse
import ninja_gen
import os

def write(blockMeshCase, sourceMountainDict, case, sourceControlDict=os.path.join("src", "controlDict")):
    g = ninja_gen.Generator(case)
    g.header()

    targetMountainDict = g.forCase("system", "mountainDict")
    targetControlDict = g.forCase("system", "controlDict")

    g.n.build \
    ( \
            outputs=g.polyMesh(), \
            rule="terrainFollowingMesh", \
            inputs=targetMountainDict, \
            implicit=g.polyMesh(blockMeshCase) + [targetControlDict], \
            variables={"blockMeshCase": blockMeshCase, "terrainFollowingMeshCase": case} \
    )
    g.n.newline()

    g.copy(sourceMountainDict, targetMountainDict)
    g.copy(sourceControlDict, targetControlDict)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a terrainFollowingMesh .ninja file.')
    parser.add_argument('case', help="Target terrainFollowingMesh case directory")
    parser.add_argument('blockMeshCase', help="Case directory of the block mesh")
    parser.add_argument('mountainDict', help="Location of the mountainDict file")
    args = parser.parse_args()

    write(args.blockMeshCase, args.mountainDict, args.case)
