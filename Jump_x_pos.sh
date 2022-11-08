#!/bin/bash
tmp=`mktemp -d`
rm x_min.dat
for (( i = 0; i < 1; i++ )); do
for (( j = 0; j <= 9; j++ )); do
for (( k = 0; k <= 9; k++ )); do
for (( l = 0; l <= 9; l++ )); do
for (( m = 0; m <= 9; m++ )); do

t=0.${i}${j}${k}${l}${m}
FILE=i-${i}.${i}${j}${k}${l}${m}.gnu
if [ -f "$FILE" ]; then

awk '$2>=0 && $2<=0.1 {print $2,$1}' i-${i}.${i}${j}${k}${l}${m}.gnu > $tmp/out

Y_max=$(awk 'BEGIN { max=-100} { if($2 > max ) {max = $2};  } END { print max}' $tmp/out)

awk '$2=='$Y_max' {print $1}' $tmp/out > $tmp/out2
X_req=$(awk 'NR==1 {print }' $tmp/out2)

awk '$2>=0 && $2<='$X_req' {print $2,$1}' i-${i}.${i}${j}${k}${l}${m}.gnu > $tmp/out3
Y_min=$(awk 'BEGIN { min= 100} { if($2 < min ) {min = $2};  } END { print min}' $tmp/out3)

awk '$2=='$Y_min' {print $1}' $tmp/out3 > $tmp/out4
X_req1=$(awk 'NR==1 {print }' $tmp/out4)

echo 0.${i}${j}${k}${l}${m} 'Y_min='$Y_min 'X_min='$X_req1
echo 0.${i}${j}${k}${l}${m} $X_req1 >> x_min.dat
fi
done
done
done
done
done

rm -rf $tmp
