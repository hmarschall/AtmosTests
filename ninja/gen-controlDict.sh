#!/bin/bash
set -e

display_usage() {
	echo -e "Usage: gen-controlDict.sh <endTime> <timestep> <writeInterval>\n"
}

if [ $# -lt 3 ]
then
	display_usage
	exit 1
fi

export endTime=$1
export timestep=$2
export writeInterval=$3

envsubst <&0 >&1
