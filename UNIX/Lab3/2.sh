echo "Enter File1"
read File1
echo "Enter File2"
read File2



if [ -f $File1 -a -f $File2 ]
then
echo "Both exist "
cat $File2 >> $File1


fi


