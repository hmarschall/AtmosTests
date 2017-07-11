#!/usr/bin/python3

import argparse
import ninja_gen
import os

class SchaerAdvect:
    def __init__(self, case, meshCase, timestep, fvSchemes, s3uri="s3://atmostests/"):
        self.case = case
        self.meshCase = meshCase
        self.timestep = timestep
        self.endTime = 10000
        self.writeInterval = 5000
        self.fvSchemes = fvSchemes
        self.s3uri = s3uri

    def write(self):
        case = self.case
        g = ninja_gen.Generator()
        g.header()

        g.n.build \
        ( \
                outputs=[case.path(str(self.endTime), "T"), \
                         case.path(str(self.writeInterval), "T")], \
                rule="advectionFoam", \
                implicit=case.polyMesh + case.systemFiles + \
                        [case.path("0", "T"), case.path("0", "phi")], \
                variables={"case": self.case} \
        )
        g.n.newline()
        g.n.build \
        ( \
                outputs=case.controlDict, \
                rule="gen-controlDict", \
                inputs=os.path.join("src", "controlDict.template"), \
                variables= \
                { \
                    "endTime": self.endTime, \
                    "timestep": self.timestep, \
                    "writeInterval": self.writeInterval, \
                } \
        )
        g.n.newline()
        g.n.build \
        ( \
                outputs=case.path("0", "T"), \
                rule="setInitialTracerField", \
                implicit=case.polyMesh + case.systemFiles + \
                        [case.path("system", "tracerFieldDict"), \
                         case.path("constant", "T_init")], \
                variables={"case": self.case} \
        )
        g.n.newline()
        g.copy(os.path.join("src", "schaerAdvect", "tracerField"), case.path("system", "tracerFieldDict"))
        g.copy(os.path.join("src", "schaerAdvect", "T_init"), case.path("constant", "T_init"))
        g.n.newline()
        g.n.build \
        ( \
                outputs=case.path("0", "phi"), \
                rule="setVelocityField", \
                implicit=case.polyMesh + case.systemFiles + \
                        [case.path("system", "velocityFieldDict")], \
                variables={"case": self.case} \
        )
        g.n.newline()
        g.copy(os.path.join("src", "schaerAdvect", "velocityField"), case.path("system", "velocityFieldDict"))
        g.n.newline()

        g.copyAll(ninja_gen.Paths.polyMesh, source=self.meshCase, target=case)
        g.copy(self.fvSchemes, case.fvSchemes)
        g.copy(os.path.join("src", "schaerAdvect", "fvSolution"), case.fvSolution)

        g.n.build \
        ( \
                outputs=case.path("s3.uploaded"),
                rule="s3-upload", \
                implicit=case.polyMesh + case.systemFiles + \
                        [case.path(str(self.endTime), "T"), \
                         case.path(str(self.writeInterval), "T"), \
                         case.path("0", "T")], \
                variables={"source": case, "target": self.s3uri} \
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a schaerAdvect .ninja file.')
    parser.add_argument('case', help="OpenFOAM case directory")
    parser.add_argument('meshCase', help="Case directory of the mesh")
    parser.add_argument('timestep', type=float, help="double-precision float that divides into 1000")
    parser.add_argument('fvSchemes', help="OpenFOAM fvSchemes file")
    args = parser.parse_args()

    SchaerAdvect(ninja_gen.Case(args.case), ninja_gen.Case(args.meshCase), args.timestep, args.fvSchemes).write()
