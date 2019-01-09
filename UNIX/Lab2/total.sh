#!/bin/sh

x=0

if (( $1 <= 0 || $2 <= 0))
then
echo "Invalid Input,Please Try Again"
elif [ $1 -gt $2 ]
then
echo "scale=2; $2/$1" | bc
else
echo "scale=2; $1/$2" | bc
fi
#!/bin/sh

echo "current user is"
whoami
echo "\n"

echo "Home directory is"
echo `$HOME` 
echo "\n"

echo "Todays date is "
date
echo "\n"


echo "Total number of active users"
who --count
echo "\n"


echo "Terminal: $SHLVL"



#!/bin/sh

array=()

for i in {0..4}
do
echo "Enter the Element $i"
read array[$i]
done

for i in {0..4}
do
for j in {0..3}
do
if [ ${array[$j]} -gt ${array[$j+1]} ]
then
temp=${array[$j]}
array[$j]=${array[$j+1]}
array[$j+1]=$temp
fi
done
done




max=${array[4]}
min=${array[0]}
count=1

for j in {0..3}
do
curr=${array[$j]}
if [ ${array[$j+1]} -eq $curr ]
then
((count++))
else
echo "$curr appears $count times"
count=1
fi
done

if [ $count -eq 1 ]
then
echo "${array[4]} appears 1 times"
fi


echo "MAX = $max"
echo "MIN = $min"#!/bin/sh

array=()
pos=0
neg=0
zero=0

for i in {0..9}
do
echo "Enter the Element $i"
read array[$i]
if [ ${array[$i]} -gt 0 ]
then
((pos++))
elif [ ${array[$i]} -lt 0 ]
then
((neg++))
else
((zero++))
fi
done

echo "NUmber of positives = $pos"
echo "NUmber of negatives = $neg"
echo "NUmber of zeros = $zero"

for i in {0..9}
do
for j in {0..8}
do
if [ ${array[$j]} -gt ${array[$j+1]} ]
then
temp=${array[$j]}
array[$j]=${array[$j+1]}
array[$j+1]=$temp
fi
done
done

for i in {0..9}
do
echo "${array[$i]}"
done
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
done#!/bin/sh

echo "Number of files and directories in the current directory \n"
ls -1| wc -l



