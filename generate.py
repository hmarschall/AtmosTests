#!/usr/bin/python3

import configparser
import distutils.util
import errno
import generators
import itertools
from ninjaopenfoam import Build, SolverRule
import os

class AtmosTests:
    def __init__(self):
        config = configparser.ConfigParser()
        with open('build.properties', 'r') as f:
            config.read_file(itertools.chain(['[default]'], f))
            self.parallel = config['default']['solver_execution'] == 'parallel'
            self.fast = bool(distutils.util.strtobool(config['default']['fast_standins']))

        self.build = Build([
            'generators/deformationSphere.py',
            'generators/schaerAdvect.py'])

        self.solvers()
        generators.DeformationSphere(self.parallel, self.fast).addTo(self.build)
        generators.SchaerAdvect(self.parallel, self.fast).addTo(self.build)

    def write(self):
        self.build.write()

    def solvers(self):
        advectionFoam = SolverRule(
                'advectionFoam',
                'advectionFoam -case $case -heun2',
                self.parallel)

        sphericalAdvectionFoam = SolverRule(
                'sphericalAdvectionFoam',
                'sphericalAdvectionFoam -case $case -heun2',
                self.parallel)

        self.build.add(advectionFoam)
        self.build.add(sphericalAdvectionFoam)


if __name__ == '__main__':
    AtmosTests().write()
