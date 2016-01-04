#!/bin/bash
rm -r build/advection-*
make build/advection-horizontal-linear-btf/10000/T_diff
make build/advection-horizontal-linear-sleve/10000/T_diff
make build/advection-horizontal-linear-cutCell/10000/T_diff
make build/advection-horizontal-cubicUpwind-btf/10000/T_diff
make build/advection-horizontal-cubicUpwind-sleve/10000/T_diff
make build/advection-horizontal-cubicUpwind-cutCell/10000/T_diff
make build/advection-terrainFollowing-linear-btf/10000/T_diff
make build/advection-terrainFollowing-linear-sleve/10000/T_diff
make build/advection-terrainFollowing-linear-cutCell/10000/T_diff
make build/advection-terrainFollowing-cubicUpwind-btf/10000/T_diff
make build/advection-terrainFollowing-cubicUpwind-sleve/10000/T_diff
make build/advection-terrainFollowing-cubicUpwind-cutCell/10000/T_diff
