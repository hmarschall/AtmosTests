#!/usr/bin/python3

import ninja_gen
import os

class SchaerAdvect:
    def __init__(self, case, meshCase, timestep, fvSchemes, parallel):
        self.case = case
        self.meshCase = meshCase
        self.timestep = timestep
        self.endTime = 10000
        self.writeInterval = 5000
        self.fvSchemes = fvSchemes
        self.parallel = parallel

    def write(self):
        case = self.case
        g = ninja_gen.Generator()
        g.header()

        solver = ninja_gen.Solver(g, case, self.parallel, os.path.join("src", "decomposeParDict.template"))
        solver.solve(
                outputs=[case.path(str(self.endTime), "T"),
                         case.path(str(self.writeInterval), "T")],
                rule="advectionFoam",
                implicit=[case.path("0", "T"), case.path("0", "phi")]
        )

        g.controlDict(case, self.endTime, self.timestep, self.writeInterval)
        g.n.build(
                outputs=case.path("0", "T"),
                rule="setInitialTracerField",
                implicit=case.polyMesh + case.systemFiles +
                        [case.tracerFieldDict, case.T_init],
                variables={"case": self.case}
        )
        g.n.newline()
        g.copy(os.path.join("src", "schaerAdvect", "tracerField"), case.tracerFieldDict)
        g.copy(os.path.join("src", "schaerAdvect", "T_init"), case.T_init)
        g.n.newline()
        g.n.build(
                outputs=case.path("0", "phi"),
                rule="setVelocityField",
                implicit=case.polyMesh + case.systemFiles + [case.velocityFieldDict],
                variables={"case": self.case}
        )
        g.n.newline()
        g.copy(os.path.join("src", "schaerAdvect", "velocityField"), case.velocityFieldDict)
        g.n.newline()

        g.copyAll(ninja_gen.Paths.polyMesh, source=self.meshCase, target=case)
        g.copy(self.fvSchemes, case.fvSchemes)
        g.copy(os.path.join("src", "fvSolution"), case.fvSolution)

        g.s3upload(
                case,
                [case.path(str(self.endTime), "T"),
                 case.path(str(self.writeInterval), "T"),
                 case.path("0", "T")])

if __name__ == '__main__':
    parser = ninja_gen.Parser()
    parser.case()
    parser.meshCase()
    parser.timestep("double-precision float that divides into 5000")
    parser.fvSchemes()
    parser.solverExecution()
    args = parser.p.parse_args()

    solver = SchaerAdvect(ninja_gen.Case(args.case), ninja_gen.Case(args.meshCase), args.timestep, args.fvSchemes, args.solver_execution=="parallel")
    solver.write()
