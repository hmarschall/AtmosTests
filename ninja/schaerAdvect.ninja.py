#!/usr/bin/python3

import argparse
import ninja_gen

class SchaerAdvect:
    def __init__(self, case, meshCase, timestep, interpolationScheme):
        self.case = case
        self.meshCase = meshCase
        self.timestep = timestep
        self.endTime = 10000
        self.interpolationScheme = interpolationScheme

    def write(self):
        g = ninja_gen.Generator(self.case)
        g.header()

        inputs = g.polyMeshForCase() + g.systemFilesForCase() + \
                [g.forCase("0", "T"), g.forCase("0", "phi")]

        g.n.build \
        ( \
                outputs=g.forCase(str(self.endTime), "T"), \
                rule="advectionFoam", \
                implicit=inputs, \
                variables={"case": self.case} \
        )
        g.n.newline()

        g.copyAll(g.polyMesh, source=self.meshCase, target=self.case)
        
        # TODO: 0/T
        # TODO: 0/phi
        # TODO: system/fvSolution
        # TODO: system/fvSchemes
        # TODO: system/controlDict

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a schaerAdvect .ninja file.')
    parser.add_argument('case', help="OpenFOAM case directory")
    parser.add_argument('meshCase', help="Case directory of the mesh")
    parser.add_argument('timestep', type=float, help="double-precision float that divides into 1000")
    parser.add_argument('interpolationScheme', help="OpenFOAM interpolationScheme for div(T, phi) advection")
    args = parser.parse_args()

    SchaerAdvect(args.case, args.meshCase, args.timestep, args.interpolationScheme).write()
