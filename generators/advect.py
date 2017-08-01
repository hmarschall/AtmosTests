from ninjaopenfoam import BlockMesh

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

        self.meshes = [
                self.meshNoOrography5000, self.meshNoOrography2500, self.meshNoOrography2000,
                self.meshNoOrography1250, self.meshNoOrography1000, self.meshNoOrography667,
                self.meshNoOrography500, self.meshNoOrography333, self.meshNoOrography250
        ]

    def addTo(self, build):
        build.addAll(self.meshes)
