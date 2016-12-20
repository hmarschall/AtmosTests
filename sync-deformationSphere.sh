#!/bin/bash
MACHINE=ash
rm -rf build/deformationSphere*
mkdir -p build
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-linearUpwind-hex-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-cubicUpwind-hex-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-linearUpwind-quad-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-cubicUpwind-quad-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-cosBells-nondiv-linearUpwind-hex-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-cosBells-nondiv-cubicUpwind-hex-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-cosBells-nondiv-linearUpwind-quad-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-cosBells-nondiv-cubicUpwind-quad-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-cubicUpwind-hex-8 build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-mesh-hex-3 build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-mesh-quad-8 build/
