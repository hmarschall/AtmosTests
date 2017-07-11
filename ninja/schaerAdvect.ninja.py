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
        g = ninja_gen.Generator(self.case)
        g.header()

        g.n.build \
        ( \
                outputs=[g.forCase(str(self.endTime), "T"), \
                         g.forCase(str(self.writeInterval), "T")], \
                rule="advectionFoam", \
                implicit=g.polyMeshForCase() + g.systemFilesForCase() + \
                        [g.forCase("0", "T"), g.forCase("0", "phi")], \
                variables={"case": self.case} \
        )
        g.n.newline()
        g.n.build \
        ( \
                outputs=g.forCase("system", "controlDict"), \
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
                outputs=g.forCase("0", "T"), \
                rule="setInitialTracerField", \
                implicit=g.polyMeshForCase() + g.systemFilesForCase() + \
                        [g.forCase("system", "tracerFieldDict"), \
                         g.forCase("constant", "T_init")], \
                variables={"case": self.case} \
        )
        g.n.newline()
        g.copy(os.path.join("src", "schaerAdvect", "tracerField"), g.forCase("system", "tracerFieldDict"))
        g.copy(os.path.join("src", "schaerAdvect", "T_init"), g.forCase("constant", "T_init"))
        g.n.newline()
        g.n.build \
        ( \
                outputs=g.forCase("0", "phi"), \
                rule="setVelocityField", \
                implicit=g.polyMeshForCase() + g.systemFilesForCase() + \
                        [g.forCase("system", "velocityFieldDict")], \
                variables={"case": self.case} \
        )
        g.n.newline()
        g.copy(os.path.join("src", "schaerAdvect", "velocityField"), g.forCase("system", "velocityFieldDict"))
        g.n.newline()

        g.copyAll(g.polyMesh, source=self.meshCase, target=self.case)
        g.copy(self.fvSchemes, g.forCase("system", "fvSchemes"))
        g.copy(os.path.join("src", "schaerAdvect", "fvSolution"), g.forCase("system", "fvSolution"))

        g.n.build \
        ( \
                outputs=g.forCase("s3.uploaded"),
                rule="s3-upload", \
                implicit=g.polyMeshForCase() + g.systemFilesForCase() + \
                        [g.forCase(str(self.endTime), "T"), \
                         g.forCase(str(self.writeInterval), "T"), \
                         g.forCase("0", "T")], \
                variables={"source": self.case, "target": self.s3uri} \
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a schaerAdvect .ninja file.')
    parser.add_argument('case', help="OpenFOAM case directory")
    parser.add_argument('meshCase', help="Case directory of the mesh")
    parser.add_argument('timestep', type=float, help="double-precision float that divides into 1000")
    parser.add_argument('fvSchemes', help="OpenFOAM fvSchemes file")
    args = parser.parse_args()

    SchaerAdvect(args.case, args.meshCase, args.timestep, args.fvSchemes).write()
