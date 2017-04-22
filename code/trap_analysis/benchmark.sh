#!/bin/bash 

bold=$(tput bold)
normal=$(tput sgr0)

echo 
echo =============================================
echo ${bold}General Information${normal} 
echo =============================================
echo USER=$USER
date
echo HOSTNAME=$HOSTNAME
echo 
echo =============================================
echo ${bold}Configure Environment${normal} 
echo =============================================
module load intel
ulimit -S -s 120000

echo 
echo =============================================
echo ${bold}Set OpenMP Environment Variables${normal}
echo =============================================
export OMP_STACKSIZE=100M
export OMP_NUM_THREADS=16
echo OMP_STACKSIZE=$OMP_STACKSIZE
echo OMP_NUM_THREADS=$OMP_NUM_THREADS

echo
echo =============================================
echo ${bold}Build Executable${normal}
echo =============================================
make clean
make trap_omp
make clean

echo 
echo =============================================
echo ${bold}Move to Data Directory${normal}
echo =============================================
cd ../../data
pwd

echo 
echo =============================================
echo ${bold}Run Application${normal}
echo =============================================
num=1
timing_info=""
for i in `seq 1 5`;
do
    START=$(date +%s)
    export OMP_NUM_THREADS=$num
    echo ***Benchmarking with OMP_NUM_THREADS=$OMP_NUM_THREADS***
    ../code/trap_analysis/./trap_omp
    num=$(echo $(( $num * 2 )))
    END=$(date +%s)
    DIFF=$(( $END - $START ))
    timing_info=$timing_info"time (seconds) ./trap_omp $OMP_NUM_THREADS: $DIFF\n"
done   
return_val=$?

echo 
echo =============================================
echo ${bold}Timing Information${normal}
echo =============================================
echo -e $timing_info

echo 
echo =============================================
echo ${bold}Done${normal}
echo =============================================

exit $return_val
