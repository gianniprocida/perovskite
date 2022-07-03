#!/bin/bash



for d in */;do
 cd $d || { echo "Error"; exit 1; }
 sbatch gaussian.job;
 cd ..;
 done
