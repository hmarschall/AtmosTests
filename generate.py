#!/usr/bin/python3

import configparser
import distutils.util
import errno
import itertools
from ninjaopenfoam import BlockMesh, Build, CubedSphereMesh, DeformationSphereBuilder, DeformationSphereCollated, \
                        GeodesicHexMesh, SolverRule, SchaerAdvectBuilder, SchaerAdvectCollated, TerrainFollowingMesh
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

        meshHex4 = b.add(GeodesicHexMesh('deformationSphere-mesh-hex-4', 4, self.fast))
        meshHex5 = b.add(GeodesicHexMesh('deformationSphere-mesh-hex-5', 5, self.fast))
        meshHex6 = b.add(GeodesicHexMesh('deformationSphere-mesh-hex-6', 6, self.fast))
        meshHex7 = b.add(GeodesicHexMesh('deformationSphere-mesh-hex-7', 7, self.fast))
        meshHex8 = b.add(GeodesicHexMesh('deformationSphere-mesh-hex-8', 8, self.fast))
        meshHex9 = b.add(GeodesicHexMesh('deformationSphere-mesh-hex-9', 9, self.fast))

        meshCubedSphere15 = b.add(CubedSphereMesh('deformationSphere-mesh-cubedSphere-15', 15, self.fast))
        meshCubedSphere30 = b.add(CubedSphereMesh('deformationSphere-mesh-cubedSphere-30', 30, self.fast))
        meshCubedSphere60 = b.add(CubedSphereMesh('deformationSphere-mesh-cubedSphere-60', 60, self.fast))
        meshCubedSphere120 = b.add(CubedSphereMesh('deformationSphere-mesh-cubedSphere-120', 120, self.fast))
        meshCubedSphere240 = b.add(CubedSphereMesh('deformationSphere-mesh-cubedSphere-240', 240, self.fast))

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

        gaussiansCubedSphereLinearUpwindCollated = deformationSphere.collated(
                'deformationSphere-gaussians-cubedSphere-linearUpwind-collated',
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tracerFieldDict=os.path.join('src/deformationSphere/gaussians'),
                tests=[
                    DeformationSphereCollated.Test('deformationSphere-gaussians-cubedSphere-15-linearUpwind', meshCubedSphere15, timestep=800),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-cubedSphere-30-linearUpwind', meshCubedSphere30, timestep=400),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-cubedSphere-60-linearUpwind', meshCubedSphere60, timestep=200),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-cubedSphere-120-linearUpwind', meshCubedSphere120, timestep=100),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-cubedSphere-240-linearUpwind', meshCubedSphere240, timestep=50)
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

        gaussiansCubedSphereCubicFitCollated = deformationSphere.collated(
                'deformationSphere-gaussians-cubedSphere-cubicFit-collated',
                fvSchemes=os.path.join('src/deformationSphere/cubicFit'),
                tracerFieldDict=os.path.join('src/deformationSphere/gaussians'),
                tests=[
                    DeformationSphereCollated.Test('deformationSphere-gaussians-cubedSphere-15-cubicFit', meshCubedSphere15, timestep=800),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-cubedSphere-30-cubicFit', meshCubedSphere30, timestep=400),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-cubedSphere-60-cubicFit', meshCubedSphere60, timestep=200),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-cubedSphere-120-cubicFit', meshCubedSphere120, timestep=100),
                    DeformationSphereCollated.Test('deformationSphere-gaussians-cubedSphere-240-cubicFit', meshCubedSphere240, timestep=50)
        ])

        b.add(gaussiansHexLinearUpwindCollated)
        b.addAll(gaussiansHexLinearUpwindCollated.tests)
        b.add(gaussiansCubedSphereLinearUpwindCollated)
        b.addAll(gaussiansCubedSphereLinearUpwindCollated.tests)
        b.add(gaussiansHexCubicFitCollated)
        b.addAll(gaussiansHexCubicFitCollated.tests)
        b.add(gaussiansCubedSphereCubicFitCollated)
        b.addAll(gaussiansCubedSphereCubicFitCollated.tests)

    def schaerAdvect(self):
        b = self.build

        meshNoOrography5000 = b.add(BlockMesh('schaerAdvect-mesh-noOrography-5000', os.path.join('src/schaerAdvect/mesh-noOrography-5000')))
        meshNoOrography2500 = b.add(BlockMesh('schaerAdvect-mesh-noOrography-2500', os.path.join('src/schaerAdvect/mesh-noOrography-2500')))
        meshNoOrography2000 = b.add(BlockMesh('schaerAdvect-mesh-noOrography-2000', os.path.join('src/schaerAdvect/mesh-noOrography-2000')))
        meshNoOrography1250 = b.add(BlockMesh('schaerAdvect-mesh-noOrography-1250', os.path.join('src/schaerAdvect/mesh-noOrography-1250')))
        meshNoOrography1000 = b.add(BlockMesh('schaerAdvect-mesh-noOrography-1000', os.path.join('src/schaerAdvect/mesh-noOrography-1000')))
        meshNoOrography667 = b.add(BlockMesh('schaerAdvect-mesh-noOrography-667', os.path.join('src/schaerAdvect/mesh-noOrography-667')))
        meshNoOrography500 = b.add(BlockMesh('schaerAdvect-mesh-noOrography-500', os.path.join('src/schaerAdvect/mesh-noOrography-500')))
        meshNoOrography333 = b.add(BlockMesh('schaerAdvect-mesh-noOrography-333', os.path.join('src/schaerAdvect/mesh-noOrography-333')))
        meshNoOrography250 = b.add(BlockMesh('schaerAdvect-mesh-noOrography-250', os.path.join('src/schaerAdvect/mesh-noOrography-250')))

        meshBtf5000 = b.add(TerrainFollowingMesh('schaerAdvect-mesh-btf-5000', meshNoOrography5000, os.path.join('src/schaerAdvect/mesh-btf')))
        meshBtf2500 = b.add(TerrainFollowingMesh('schaerAdvect-mesh-btf-2500', meshNoOrography2500, os.path.join('src/schaerAdvect/mesh-btf')))
        meshBtf2000 = b.add(TerrainFollowingMesh('schaerAdvect-mesh-btf-2000', meshNoOrography2000, os.path.join('src/schaerAdvect/mesh-btf')))
        meshBtf1250 = b.add(TerrainFollowingMesh('schaerAdvect-mesh-btf-1250', meshNoOrography1250, os.path.join('src/schaerAdvect/mesh-btf')))
        meshBtf1000 = b.add(TerrainFollowingMesh('schaerAdvect-mesh-btf-1000', meshNoOrography1000, os.path.join('src/schaerAdvect/mesh-btf')))
        meshBtf667 = b.add(TerrainFollowingMesh('schaerAdvect-mesh-btf-667', meshNoOrography667, os.path.join('src/schaerAdvect/mesh-btf')))
        meshBtf500 = b.add(TerrainFollowingMesh('schaerAdvect-mesh-btf-500', meshNoOrography500, os.path.join('src/schaerAdvect/mesh-btf')))
        meshBtf333 = b.add(TerrainFollowingMesh('schaerAdvect-mesh-btf-333', meshNoOrography333, os.path.join('src/schaerAdvect/mesh-btf')))
        meshBtf250 = b.add(TerrainFollowingMesh('schaerAdvect-mesh-btf-250', meshNoOrography250, os.path.join('src/schaerAdvect/mesh-btf')))

        schaerAdvect = SchaerAdvectBuilder(self.parallel, self.fast, fastMesh=meshNoOrography5000)

        btfLinearUpwindCollated = schaerAdvect.collated(
                'schaerAdvect-btf-linearUpwind-collated',
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    SchaerAdvectCollated.Test('schaerAdvect-btf-5000-linearUpwind', meshBtf5000, timestep=40),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2500-linearUpwind', meshBtf2500, timestep=20),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2000-linearUpwind', meshBtf2000, timestep=16),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1250-linearUpwind', meshBtf1250, timestep=10),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1000-linearUpwind', meshBtf1000, timestep=8),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-667-linearUpwind', meshBtf667, timestep=5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-500-linearUpwind', meshBtf500, timestep=4),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-333-linearUpwind', meshBtf333, timestep=2.5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-250-linearUpwind', meshBtf250, timestep=2)
        ])

        btfCubicFitCollated = schaerAdvect.collated(
                'schaerAdvect-btf-cubicFit-collated',
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    SchaerAdvectCollated.Test('schaerAdvect-btf-5000-cubicFit', meshBtf5000, timestep=40),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2500-cubicFit', meshBtf2500, timestep=20),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2000-cubicFit', meshBtf2000, timestep=16),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1250-cubicFit', meshBtf1250, timestep=10),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1000-cubicFit', meshBtf1000, timestep=8),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-667-cubicFit', meshBtf667, timestep=5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-500-cubicFit', meshBtf500, timestep=4),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-333-cubicFit', meshBtf333, timestep=2.5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-250-cubicFit', meshBtf250, timestep=2)
        ])

        b.add(btfLinearUpwindCollated)
        b.addAll(btfLinearUpwindCollated.tests)
        b.add(btfCubicFitCollated)
        b.addAll(btfCubicFitCollated.tests)


if __name__ == '__main__':
    AtmosTests().write()
