#!/bin/bash
set -e
make build/horizontalAdvection-btf-{linear,cubic}Upwind-collated/10000/l{2,inf}errorT.txt
