#!/bin/bash
for t in $(ls); do
	sumFields -scale0 1 -scale1 -1 $t thetaf_diff $t thetaf 0 thetaf
done
