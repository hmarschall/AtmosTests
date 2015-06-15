#!/bin/bash
for CASE in $1/processor*; do
	fixProcessorFaceVelocities -case $CASE
done
