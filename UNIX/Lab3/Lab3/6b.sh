echo "Enter binary number "
read binary

echo "The decimal number is "
echo "obase=10;ibase=2;$binary"|bc
