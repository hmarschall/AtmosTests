#!/usr/bin/python3

import argparse
import ninja_gen
import os

def write(case, sourceBlockMeshDict, sourceControlDict=os.path.join("src", "controlDict")):
    g = ninja_gen.Generator()
    g.header()

    g.n.build(
            outputs=case.polyMesh,
            rule="blockMesh",
            inputs=case.blockMeshDict,
            implicit=case.controlDict,
            variables={"case": case}
    )
    g.n.newline()

    g.copy(sourceBlockMeshDict, case.blockMeshDict)
    g.copy(sourceControlDict, case.controlDict)

if __name__ == '__main__':
    parser = ninja_gen.Parser()
    parser.case()
    parser.p.add_argument('blockMeshDict', help="Location of the blockMeshDict file")
    args = parser.p.parse_args()

    write(ninja_gen.Case(args.case), args.blockMeshDict)
