#!/usr/bin/python3

import argparse
import ninja_gen
import os

def write(execution, taskCount, serialCommand):
    g = ninja_gen.Generator()
    g.header()

    if execution == "serial":
        g.n.rule("advectionFoam", serialCommand)
    else:
        g.n.rule("advectionFoam", 'ninja/openfoam-solve.sh $case $solver_parallel_tasks "{serialCommand} -parallel"'.format(serialCommand=serialCommand))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a solver .ninja file.')
    parser.add_argument('execution', choices=["serial", "parallel"], help="Determines how the solver is executed")
    parser.add_argument('taskCount', type=int, help="The number of MPI tasks used for parallel execution")
    parser.add_argument('serialCommand', help="The serial solver command line")
    args = parser.parse_args()

    write(args.execution, args.taskCount, args.serialCommand)

