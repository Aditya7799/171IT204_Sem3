echo "Kernel name is "
uname -s
echo ""

echo "Processor is"
cat /proc/cpuinfo | grep 'model name' | uniq	