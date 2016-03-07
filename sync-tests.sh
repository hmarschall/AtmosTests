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
	scp -prC ash:~/data/AtmosTests/build/gravityWaves-mesh-cutCell-250m-200dz build/
	scp -prC ash:~/data/AtmosTests/build/gravityWaves-mesh-cutCell-250m-150dz build/
}

function gravityWaves {
	rm -r build/gravityWaves-*
	sampleLine gravityWaves-btf-250m-500dz ash
	sampleLine gravityWaves-btf-250m-300dz ash
	sampleLine gravityWaves-btf-250m-250dz ash
	sampleLine gravityWaves-btf-250m-200dz ash
	sampleLine gravityWaves-btf-250m-150dz ash
	sampleLine gravityWaves-btf-250m-125dz ash
	sampleLine gravityWaves-btf-250m-100dz conifer
	sampleLine gravityWaves-btf-250m-75dz conifer
#	sampleLine gravityWaves-btf-250m-50dz jasmin1
	sampleLine gravityWaves-cutCell-250m-500dz ash
	sampleLine gravityWaves-cutCell-250m-300dz ash
	sampleLine gravityWaves-cutCell-250m-250dz ash
	sampleLine gravityWaves-cutCell-250m-200dz ash
	sampleLine gravityWaves-cutCell-250m-150dz ash
	sampleLine gravityWaves-cutCell-250m-125dz ash
	sampleLine gravityWaves-cutCell-250m-100dz ash
#	sampleLine gravityWaves-cutCell-250m-75dz ash
#	sampleLine gravityWaves-cutCell-250m-50dz jasmin1
}

function thermalAdvection {
	rm -r build/thermalAdvection-*
	sampleLine thermalAdvection-btf-250m-500dz conifer
	sampleLine thermalAdvection-btf-250m-300dz conifer
	sampleLine thermalAdvection-btf-250m-250dz conifer
	sampleLine thermalAdvection-btf-250m-200dz conifer
	sampleLine thermalAdvection-btf-250m-150dz conifer
	sampleLine thermalAdvection-btf-250m-125dz conifer
	sampleLine thermalAdvection-btf-250m-100dz conifer
	sampleLine thermalAdvection-btf-250m-75dz birch
#	sampleLine thermalAdvection-btf-250m-50dz jasmin1
	sampleLine thermalAdvection-cutCell-250m-500dz conifer
	sampleLine thermalAdvection-cutCell-250m-300dz conifer
	sampleLine thermalAdvection-cutCell-250m-250dz conifer
	sampleLine thermalAdvection-cutCell-250m-200dz conifer
	sampleLine thermalAdvection-cutCell-250m-150dz conifer
	sampleLine thermalAdvection-cutCell-250m-125dz conifer
	sampleLine thermalAdvection-cutCell-250m-100dz conifer
	sampleLine thermalAdvection-cutCell-250m-75dz birch
#	sampleLine thermalAdvection-cutCell-250m-50dz jasmin1
}

#advection
#resting
#gravityWaves
#gravityWaves-meshes
#thermalAdvection
sampleLine gravityWaves-btf-250m-50dz birch
sampleLine gravityWaves-cutCell-250m-50dz birch
