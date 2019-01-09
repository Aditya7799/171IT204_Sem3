echo "Enter binary number "
read binary

echo "The Hexadecimal number is "
echo "obase=16;ibase=2;$binary"|bc
