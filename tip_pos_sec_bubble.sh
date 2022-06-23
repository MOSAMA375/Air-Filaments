#!/bin/bash
tmp=`mktemp -d`

for (( i = 0; i < 1; i++ )); do
for (( j = 0; j < 1; j++ )); do
for (( k = 0; k < 1; k++ )); do
for (( l = 4; l <= 7; l++ )); do

t=${i}.${j}${k}${l}
FILE=i-${i}.${j}${k}${l}.gnu
if [ -f "$FILE" ]; then

awk '$1<=0 && $1>=-0.25 && $2>0 {print $1,$2}' i-${i}.${j}${k}${l}.gnu > $tmp/out

Y_min=$(awk 'BEGIN { min= 100} { if($2 < min ) {min = $2};  } END { print min}' $tmp/out)

awk '$2=='$Y_min' {print $1}' $tmp/out > $tmp/out2
X_req=$(awk 'NR>1 && NR<=2 {print }' $tmp/out2)

awk '$1<=0 && $1>'$X_req' && $2>0  {print $1,$2}' i-${i}.${j}${k}${l}.gnu > $tmp/out
Y_min1=$(awk 'BEGIN { min= 100} { if($2 < min ) {min = $2};  } END { print min}' $tmp/out)

awk '$2=='$Y_min1' {print $1}' $tmp/out > $tmp/out3
X_req1=$(awk 'NR==1 {print }' $tmp/out3)

echo ${i}.${j}${k}${l} 'Y_min='$Y_min1  'X_req='$X_req1
echo  $X_req1 0 0  >> 2r_min.dat
fi
done
done
done
done
