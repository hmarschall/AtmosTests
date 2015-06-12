#!/bin/bash
rm -r build/advection-*
rm -r build/resting-*
rm -r build/gravityWaves-*
scp -prC jasmin3:~/data/AtmosTests/build/advection-\* build/
scp -prC jasmin3:~/data/AtmosTests/build/resting-\* build/
scp -prC jasmin3:~/data/AtmosTests/build/gravityWaves-\* build/
