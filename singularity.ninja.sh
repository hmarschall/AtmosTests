#!/bin/bash
set -e
singularity exec -e atmostests.img ninja -f generate.ninja $@
singularity exec -e atmostests.img ninja $@
