#!/bin/bash -ve

rm -rf [0-9]*

# mesh generation
blockMesh
plotPatchData mesh
gv constant/mesh.eps &

# initial conditions
cp init_0/Exner_init constant
cp init_0/theta_init constant
setAtmosProfile

mkdir -p 0
makeSK94perturb

\mv constant/Exner_init 0/Exner
cp init_0/Uf 0
mv constant/theta_init constant/thetaRef

# change Exner BC from fixedValue to fixedFluxBouyantExner
sed -i 's/fixedValue;/fixedFluxBuoyantExner; gradient uniform 0;/g' 0/Exner

sumFields 0 thetaDiff 0 theta constant thetaRef -scale0 1 -scale1 -1
plotPatchData -time 0 thetaDiff
gv 0/thetaDiff.eps &

