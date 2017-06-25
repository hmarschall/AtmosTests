#!/bin/bash
set -e

sudo singularity create --size 2048 atmostests.img
sudo singularity bootstrap atmostests.img Singularity
