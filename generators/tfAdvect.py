from ninjaopenfoam import BlockMesh, SchaerAdvectBuilder, SchaerAdvectCollated, TerrainFollowingMesh
import os

class TerrainFollowingAdvect:
    def __init__(self, advect, parallel, fast):
        tfAdvect = SchaerAdvectBuilder(
                mountainHeight=6000,
                velocityField=os.path.join('src/tfAdvect/velocityField'),
                parallel=parallel,
                fast=fast,
                fastMesh=advect.meshNoOrography5000)

        self.btfLinearUpwindCollated = tfAdvect.collated(
                'tfAdvect-btf-linearUpwind-collated',
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    SchaerAdvectCollated.Test('tfAdvect-btf-5000-linearUpwind', 5000,     advect.meshBtf5000_6000m, timestep=40),
                    SchaerAdvectCollated.Test('tfAdvect-btf-2500-linearUpwind', 2500,     advect.meshBtf2500_6000m, timestep=20),
                    SchaerAdvectCollated.Test('tfAdvect-btf-2000-linearUpwind', 2000,     advect.meshBtf2000_6000m, timestep=16),
                    SchaerAdvectCollated.Test('tfAdvect-btf-1250-linearUpwind', 1250,     advect.meshBtf1250_6000m, timestep=10),
                    SchaerAdvectCollated.Test('tfAdvect-btf-1000-linearUpwind', 1000,     advect.meshBtf1000_6000m, timestep=8),
                    SchaerAdvectCollated.Test('tfAdvect-btf-667-linearUpwind',  1000/3*2, advect.meshBtf667_6000m,  timestep=5),
                    SchaerAdvectCollated.Test('tfAdvect-btf-500-linearUpwind',  500,      advect.meshBtf500_6000m,  timestep=4),
                    SchaerAdvectCollated.Test('tfAdvect-btf-333-linearUpwind',  1000/3,   advect.meshBtf333_6000m,  timestep=2.5),
                    SchaerAdvectCollated.Test('tfAdvect-btf-250-linearUpwind',  250,      advect.meshBtf250_6000m,  timestep=2)
        ])

        self.btfCubicFitCollated = tfAdvect.collated(
                'tfAdvect-btf-cubicFit-collated',
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    SchaerAdvectCollated.Test('tfAdvect-btf-5000-cubicFit', 5000,     advect.meshBtf5000_6000m, timestep=40),
                    SchaerAdvectCollated.Test('tfAdvect-btf-2500-cubicFit', 2500,     advect.meshBtf2500_6000m, timestep=20),
                    SchaerAdvectCollated.Test('tfAdvect-btf-2000-cubicFit', 2000,     advect.meshBtf2000_6000m, timestep=16),
                    SchaerAdvectCollated.Test('tfAdvect-btf-1250-cubicFit', 1250,     advect.meshBtf1250_6000m, timestep=10),
                    SchaerAdvectCollated.Test('tfAdvect-btf-1000-cubicFit', 1000,     advect.meshBtf1000_6000m, timestep=8),
                    SchaerAdvectCollated.Test('tfAdvect-btf-667-cubicFit',  1000/3*2, advect.meshBtf667_6000m,  timestep=5),
                    SchaerAdvectCollated.Test('tfAdvect-btf-500-cubicFit',  500,      advect.meshBtf500_6000m,  timestep=4),
                    SchaerAdvectCollated.Test('tfAdvect-btf-333-cubicFit',  1000/3,   advect.meshBtf333_6000m,  timestep=2.5),
                    SchaerAdvectCollated.Test('tfAdvect-btf-250-cubicFit',  250,      advect.meshBtf250_6000m,  timestep=2)
        ])

        self.cutCellLinearUpwindCollated = tfAdvect.collated(
                'tfAdvect-cutCell-linearUpwind-collated',
                fvSchemes=os.path.join('src/schaerAdvect/linearUpwind'),
                tests=[
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-5000-linearUpwind', 5000,     advect.meshCutCell5000_6000m, timestep=200),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-2500-linearUpwind', 2500,     advect.meshCutCell2500_6000m, timestep=100),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-2000-linearUpwind', 2000,     advect.meshCutCell2000_6000m, timestep=80),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-1250-linearUpwind', 1250,     advect.meshCutCell1250_6000m, timestep=50),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-1000-linearUpwind', 1000,     advect.meshCutCell1000_6000m, timestep=40),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-667-linearUpwind',  1000/3*2, advect.meshCutCell667_6000m,  timestep=25),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-500-linearUpwind',  500,      advect.meshCutCell500_6000m,  timestep=20),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-333-linearUpwind',  1000/3,   advect.meshCutCell333_6000m,  timestep=12.5),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-250-linearUpwind',  250,      advect.meshCutCell250_6000m,  timestep=10)
        ])

        self.cutCellCubicFitCollated = tfAdvect.collated(
                'tfAdvect-cutCell-cubicFit-collated',
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-5000-cubicFit', 5000,     advect.meshCutCell5000_6000m, timestep=200),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-2500-cubicFit', 2500,     advect.meshCutCell2500_6000m, timestep=100),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-2000-cubicFit', 2000,     advect.meshCutCell2000_6000m, timestep=80),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-1250-cubicFit', 1250,     advect.meshCutCell1250_6000m, timestep=50),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-1000-cubicFit', 1000,     advect.meshCutCell1000_6000m, timestep=40),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-667-cubicFit',  1000/3*2, advect.meshCutCell667_6000m,  timestep=25),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-500-cubicFit',  500,      advect.meshCutCell500_6000m,  timestep=20),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-333-cubicFit',  1000/3,   advect.meshCutCell333_6000m,  timestep=12.5),
                    SchaerAdvectCollated.Test('tfAdvect-cutCell-250-cubicFit',  250,      advect.meshCutCell250_6000m,  timestep=10)
        ])

    def addTo(self, build):
        build.add(self.btfLinearUpwindCollated)
        build.addAll(self.btfLinearUpwindCollated.tests)
        build.add(self.btfCubicFitCollated)
        build.addAll(self.btfCubicFitCollated.tests)
        build.add(self.cutCellLinearUpwindCollated)
        build.addAll(self.cutCellLinearUpwindCollated.tests)
        build.add(self.cutCellCubicFitCollated)
        build.addAll(self.cutCellCubicFitCollated.tests)

