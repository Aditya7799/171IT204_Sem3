a=$1
if [ -f $a ]
	then
	od -bc $a
else
	echo $a | od -bc
fi
