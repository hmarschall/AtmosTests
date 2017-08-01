from ninjaopenfoam import BlockMesh, SchaerAdvectBuilder, SchaerAdvectCollated, TerrainFollowingMesh
import os

class SchaerAdvect:
    def __init__(self, advect, parallel, fast):
        schaerAdvect = SchaerAdvectBuilder(parallel, fast, fastMesh=advect.meshNoOrography5000)

        self.btfLinearUpwindCollated = schaerAdvect.collated(
                'schaerAdvect-btf-linearUpwind-collated',
                mountainHeight=6000,
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    SchaerAdvectCollated.Test('schaerAdvect-btf-5000-linearUpwind', 5000,     advect.meshBtf5000_6000m, timestep=40),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2500-linearUpwind', 2500,     advect.meshBtf2500_6000m, timestep=20),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2000-linearUpwind', 2000,     advect.meshBtf2000_6000m, timestep=16),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1250-linearUpwind', 1250,     advect.meshBtf1250_6000m, timestep=10),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1000-linearUpwind', 1000,     advect.meshBtf1000_6000m, timestep=8),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-667-linearUpwind',  1000/3*2, advect.meshBtf667_6000m,  timestep=5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-500-linearUpwind',  500,      advect.meshBtf500_6000m,  timestep=4),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-333-linearUpwind',  1000/3,   advect.meshBtf333_6000m,  timestep=2.5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-250-linearUpwind',  250,      advect.meshBtf250_6000m,  timestep=2)
        ])

        self.btfCubicFitCollated = schaerAdvect.collated(
                'schaerAdvect-btf-cubicFit-collated',
                mountainHeight=6000,
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    SchaerAdvectCollated.Test('schaerAdvect-btf-5000-cubicFit', 5000,     advect.meshBtf5000_6000m, timestep=40),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2500-cubicFit', 2500,     advect.meshBtf2500_6000m, timestep=20),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-2000-cubicFit', 2000,     advect.meshBtf2000_6000m, timestep=16),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1250-cubicFit', 1250,     advect.meshBtf1250_6000m, timestep=10),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-1000-cubicFit', 1000,     advect.meshBtf1000_6000m, timestep=8),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-667-cubicFit',  1000/3*2, advect.meshBtf667_6000m,  timestep=5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-500-cubicFit',  500,      advect.meshBtf500_6000m,  timestep=4),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-333-cubicFit',  1000/3,   advect.meshBtf333_6000m,  timestep=2.5),
                    SchaerAdvectCollated.Test('schaerAdvect-btf-250-cubicFit',  250,      advect.meshBtf250_6000m,  timestep=2)
        ])

    def addTo(self, build):
        build.add(self.btfLinearUpwindCollated)
        build.addAll(self.btfLinearUpwindCollated.tests)
        build.add(self.btfCubicFitCollated)
        build.addAll(self.btfCubicFitCollated.tests)

