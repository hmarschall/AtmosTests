#!/bin/bash
MACHINE=ash
rm -rf build/mountainAdvection*
mkdir -p build
scp -rCp $MACHINE:~/data/AtmosTests/build/mountainAdvection-btf-linearUpwind-1000 build/
