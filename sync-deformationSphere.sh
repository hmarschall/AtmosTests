#!/bin/bash
MACHINE=ash
rm -rf build/deformationSphere*
mkdir -p build
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-linearUpwind-hex-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-cubicUpwind-hex-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-linearUpwind-quad-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-cubicUpwind-quad-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-linearUpwind-hex-5 build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-cosBells-nondiv-linearUpwind-hex-5 build/
