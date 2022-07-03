#!/bin/bash



for d in */;do
cd $d || { echo "Error"; exit 1; }
col1=molecule
col2=hour
col3=minute
col4=second
echo $col1 $col2 $col3 $col4 > summary.txt
counter_tdPcm=0
counter_optPcm=0
for file in *.out;do
  if grep -q 'Excitation' $file ;then
    echo " TD-DFT/PCM calculation detected"
    echo "Plotting results"
    let counter_tdPcm++
    python3 uvvis.py $file
    h=$(awk '/cpu time/ {print$6}' $file)
    m=$(awk '/cpu time/ {print$8}' $file)
    s=$(awk '/cpu time/ {print$10}' $file)
    cwd=$(pwd)
    mol=$(echo $file | cut -f 1 -d '.')
  echo $mol $h $m $s>> summary.txt
  elif grep -q 'Stationary point found' $file; then
    let counter_optPcm++
    echo "Optimization completed for $file"
    else
      echo "None of the two"
  fi
done
cd ..;
echo " There are $counter_tdPcm TD-DFT/PCM calculation in $cwd"
echo " There are $counter_optPcm OPT/PCM calculation in $cwd"
done

