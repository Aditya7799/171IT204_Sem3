#!/bin/sh
r=0
for i in {1..999}
do
r=$i
sum=0
	while [ $r -gt 0 ]
	do
	x=$(($r % 10))
	x=$(($x*$x*$x))
	sum=$(($sum+$x))
	r=$(($r/10))
	done

if [ $sum -eq $i ]
then
echo "$i"
fi
done