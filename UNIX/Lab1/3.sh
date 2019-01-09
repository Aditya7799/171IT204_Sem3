echo "enter N"
read n

array=()
   
for ((i=0;$i<$n;i++))
do
echo "Enter the Element $i"
read array[$i]
done

sum=0
for ((i=0;$i<$n;i++))
do
# sum=$$sum + ${array[$i]}
sum=$(echo "scale=2;$sum+${array[$i]}"|bc)
done

sum=$(echo "scale=2;$sum/$n"|bc)

echo "the average is $sum"

