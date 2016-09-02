#!/bin/bash
MACHINE=ash
rm -rf build/mountainAdvection*
mkdir -p build
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-btf-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-btf-cubicUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-slantedCell-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-slantedCell-cubicUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-cutCell-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-cutCell-cubicUpwind-collated build/
