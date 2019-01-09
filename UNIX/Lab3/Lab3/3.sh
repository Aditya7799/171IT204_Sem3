echo "Enter the first String"
read String1
echo "Enter the second string"
read String2

echo "Enter Option 1.Not Empty \n 2.Equal \n 3.Palindrome"
read x

case $x in 
1) 
if [ -n $String1 ] 
then
echo "$String1 not Empty"
fi

if [ -z $String2 ]
then
echo "$String2 not Empty"
fi;;
	

	2) if [ $String2 == $String1 ]
		then
		echo "Strings are Equal"
	else
		echo "Strings not equal"
	fi
	;;


	3) if [[ "$(echo "$String1" | rev)" == "$String1" ]]; then
    echo "String 1 is a Palindrome"
    	else
    		echo "String1 Not Palindrome"
		fi

		if [[ "$(echo "$String2" | rev)" == "$String2" ]]; then
    echo "String 2 is a Palindrome"
    	else
    		echo "String2 Not Palindrome"
		fi
		;;


esac




