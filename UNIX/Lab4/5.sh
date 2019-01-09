#!/bin/bash 

read -p "Enter the matrix order [mxn] : " t 
m=${t:0:1} 
n=${t:2:1} 

echo "Enter the elements for first matrix" 
for i in `seq 0 $(($m-1))` 
do 
for j in `seq 0 $(($n-1))` 
 do 
     read x[$(($n*$i+$j))] 
done 
done 

echo "Enter the elements for second matrix" 
for i in `seq 0 $(($m-1))` 
do 
for j in `seq 0 $(($n-1))` 
do 
    read y[$(($n*$i+$j))] 
    z[$(($n*$i+$j))]=$((${x[$(($n*$i+$j))]}+${y[$(($n*$i+$j))]})) 
done 
done 

echo "Matrix after addition is"  
for i in `seq 0 $(($m-1))` 
do 
for j in `seq 0 $(($n-1))` 
do 
    echo -ne "${z[$(($n*$i+$j))]}\t" 
done 
echo -e "\n" 
done 

exit 0 