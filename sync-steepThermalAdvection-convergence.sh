#!/bin/bash
MACHINE=ash
make clean
mkdir build
scp -rCp $MACHINE:~/data/AtmosTests/build/steepThermalAdvection-btf-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/steepThermalAdvection-btf-cubicUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/steepThermalAdvection-slantedCell-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/steepThermalAdvection-slantedCell-cubicUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/steepThermalAdvection-cutCell-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/steepThermalAdvection-cutCell-cubicUpwind-collated build/
