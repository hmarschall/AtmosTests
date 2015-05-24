#!/bin/bash
rm -r build/gravityWaves-*
rm -r build/resting-*
scp -prC jasmin3:~/data/AtmosTests/build/resting-\* build/
scp -prC jasmin3:~/data/AtmosTests/build/gravityWaves-\* build/
