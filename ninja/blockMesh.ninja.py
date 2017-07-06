#!/usr/bin/python3

import argparse
import ninja_gen
import os

def write(case, sourceBlockMeshDict, sourceControlDict=os.path.join("src", "controlDict")):
    g = ninja_gen.Generator(case)
    g.header()

    targetBlockMeshDict = g.forCase("system", "blockMeshDict")
    targetControlDict = g.forCase("system", "controlDict")

    g.n.build \
    ( \
            outputs=g.polyMeshForCase(), \
            rule="blockMesh", \
            inputs=targetBlockMeshDict, \
            implicit=targetControlDict, \
            variables={"case": case} \
    )
    g.n.newline()

    g.copy(sourceBlockMeshDict, targetBlockMeshDict)
    g.copy(sourceControlDict, targetControlDict)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a blockMesh .ninja file.')
    parser.add_argument('case', help="OpenFOAM case directory")
    parser.add_argument('blockMeshDict', help="Location of the blockMeshDict file")
    args = parser.parse_args()

    write(args.case, args.blockMeshDict)
