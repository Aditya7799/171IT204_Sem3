echo "Enter marks obtained in UNIX , Java , DSA"
read u
read j 
read d

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