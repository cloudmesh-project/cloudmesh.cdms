#!/bin/bash
source /home/cc/intel/bin/compilervars.sh intel64
ifort binary_to_text.f90 -o binary_to_text
for filename in cloudmesh.cdms-master/data/*.dat; do
    filename_new="${filename%.*}".txt
    ./binary_to_text < $filename > $filename_new
done
