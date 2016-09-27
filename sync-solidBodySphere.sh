#!/bin/bash
MACHINE=ash
rm -rf build/solidBodySphere*
mkdir -p build
scp -rCp $MACHINE:~/data/AtmosTests/build/solidBodySphere-noTilt-linearUpwind-hex-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/solidBodySphere-noTilt-cubicUpwind-hex-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/solidBodySphere-noTilt-linearUpwind-tri-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/solidBodySphere-noTilt-cubicUpwind-tri-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/solidBodySphere-noTilt-linearUpwind-quad-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/solidBodySphere-noTilt-cubicUpwind-quad-collated build/
