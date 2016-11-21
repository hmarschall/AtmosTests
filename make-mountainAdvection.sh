#!/bin/bash
make build/mountainAdvection-btf-collated-{linear,cubic}Upwind-1000/10000/l{inf,2}errorT.txt
make build/mountainAdvection-cutCell-collated-{linear,cubic}Upwind-1000/10000/l{inf,2}errorT.txt
make build/mountainAdvection-slantedCell-collated-{linear,cubic}Upwind-1000/10000/l{inf,2}errorT.txt
make build/mountainAdvection-btf-6000-{linear,cubic}Upwind-collated/10000/l{2,inf}errorT.txt
make build/mountainAdvection-cutCell-6000-{linear,cubic}Upwind-collated/10000/l{2,inf}errorT.txt
make build/mountainAdvection-slantedCell-6000-{linear,cubic}Upwind-collated/10000/l{2,inf}errorT.txt
make build/mountainAdvection-btf-6000-linearUpwind-collated/0/maxdt.txt
make build/mountainAdvection-cutCell-6000-linearUpwind-collated/0/maxdt.txt
make build/mountainAdvection-slantedCell-6000-linearUpwind-collated/0/maxdt.txt
