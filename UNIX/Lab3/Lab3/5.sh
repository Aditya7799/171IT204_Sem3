echo "Kernel name is "
uname -s
echo "\n"

echo "Processor is"
cat /proc/cpuinfo | grep 'model name' | uniq	