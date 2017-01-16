#!/bin/bash
set -e
docker build -t hertzsprung/atmos-tests:latest . $@
