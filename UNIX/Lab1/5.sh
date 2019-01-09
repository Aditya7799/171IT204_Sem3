echo "enter the two numbers"
read a
read b
echo "enter the operand +,-,*,/"
read c



result=$(echo "scale=2;$a$c$b"|bc)


echo "The result is $result"

