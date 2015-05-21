#!/bin/bash
rm -r build/gravityWaves-*
scp -prC jasmin3:~/data/AtmosTests/build/gravityWaves-\* build/
