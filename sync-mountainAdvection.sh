#!/bin/bash
MACHINE=ash
rm -rf build/mountainAdvection*
mkdir -p build
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-btf-linearUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-btf-cubicUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-slantedCell-linearUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-slantedCell-cubicUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-cutCell-linearUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-cutCell-cubicUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-btf-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-slantedCell-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-cutCell-linearUpwind-collated build/
