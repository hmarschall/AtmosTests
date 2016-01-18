#!/bin/bash
function sampleLine {
	mkdir -p build/$1/18000
	scp -prC $2:~/data/AtmosTests/build/$1/18000/sampleLine.dat build/$1/18000/
}

function advection {
	rm -r build/advection-*
	scp -prC ash:~/data/AtmosTests/build/advection-* build/
}

function resting {
	rm -r build/resting-*
	scp -prC ash:~/data/AtmosTests/build/resting-* build/
}

function gravityWaves-meshes {
	rm -r build/gravityWaves-mesh-*
	scp -prC ash:~/data/AtmosTests/build/gravityWaves-mesh-cutCell-250m-300dz build/
#	scp -prC ash:~/data/AtmosTests/build/gravityWaves-mesh-cutCell-250m-250dz build/
#	scp -prC ash:~/data/AtmosTests/build/gravityWaves-mesh-cutCell-250m-200dz build/
}

function thermalAdvection {
	rm -r build/thermalAdvection-*
	sampleLine thermalAdvection-btf-250m-500dz ash
	sampleLine thermalAdvection-btf-250m-300dz ash
	sampleLine thermalAdvection-btf-250m-250dz ash
	sampleLine thermalAdvection-btf-250m-200dz ash
	sampleLine thermalAdvection-btf-250m-150dz ash
	sampleLine thermalAdvection-btf-250m-125dz ash
	sampleLine thermalAdvection-btf-250m-100dz ash
	sampleLine thermalAdvection-btf-250m-75dz ash
	sampleLine thermalAdvection-btf-250m-50dz ash
	sampleLine thermalAdvection-cutCell-250m-500dz conifer
	sampleLine thermalAdvection-cutCell-250m-300dz conifer
	sampleLine thermalAdvection-cutCell-250m-250dz conifer
	sampleLine thermalAdvection-cutCell-250m-200dz conifer
	sampleLine thermalAdvection-cutCell-250m-150dz conifer
	sampleLine thermalAdvection-cutCell-250m-125dz conifer
	sampleLine thermalAdvection-cutCell-250m-100dz conifer
	sampleLine thermalAdvection-cutCell-250m-75dz jasmin3
	sampleLine thermalAdvection-cutCell-250m-50dz conifer
}

#advection
resting
#gravityWaves-meshes
#thermalAdvection
