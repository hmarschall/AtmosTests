#!/bin/bash
MACHINE=ash
rm -rf build/horizontalAdvection*
mkdir -p build

scp -rCp $MACHINE:~/data/AtmosTests/build/horizontalAdvection-btf-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/horizontalAdvection-btf-cubicUpwind-collated build/
