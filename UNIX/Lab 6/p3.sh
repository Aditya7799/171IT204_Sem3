sort input.txt>output.txt &
pid=$!
echo "pid is : $pid"
kill $pid
ps

