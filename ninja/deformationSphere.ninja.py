#!/usr/bin/python3

import ninja_gen
import os

class DeformationSphere:
    def __init__(self, case, meshCase, tracerFieldDict, timestep, fvSchemes, parallel):
        self.case = case
        self.meshCase = meshCase
        self.tracerFieldDict = tracerFieldDict
        self.timing = ninja_gen.Timing(1036800, 172800, timestep)
        self.fvSchemes = fvSchemes
        self.parallel = parallel

    def write(self):
        case = self.case
        g = ninja_gen.Generator()
        g.header()

        solver = ninja_gen.Solver(
                g,
                case,
                self.parallel,
                os.path.join("src", "deformationSphere", "decomposeParDict.template")
        )
        solver.solve(
                outputs=[case.path(str(self.timing.endTime), "T"),
                         case.path(str(self.timing.endTime/2), "T")],
                rule="sphericalAdvectionFoam",
                implicit=[case.path("0", "T"), case.advectionDict]
        )

        g.initialTracer(
                case,
                self.tracerFieldDict,
                os.path.join("src", "deformationSphere", "T_init")
        )

        g.copy(os.path.join("src", "deformationSphere", "nonDivergent"), case.advectionDict)
        g.copyMesh(source=self.meshCase, target=case)
        g.copy(self.fvSchemes, case.fvSchemes)
        g.copy(os.path.join("src", "fvSolution"), case.fvSolution)
        g.controlDict(case, self.timing)

        g.s3upload(
                case,
                [case.path(str(self.timing.endTime), "T"),
                 case.path(str(self.timing.endTime/2), "T"),
                 case.path("0", "T")])

if __name__ == '__main__':
    parser = ninja_gen.Parser()
    parser.case()
    parser.meshCase()
    parser.p.add_argument('tracerFieldDict')
    parser.timestep("double-precision float that divides into 5000")
    parser.fvSchemes()
    parser.solverExecution()
    args = parser.p.parse_args()

    solver = DeformationSphere(ninja_gen.Case(args.case), ninja_gen.Case(args.meshCase), args.tracerFieldDict, args.timestep, args.fvSchemes, args.solver_execution=="parallel")
    solver.write()
