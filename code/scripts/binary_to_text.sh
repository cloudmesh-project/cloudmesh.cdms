#!/bin/bash
source /home/cc/intel/bin/compilervars.sh intel64
cdms_scripts=/home/cc/cloudmesh.cdms-master/code/scripts
ifort $cdms_scripts/binary_to_text.f90 -o $cdms_scripts/binary_to_text
for filename in /home/cc/cloudmesh.cdms-master/data/*.dat; do
    filename_new="${filename%.*}".txt
    $cdms_scripts/binary_to_text < $filename > $filename_new
done
