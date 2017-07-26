from ninjaopenfoam import CubedSphereMesh, DeformationSphereBuilder, DeformationSphereCollated, GeodesicHexMesh
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

