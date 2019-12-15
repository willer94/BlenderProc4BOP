#!/bin/bash

export WORKDIR=/media/willer/data/BOP/BlenderProc4BOP/examples/bop

for idx in `seq 15`
do 
	printf "scene: %06d\n" $idx
	output=$(printf "$WORKDIR/output/lm/%06d" ${idx})
	python run.py "$WORKDIR/config.yaml" "/media/willer/data/BOP/bop_models/lm" $output $idx
done
