#!/bin/bash
rm -r build/resting-*
make build/resting-noOrography-low/21600/theta
make build/resting-btf-low/21600/theta
make build/resting-sleve-low/21600/theta
make build/resting-cutCell-low/21600/theta
make build/resting-noOrography-high/21600/theta
make build/resting-btf-high/21600/theta
make build/resting-sleve-high/21600/theta
make build/resting-cutCell-high/21600/theta
