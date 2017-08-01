#!/usr/bin/python3

import configparser
import distutils.util
import errno
import generators
import itertools
from ninjaopenfoam import Build
import os

class AtmosTests:
    def __init__(self):
        config = configparser.ConfigParser()
        with open('build.properties', 'r') as f:
            config.read_file(itertools.chain(['[default]'], f))
            self.parallel = config['default']['solver_execution'] == 'parallel'
            self.fast = bool(distutils.util.strtobool(config['default']['fast_standins']))

        self.build = Build([
            'generators/advect.py',
            'generators/deformationSphere.py',
            'generators/mountainAdvect.py',
            'generators/resting.py',
            'generators/schaerAdvect.py',
            'generators/solvers.py',
            'generators/tfAdvect.py'
        ])

        generators.Solvers(self.parallel).addTo(self.build)

        advect = generators.Advect()
        advect.addTo(self.build)
        generators.SchaerAdvect(advect, self.parallel, self.fast).addTo(self.build)
        generators.TerrainFollowingAdvect(advect, self.parallel, self.fast).addTo(self.build)
        generators.DeformationSphere(self.parallel, self.fast).addTo(self.build)
        generators.MountainAdvect(advect, self.parallel, self.fast).addTo(self.build)
        generators.Resting(self.parallel, self.fast).addTo(self.build)

    def write(self):
        self.build.write()

if __name__ == '__main__':
    AtmosTests().write()
