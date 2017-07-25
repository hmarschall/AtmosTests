#!/usr/bin/python3

import configparser
import distutils.util
import errno
import itertools
from ninjaopenfoam import BlockMesh, Build, DeformationSphereBuilder, DeformationSphereCollated, GeodesicHexMesh, SolverRule, SchaerAdvect, TerrainFollowingMesh
import os

class AtmosTests:
    def __init__(self):
        config = configparser.ConfigParser()
        with open('build.properties', 'r') as f:
            config.read_file(itertools.chain(['[default]'], f))
            self.parallel = config['default']['solver_execution'] == 'parallel'
            self.fast = bool(distutils.util.strtobool(config['default']['fast_standins']))

        self.build = Build()
        self.solvers()
        self.deformationSphere()
        self.schaerAdvect()

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

    def deformationSphere(self):
        b = self.build

        meshHex4 = GeodesicHexMesh('deformationSphere-mesh-hex-4', 4, self.fast)
        meshHex5 = GeodesicHexMesh('deformationSphere-mesh-hex-5', 5, self.fast)
        meshHex6 = GeodesicHexMesh('deformationSphere-mesh-hex-6', 6, self.fast)
        meshHex7 = GeodesicHexMesh('deformationSphere-mesh-hex-7', 7, self.fast)
        meshHex8 = GeodesicHexMesh('deformationSphere-mesh-hex-8', 8, self.fast)
        meshHex9 = GeodesicHexMesh('deformationSphere-mesh-hex-9', 9, self.fast)

        deformationSphere = DeformationSphereBuilder(self.parallel, self.fast)

        gaussiansHexLinearUpwindCollated = deformationSphere.collated(
                'deformationSphere-gaussians-hex-linearUpwind-collated',
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tracerFieldDict=os.path.join('src/deformationSphere/gaussians'),
                tests=[
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-4-linearUpwind', meshHex4, timestep=3200),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-5-linearUpwind', meshHex5, timestep=1600),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-6-linearUpwind', meshHex6, timestep=800),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-7-linearUpwind', meshHex7, timestep=400),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-8-linearUpwind', meshHex8, timestep=200),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-9-linearUpwind', meshHex9, timestep=100)
        ])

        gaussiansHexCubicFitCollated = deformationSphere.collated(
                'deformationSphere-gaussians-hex-cubicFit-collated',
                fvSchemes=os.path.join('src/deformationSphere/cubicFit'),
                tracerFieldDict=os.path.join('src/deformationSphere/gaussians'),
                tests=[
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-4-cubicFit', meshHex4, timestep=3200),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-5-cubicFit', meshHex5, timestep=1600),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-6-cubicFit', meshHex6, timestep=800),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-7-cubicFit', meshHex7, timestep=400),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-8-cubicFit', meshHex8, timestep=200),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-hex-9-cubicFit', meshHex9, timestep=100)
        ])

        b.add(meshHex4)
        b.add(meshHex5)
        b.add(meshHex6)
        b.add(meshHex7)
        b.add(meshHex8)
        b.add(meshHex9)

        b.add(gaussiansHexLinearUpwindCollated)
        b.addAll(gaussiansHexLinearUpwindCollated.tests)
        b.add(gaussiansHexCubicFitCollated)
        b.addAll(gaussiansHexCubicFitCollated.tests)

    def schaerAdvect(self):
        b = self.build

        meshNoOrography = BlockMesh(
                'schaerAdvect-mesh-noOrography',
                os.path.join('src/schaerAdvect/mesh-noOrography'))

        meshBtf = TerrainFollowingMesh(
                'schaerAdvect-mesh-btf',
                meshNoOrography,
                os.path.join('src/schaerAdvect/mesh-btf'))

        noOrographyLinearUpwind = SchaerAdvect(
                'schaerAdvect-noOrography-linearUpwind',
                meshNoOrography,
                timestep=8,
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                parallel=self.parallel)

        b.add(meshNoOrography)
        b.add(meshBtf)
        b.add(noOrographyLinearUpwind)


if __name__ == '__main__':
    AtmosTests().write()
