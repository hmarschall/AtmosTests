#!/bin/bash
MACHINE=ash
make clean
mkdir build
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-linearUpwind-hex-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-cubicUpwind-hex-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-linearUpwind-tri-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/deformationSphere-gaussians-nondiv-cubicUpwind-tri-collated build/
