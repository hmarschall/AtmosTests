#!/bin/bash
find . -type d -name processor* -exec rm -r {} \;
find . -type d -name 3600 -exec rm -r {} \;
find . -type d -name 7200 -exec rm -r {} \;
find . -type d -name 10800 -exec rm -r {} \;
find . -type d -name 14400 -exec rm -r {} \;
