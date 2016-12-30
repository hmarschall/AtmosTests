#!/bin/bash
MACHINE=ash
rm -rf build/horizontalAdvection*
mkdir -p build

scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/horizontalAdvection-btf-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/horizontalAdvection-btf-cubicUpwind-collated build/
