#!/bin/bash
MACHINE=ash
rm -rf build/mountainAdvection*
mkdir -p build
# error plots
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-btf-5000-linearUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-btf-5000-cubicUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-cutCell-5000-linearUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-cutCell-5000-cubicUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-slantedCell-5000-linearUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-slantedCell-5000-cubicUpwind-1000 build/

# analytic contours
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-btf-5000-linearUpwind-1000-analyticTracer build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-btf-5000-cubicUpwind-1000-analyticTracer build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-cutCell-5000-linearUpwind-1000-analyticTracer build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-cutCell-5000-cubicUpwind-1000-analyticTracer build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-slantedCell-5000-linearUpwind-1000-analyticTracer build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-slantedCell-5000-cubicUpwind-1000-analyticTracer build/

# error norms for various h0 
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-btf-collated-linearUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-btf-collated-cubicUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-slantedCell-collated-linearUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-slantedCell-collated-cubicUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-cutCell-collated-linearUpwind-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-cutCell-collated-cubicUpwind-1000 build/

# maxdt for various mesh spacings
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-btf-6000-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-slantedCell-6000-linearUpwind-collated build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-cutCell-6000-linearUpwind-collated build/

# mesh plots
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-mesh-btf-5000-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-mesh-cutCell-5000-1000 build/
scp -rCp $MACHINE:~/data/AtmosTests.cubicFit-jcp-2017/build/mountainAdvection-mesh-slantedCell-5000-1000 build/
