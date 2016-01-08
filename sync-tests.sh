#!/bin/bash
function sampleLine {
	mkdir -p build/$1/18000
	scp -prC $2:~/data/AtmosTests/build/$1/18000/sampleLine.dat build/$1/18000/
}

function advection {
	rm -r build/advection-*
	scp -prC birch:~/data/AtmosTests/build/advection-* build/
}

function thermalAdvection {
	rm -r build/thermalAdvection-*
	sampleLine thermalAdvection-btf-250m-500dz jasmin3
	sampleLine thermalAdvection-btf-250m-300dz jasmin3
	sampleLine thermalAdvection-btf-250m-250dz jasmin3
	sampleLine thermalAdvection-btf-250m-200dz jasmin3
	sampleLine thermalAdvection-btf-250m-150dz jasmin3
	sampleLine thermalAdvection-btf-250m-125dz jasmin3
	sampleLine thermalAdvection-btf-250m-100dz jasmin3
	sampleLine thermalAdvection-btf-250m-75dz jasmin3
	sampleLine thermalAdvection-btf-250m-50dz jasmin3
	sampleLine thermalAdvection-cutCell-250m-500dz jasmin3
	sampleLine thermalAdvection-cutCell-250m-300dz jasmin3
	sampleLine thermalAdvection-cutCell-250m-250dz jasmin3
	sampleLine thermalAdvection-cutCell-250m-200dz jasmin3
	sampleLine thermalAdvection-cutCell-250m-150dz jasmin3
	sampleLine thermalAdvection-cutCell-250m-125dz jasmin3
	sampleLine thermalAdvection-cutCell-250m-100dz jasmin3
	sampleLine thermalAdvection-cutCell-250m-75dz jasmin3
	sampleLine thermalAdvection-cutCell-250m-50dz jasmin3
}

advection
