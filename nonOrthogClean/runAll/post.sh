#!/bin/bash -e

time=$1

#if [ ! -e $time/dualMesh/enstrophy ]; then
#    writeuvw U
#fi

# post processing
sumFields $time UfDiff $time Uf 0 Uf -scale0 1 -scale1 -1
sumFields $time ExnerDiff $time Exner 0 Exner -scale0 1 -scale1 -1
plotPatchData -time $time ExnerDiff
gv $time/ExnerDiff.eps &

sumFields $time thetaDiff $time theta constant thetaRef -scale0 1 -scale1 -1
plotPatchData -time $time thetaDiff
gv $time/thetaDiff.eps &

plotPatchData -time $time thetaDiffSK
gv $time/thetaDiffSK.eps &

#plotPatchData -time $time U
#gv $time/U.eps &

#plotPatchData -time $time ExnerU
#gv $time/ExnerU.eps &

#plotPatchData -time $time theta
#gv $time/theta.eps &

