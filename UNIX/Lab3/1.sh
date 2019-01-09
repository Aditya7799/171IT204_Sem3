echo "Enter a path"
read path
x="cat $path"
y="ls $path" 



if [ -f $path ]
	then
	echo "it is a file \n"
	echo "Its contents are :"
	echo ""
	$x




elif [ -d $path ]
	then
	echo "it is a directory\n"
	echo "Its contents are :"
	$y


else
	echo "Please enter valid path in the current directory "



fi



