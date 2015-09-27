#!/bin/bash
#

array=(in*bmp)

for input in "${array[@]}"; do
	echo $input
	python3.4 blind_search.py $input
	python3.4 heuristic_search.py $input
done

echo "Results:"
ls out*bmp


