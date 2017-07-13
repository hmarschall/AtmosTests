#!/usr/bin/python3

import argparse
import ninja_gen
import os

def write(application, execution, taskCount, serialCommand):
    g = ninja_gen.Generator()
    g.header()

    description = "{application} $case".format(application=application)

    if execution == "serial":
        g.n.rule(application, serialCommand, description=description)
    else:
        g.n.rule(
                application,
                'ninja/openfoam-solve.sh $case $solver_parallel_tasks "{serialCommand} -parallel"'.format(serialCommand=serialCommand),
                description=description)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('application', help="OpenFOAM application")
    parser.add_argument('execution', choices=["serial", "parallel"], help="Determines how the solver is executed")
    parser.add_argument('taskCount', type=int, help="The number of MPI tasks used for parallel execution")
    parser.add_argument('serialCommand', help="The serial solver command line")
    args = parser.parse_args()

    write(args.application, args.execution, args.taskCount, args.serialCommand)

