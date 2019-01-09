echo "Enter the Basc Salary"
read b
dp=$(echo "scale=2; .5*$b"|bc)

a=$(echo "scale=2; $b+$dp"|bc)

sal=$(echo "scale =2; 1.36*$a"|bc)

echo "The Salary is $sal"