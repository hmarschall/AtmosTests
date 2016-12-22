#!/bin/bash
set -e
# mesh plots
make build/deformationSphere-mesh-hex-3/constant/polyMesh/points
make build/deformationSphere-mesh-quad-8/constant/polyMesh/points

# convergence
make build/deformationSphere-{gaussians,cosBells}-nondiv-{linear,cubic}Upwind-hex-collated/1.0368e+06/l{2,inf}errorT.txt
make build/deformationSphere-{gaussians,cosBells}-nondiv-{linear,cubic}Upwind-quad-collated/1.0368e+06/l{2,inf}errorT.txt

