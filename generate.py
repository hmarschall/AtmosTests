#!/usr/bin/python3

import configparser
import distutils.util
import errno
import itertools
from ninjaopenfoam import BlockMesh, Build, CubedSphereMesh, DeformationSphereBuilder, DeformationSphereCollated, \
                        GeodesicHexMesh, SolverRule, SchaerAdvectBuilder, SchaerAdvectCollated, TerrainFollowingMesh
import os

class DeformationSphere:
    def __init__(self, parallel, fast):
        meshHex4 = GeodesicHexMesh('deformationSphere-mesh-hex-4', 4, fast)
        meshHex5 = GeodesicHexMesh('deformationSphere-mesh-hex-5', 5, fast)
        meshHex6 = GeodesicHexMesh('deformationSphere-mesh-hex-6', 6, fast)
        meshHex7 = GeodesicHexMesh('deformationSphere-mesh-hex-7', 7, fast)
        meshHex8 = GeodesicHexMesh('deformationSphere-mesh-hex-8', 8, fast)
        meshHex9 = GeodesicHexMesh('deformationSphere-mesh-hex-9', 9, fast)

        meshCubedSphere15 = CubedSphereMesh('deformationSphere-mesh-cubedSphere-15', 15, fast)
        meshCubedSphere30 = CubedSphereMesh('deformationSphere-mesh-cubedSphere-30', 30, fast)
        meshCubedSphere60 = CubedSphereMesh('deformationSphere-mesh-cubedSphere-60', 60, fast)
        meshCubedSphere120 = CubedSphereMesh('deformationSphere-mesh-cubedSphere-120', 120, fast)
        meshCubedSphere240 = CubedSphereMesh('deformationSphere-mesh-cubedSphere-240', 240, fast)

        self.meshes = [
                meshHex4, meshHex5, meshHex6, meshHex7, meshHex8, meshHex9,
                meshCubedSphere15, meshCubedSphere30, meshCubedSphere60, meshCubedSphere120, meshCubedSphere240
        ]

        deformationSphere = DeformationSphereBuilder(parallel, fast)

        self.gaussiansHexLinearUpwindCollated = deformationSphere.collated(
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

        self.gaussiansCubedSphereLinearUpwindCollated = deformationSphere.collated(
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

        self.gaussiansHexCubicFitCollated = deformationSphere.collated(
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

        self.gaussiansCubedSphereCubicFitCollated = deformationSphere.collated(
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

        self.cosBellsHexLinearUpwindCollated = deformationSphere.collated(
                'deformationSphere-cosBells-hex-linearUpwind-collated',
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tracerFieldDict=os.path.join('src/deformationSphere/cosBells'),
                tests=[
                    DeformationSphereCollated.Test('deformationSphere-cosBells-hex-7-linearUpwind', meshHex7, timestep=400),
                    DeformationSphereCollated.Test('deformationSphere-cosBells-hex-8-linearUpwind', meshHex8, timestep=200),
                    DeformationSphereCollated.Test('deformationSphere-cosBells-hex-9-linearUpwind', meshHex9, timestep=100)
        ])

        self.cosBellsCubedSphereLinearUpwindCollated = deformationSphere.collated(
                'deformationSphere-cosBells-cubedSphere-linearUpwind-collated',
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tracerFieldDict=os.path.join('src/deformationSphere/cosBells'),
                tests=[
                    DeformationSphereCollated.Test('deformationSphere-cosBells-cubedSphere-60-linearUpwind', meshCubedSphere60, timestep=200),
                    DeformationSphereCollated.Test('deformationSphere-cosBells-cubedSphere-120-linearUpwind', meshCubedSphere120, timestep=100),
                    DeformationSphereCollated.Test('deformationSphere-cosBells-cubedSphere-240-linearUpwind', meshCubedSphere240, timestep=50)
        ])

        self.cosBellsHexCubicFitCollated = deformationSphere.collated(
                'deformationSphere-cosBells-hex-cubicFit-collated',
                fvSchemes=os.path.join('src/deformationSphere/cubicFit'),
                tracerFieldDict=os.path.join('src/deformationSphere/cosBells'),
                tests=[
                    DeformationSphereCollated.Test('deformationSphere-cosBells-hex-7-cubicFit', meshHex7, timestep=400),
                    DeformationSphereCollated.Test('deformationSphere-cosBells-hex-8-cubicFit', meshHex8, timestep=200),
                    DeformationSphereCollated.Test('deformationSphere-cosBells-hex-9-cubicFit', meshHex9, timestep=100)
        ])

        self.cosBellsCubedSphereCubicFitCollated = deformationSphere.collated(
                'deformationSphere-cosBells-cubedSphere-cubicFit-collated',
                fvSchemes=os.path.join('src/deformationSphere/cubicFit'),
                tracerFieldDict=os.path.join('src/deformationSphere/cosBells'),
                tests=[
                    DeformationSphereCollated.Test('deformationSphere-cosBells-cubedSphere-60-cubicFit', meshCubedSphere60, timestep=200),
                    DeformationSphereCollated.Test('deformationSphere-cosBells-cubedSphere-120-cubicFit', meshCubedSphere120, timestep=100),
                    DeformationSphereCollated.Test('deformationSphere-cosBells-cubedSphere-240-cubicFit', meshCubedSphere240, timestep=50)
        ])

    def addTo(self, build):
        build.addAll(self.meshes)
        build.add(self.gaussiansHexLinearUpwindCollated)
        build.addAll(self.gaussiansHexLinearUpwindCollated.tests)
        build.add(self.gaussiansCubedSphereLinearUpwindCollated)
        build.addAll(self.gaussiansCubedSphereLinearUpwindCollated.tests)
        build.add(self.gaussiansHexCubicFitCollated)
        build.addAll(self.gaussiansHexCubicFitCollated.tests)
        build.add(self.gaussiansCubedSphereCubicFitCollated)
        build.addAll(self.gaussiansCubedSphereCubicFitCollated.tests)
        build.add(self.cosBellsHexLinearUpwindCollated)
        build.addAll(self.cosBellsHexLinearUpwindCollated.tests)
        build.add(self.cosBellsCubedSphereLinearUpwindCollated)
        build.addAll(self.cosBellsCubedSphereLinearUpwindCollated.tests)
        build.add(self.cosBellsHexCubicFitCollated)
        build.addAll(self.cosBellsHexCubicFitCollated.tests)
        build.add(self.cosBellsCubedSphereCubicFitCollated)
        build.addAll(self.cosBellsCubedSphereCubicFitCollated.tests)

class SchaerAdvect:
    def __init__(self, parallel, fast):
        meshNoOrography5000 = BlockMesh('schaerAdvect-mesh-noOrography-5000', os.path.join('src/schaerAdvect/mesh-noOrography-5000'))
        meshNoOrography2500 = BlockMesh('schaerAdvect-mesh-noOrography-2500', os.path.join('src/schaerAdvect/mesh-noOrography-2500'))
        meshNoOrography2000 = BlockMesh('schaerAdvect-mesh-noOrography-2000', os.path.join('src/schaerAdvect/mesh-noOrography-2000'))
        meshNoOrography1250 = BlockMesh('schaerAdvect-mesh-noOrography-1250', os.path.join('src/schaerAdvect/mesh-noOrography-1250'))
        meshNoOrography1000 = BlockMesh('schaerAdvect-mesh-noOrography-1000', os.path.join('src/schaerAdvect/mesh-noOrography-1000'))
        meshNoOrography667 = BlockMesh('schaerAdvect-mesh-noOrography-667', os.path.join('src/schaerAdvect/mesh-noOrography-667'))
        meshNoOrography500 = BlockMesh('schaerAdvect-mesh-noOrography-500', os.path.join('src/schaerAdvect/mesh-noOrography-500'))
        meshNoOrography333 = BlockMesh('schaerAdvect-mesh-noOrography-333', os.path.join('src/schaerAdvect/mesh-noOrography-333'))
        meshNoOrography250 = BlockMesh('schaerAdvect-mesh-noOrography-250', os.path.join('src/schaerAdvect/mesh-noOrography-250'))

        meshBtf5000 = TerrainFollowingMesh('schaerAdvect-mesh-btf-5000', meshNoOrography5000, os.path.join('src/schaerAdvect/mesh-btf'))
        meshBtf2500 = TerrainFollowingMesh('schaerAdvect-mesh-btf-2500', meshNoOrography2500, os.path.join('src/schaerAdvect/mesh-btf'))
        meshBtf2000 = TerrainFollowingMesh('schaerAdvect-mesh-btf-2000', meshNoOrography2000, os.path.join('src/schaerAdvect/mesh-btf'))
        meshBtf1250 = TerrainFollowingMesh('schaerAdvect-mesh-btf-1250', meshNoOrography1250, os.path.join('src/schaerAdvect/mesh-btf'))
        meshBtf1000 = TerrainFollowingMesh('schaerAdvect-mesh-btf-1000', meshNoOrography1000, os.path.join('src/schaerAdvect/mesh-btf'))
        meshBtf667 = TerrainFollowingMesh('schaerAdvect-mesh-btf-667', meshNoOrography667, os.path.join('src/schaerAdvect/mesh-btf'))
        meshBtf500 = TerrainFollowingMesh('schaerAdvect-mesh-btf-500', meshNoOrography500, os.path.join('src/schaerAdvect/mesh-btf'))
        meshBtf333 = TerrainFollowingMesh('schaerAdvect-mesh-btf-333', meshNoOrography333, os.path.join('src/schaerAdvect/mesh-btf'))
        meshBtf250 = TerrainFollowingMesh('schaerAdvect-mesh-btf-250', meshNoOrography250, os.path.join('src/schaerAdvect/mesh-btf'))

        self.meshes = [
                meshNoOrography5000, meshNoOrography2500, meshNoOrography2000, meshNoOrography1250, meshNoOrography1000, 
                meshNoOrography667, meshNoOrography500, meshNoOrography333, meshNoOrography250, 
                meshBtf5000, meshBtf2500, meshBtf2000, meshBtf1250, meshBtf1000, 
                meshBtf667, meshBtf500, meshBtf333, meshBtf250
        ]

        schaerAdvect = SchaerAdvectBuilder(parallel, fast, fastMesh=meshNoOrography5000)

        self.btfLinearUpwindCollated = schaerAdvect.collated(
                'schaerAdvect-btf-linearUpwind-collated',
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    SchaerAdvectCollated.Test('schaerAdvect-btf-5000-linearUpwind', 5000, meshBtf5000, timestep=40),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2500-linearUpwind', 2500, meshBtf2500, timestep=20),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2000-linearUpwind', 2000, meshBtf2000, timestep=16),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1250-linearUpwind', 1250, meshBtf1250, timestep=10),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1000-linearUpwind', 1000, meshBtf1000, timestep=8),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-667-linearUpwind', 1000/3*2, meshBtf667, timestep=5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-500-linearUpwind', 500, meshBtf500, timestep=4),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-333-linearUpwind', 1000/3, meshBtf333, timestep=2.5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-250-linearUpwind', 250, meshBtf250, timestep=2)
        ])

        self.btfCubicFitCollated = schaerAdvect.collated(
                'schaerAdvect-btf-cubicFit-collated',
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    SchaerAdvectCollated.Test('schaerAdvect-btf-5000-cubicFit', 5000, meshBtf5000, timestep=40),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2500-cubicFit', 2500, meshBtf2500, timestep=20),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2000-cubicFit', 2000, meshBtf2000, timestep=16),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1250-cubicFit', 1250, meshBtf1250, timestep=10),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1000-cubicFit', 1000, meshBtf1000, timestep=8),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-667-cubicFit', 1000/3*2, meshBtf667, timestep=5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-500-cubicFit', 500, meshBtf500, timestep=4),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-333-cubicFit', 1000/3, meshBtf333, timestep=2.5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-250-cubicFit', 250, meshBtf250, timestep=2)
        ])

    def addTo(self, build):
        build.addAll(self.meshes)
        build.add(self.btfLinearUpwindCollated)
        build.addAll(self.btfLinearUpwindCollated.tests)
        build.add(self.btfCubicFitCollated)
        build.addAll(self.btfCubicFitCollated.tests)

class AtmosTests:
    def __init__(self):
        config = configparser.ConfigParser()
        with open('build.properties', 'r') as f:
            config.read_file(itertools.chain(['[default]'], f))
            self.parallel = config['default']['solver_execution'] == 'parallel'
            self.fast = bool(distutils.util.strtobool(config['default']['fast_standins']))

        self.build = Build()
        self.solvers()
        DeformationSphere(self.parallel, self.fast).addTo(self.build)
        SchaerAdvect(self.parallel, self.fast).addTo(self.build)

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
