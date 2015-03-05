MAKEFLAGS += --no-builtin-rules
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:
.PHONY: clean

clean:
	rm -rf build

include make/globals/Makefile
include make/globals/Makefile-OpenFOAM
include make/executables/Makefile-OpenFOAM
include make/templates/Makefile-FileSystem
include make/templates/Makefile-BlockMesh
include make/templates/Makefile-TerrainFollowingAdvection
include make/Makefile-Advection

