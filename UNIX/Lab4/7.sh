echo "Enter the size of the diagonal matrix"
read n

array=[]

for((i = 0 ; i< $n ;i++))
do
read array[$i]
done




for((i=0 ; i< $n ;i++))
do
	for((j=0 ; j < $n ; j++))
	do
		if [ $i -eq $j ]
			then
			echo -n "${array[$i]}   "
		else
			echo -n "0   "
		fi
	done
	echo ""
done


