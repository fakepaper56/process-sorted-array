#!/bin/bash

rt=1000
if [ "$1" == "-r" ]; then
	rt=$2
fi

rt=$(printf '%d' $rt)
perf stat --repeat $rt -e branch-misses,branches ./unsorted
perf stat --repeat $rt -e branch-misses,branches ./sorted
