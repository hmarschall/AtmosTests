from ninjaopenfoam import BlockMesh, SchaerAdvectBuilder, SchaerAdvectCollated, TerrainFollowingMesh
import os

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
                mountainHeight=6000,
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
                mountainHeight=6000,
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

