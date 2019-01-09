echo "Enter marks obtained in UNIX , Java , DSA"
read u
read j 
read d



if [ $u -gt 100 ] || [ $u -lt 0 ]
	then
	echo "invalid input"
	exit
fi

if [ $j -gt 100 ] || [ $j -lt 0 ]
	then
	echo "invalid input"
	exit
fi

if [ $d -gt 100 ] || [ $d -lt 0 ]
	then
	echo "invalid input"
	exit
fi



avg=$(echo "scale =0;($u+$j+$d)/3"|bc)

if [ $avg -gt 70 ]
	then
	echo "Distinction"
elif [ $avg -gt 60 ]
	then
	echo "First Class"
elif [ $avg -gt 50 ]
	then
	echo "Second Class"
elif [ $avg -gt 40 ]
	then
	echo "Third Class"
else
	echo "Fail"
fi

echo $avg