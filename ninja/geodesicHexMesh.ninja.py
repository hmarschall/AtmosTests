#!/usr/bin/python3

import argparse
import ninja_gen
import os

def write(case, refinement):
    g = ninja_gen.Generator()
    g.header()

    g.n.build(
            outputs=case.polyMesh,
            rule="geodesicHexMesh",
            inputs=case.path("patch.obj"),
            implicit=[case.extrudeMeshDict] + case.systemFiles,
            variables={"case": case}
    )
    g.n.newline()

    g.n.build(
            outputs=case.path("patch.obj"),
            rule="geodesicHexPatch",
            variables={"case": case, "refinement": refinement}
    )
    g.n.newline()

    g.copy(os.path.join("src", "deformationSphere", "extrudeFromSurface"), case.extrudeMeshDict)
    g.copy(os.path.join("src", "controlDict"), case.controlDict)
    g.copy(os.path.join("src", "fvSchemes"), case.fvSchemes)
    g.copy(os.path.join("src", "fvSolution"), case.fvSolution)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a geodesicHexMesh .ninja file.')
    parser.add_argument('case', help="OpenFOAM case directory")
    parser.add_argument('refinement', type=int, help="Levels of refinement")
    args = parser.parse_args()

    write(ninja_gen.Case(args.case), args.refinement)

