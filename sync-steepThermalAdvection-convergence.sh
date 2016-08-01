#!/bin/bash
make clean
mkdir build
scp -rCp conifer:~/data/AtmosTests/build/steepThermalAdvection-btf-linearUpwind-collated build/
scp -rCp conifer:~/data/AtmosTests/build/steepThermalAdvection-btf-cubicUpwind-collated build/
scp -rCp conifer:~/data/AtmosTests/build/steepThermalAdvection-slantedCell-linearUpwind-collated build/
scp -rCp conifer:~/data/AtmosTests/build/steepThermalAdvection-slantedCell-cubicUpwind-collated build/
