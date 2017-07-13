#!/usr/bin/python3
import ninja_gen

class DeformationSphere:
    def __init__(self, case, meshCase, tracer, timestep, fvSchemes, parallel, s3uri="s3://atmostests/"):
        pass

    def write(self):
    #    case = self.case
        g = ninja_gen.Generator()
        g.header()

if __name__ == '__main__':
    parser = ninja_gen.Parser()
    parser.case()
    parser.meshCase()
    parser.p.add_argument('tracer', help="tracerFieldDict file")
    parser.timestep("double-precision float that divides into 5000")
    parser.fvSchemes()
    parser.solverExecution()
    args = parser.p.parse_args()

    solver = DeformationSphere(ninja_gen.Case(args.case), ninja_gen.Case(args.meshCase), args.tracer, args.timestep, args.fvSchemes, args.solver_execution=="parallel")
    solver.write()
