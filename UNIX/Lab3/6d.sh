echo "Enter Hexadecimal number "
read binary

echo "The binary number is "
echo "obase=2;ibase=16;$binary"|bc
