#!/bin/bash
rm -r build/thermalAdvection-*

function sampleLine {
	mkdir -p build/$1/18000
	scp -prC $2:~/data/AtmosTests/build/$1/18000/sampleLine.dat build/$1/18000/
}

sampleLine thermalAdvection-btf-250m-500dz jasmin3
sampleLine thermalAdvection-btf-250m-300dz jasmin3
sampleLine thermalAdvection-btf-250m-250dz jasmin3
sampleLine thermalAdvection-btf-250m-200dz jasmin3
sampleLine thermalAdvection-btf-250m-150dz jasmin3
sampleLine thermalAdvection-btf-250m-125dz jasmin3
sampleLine thermalAdvection-btf-250m-100dz jasmin3
sampleLine thermalAdvection-btf-250m-75dz jasmin3
sampleLine thermalAdvection-btf-250m-50dz jasmin3
sampleLine thermalAdvection-cutCell-250m-500dz conifer
sampleLine thermalAdvection-cutCell-250m-300dz conifer
sampleLine thermalAdvection-cutCell-250m-250dz conifer
sampleLine thermalAdvection-cutCell-250m-200dz conifer
sampleLine thermalAdvection-cutCell-250m-150dz conifer
sampleLine thermalAdvection-cutCell-250m-125dz conifer
sampleLine thermalAdvection-cutCell-250m-100dz conifer
sampleLine thermalAdvection-cutCell-250m-75dz conifer
