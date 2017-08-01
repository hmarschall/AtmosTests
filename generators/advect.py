from ninjaopenfoam import BlockMesh, CutCellMesh, TerrainFollowingMesh

import os

class Advect:
    def __init__(self):
        self.meshNoOrography5000 = BlockMesh('advect-mesh-noOrography-5000', os.path.join('src/advect/mesh-noOrography-5000'))
        self.meshNoOrography2500 = BlockMesh('advect-mesh-noOrography-2500', os.path.join('src/advect/mesh-noOrography-2500'))
        self.meshNoOrography2000 = BlockMesh('advect-mesh-noOrography-2000', os.path.join('src/advect/mesh-noOrography-2000'))
        self.meshNoOrography1250 = BlockMesh('advect-mesh-noOrography-1250', os.path.join('src/advect/mesh-noOrography-1250'))
        self.meshNoOrography1000 = BlockMesh('advect-mesh-noOrography-1000', os.path.join('src/advect/mesh-noOrography-1000'))
        self.meshNoOrography667 = BlockMesh('advect-mesh-noOrography-667', os.path.join('src/advect/mesh-noOrography-667'))
        self.meshNoOrography500 = BlockMesh('advect-mesh-noOrography-500', os.path.join('src/advect/mesh-noOrography-500'))
        self.meshNoOrography333 = BlockMesh('advect-mesh-noOrography-333', os.path.join('src/advect/mesh-noOrography-333'))
        self.meshNoOrography250 = BlockMesh('advect-mesh-noOrography-250', os.path.join('src/advect/mesh-noOrography-250'))

        self.meshBtf5000_6000m = TerrainFollowingMesh('advect-mesh-btf-5000-6000m', self.meshNoOrography5000, os.path.join('src/advect/mesh-btf-6000m'))
        self.meshBtf2500_6000m = TerrainFollowingMesh('advect-mesh-btf-2500-6000m', self.meshNoOrography2500, os.path.join('src/advect/mesh-btf-6000m'))
        self.meshBtf2000_6000m = TerrainFollowingMesh('advect-mesh-btf-2000-6000m', self.meshNoOrography2000, os.path.join('src/advect/mesh-btf-6000m'))
        self.meshBtf1250_6000m = TerrainFollowingMesh('advect-mesh-btf-1250-6000m', self.meshNoOrography1250, os.path.join('src/advect/mesh-btf-6000m'))
        self.meshBtf1000_6000m = TerrainFollowingMesh('advect-mesh-btf-1000-6000m', self.meshNoOrography1000, os.path.join('src/advect/mesh-btf-6000m'))
        self.meshBtf667_6000m = TerrainFollowingMesh('advect-mesh-btf-667-6000m', self.meshNoOrography667, os.path.join('src/advect/mesh-btf-6000m'))
        self.meshBtf500_6000m = TerrainFollowingMesh('advect-mesh-btf-500-6000m', self.meshNoOrography500, os.path.join('src/advect/mesh-btf-6000m'))
        self.meshBtf333_6000m = TerrainFollowingMesh('advect-mesh-btf-333-6000m', self.meshNoOrography333, os.path.join('src/advect/mesh-btf-6000m'))
        self.meshBtf250_6000m = TerrainFollowingMesh('advect-mesh-btf-250-6000m', self.meshNoOrography250, os.path.join('src/advect/mesh-btf-6000m'))

        self.createPatchDict = os.path.join('src/advect/createPatchDict')

        self.meshCutCell5000_6000m = CutCellMesh('advect-mesh-cutCell-5000-6000m', os.path.join('src/advect/mesh-cutCell-5000-6000m'), self.createPatchDict)
        self.meshCutCell2500_6000m = CutCellMesh('advect-mesh-cutCell-2500-6000m', os.path.join('src/advect/mesh-cutCell-2500-6000m'), self.createPatchDict)
        self.meshCutCell2000_6000m = CutCellMesh('advect-mesh-cutCell-2000-6000m', os.path.join('src/advect/mesh-cutCell-2000-6000m'), self.createPatchDict)
        self.meshCutCell1250_6000m = CutCellMesh('advect-mesh-cutCell-1250-6000m', os.path.join('src/advect/mesh-cutCell-1250-6000m'), self.createPatchDict)
        self.meshCutCell1000_6000m = CutCellMesh('advect-mesh-cutCell-1000-6000m', os.path.join('src/advect/mesh-cutCell-1000-6000m'), self.createPatchDict)
        self.meshCutCell667_6000m = CutCellMesh('advect-mesh-cutCell-667-6000m', os.path.join('src/advect/mesh-cutCell-667-6000m'), self.createPatchDict)
        self.meshCutCell500_6000m = CutCellMesh('advect-mesh-cutCell-500-6000m', os.path.join('src/advect/mesh-cutCell-500-6000m'), self.createPatchDict)
        self.meshCutCell333_6000m = CutCellMesh('advect-mesh-cutCell-333-6000m', os.path.join('src/advect/mesh-cutCell-333-6000m'), self.createPatchDict)
        self.meshCutCell250_6000m = CutCellMesh('advect-mesh-cutCell-250-6000m', os.path.join('src/advect/mesh-cutCell-250-6000m'), self.createPatchDict)

        self.meshes = [
                self.meshNoOrography5000, self.meshNoOrography2500, self.meshNoOrography2000,
                self.meshNoOrography1250, self.meshNoOrography1000, self.meshNoOrography667,
                self.meshNoOrography500, self.meshNoOrography333, self.meshNoOrography250,
                self.meshBtf5000_6000m, self.meshBtf2500_6000m, self.meshBtf2000_6000m,
                self.meshBtf1250_6000m, self.meshBtf1000_6000m, self.meshBtf667_6000m,
                self.meshBtf500_6000m, self.meshBtf333_6000m, self.meshBtf250_6000m,
                self.meshCutCell5000_6000m, self.meshCutCell2500_6000m, self.meshCutCell2000_6000m,
                self.meshCutCell1000_6000m, self.meshCutCell1250_6000m, self.meshCutCell667_6000m,
                self.meshCutCell500_6000m, self.meshCutCell333_6000m, self.meshCutCell250_6000m
        ]

    def addTo(self, build):
        build.addAll(self.meshes)
