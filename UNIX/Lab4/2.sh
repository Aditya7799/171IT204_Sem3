echo "Enter file 1 contents"
echo "Enter two strings"
read a
read b
echo "enter a number"
read d

echo $a |cat >> file1.txt
echo $b |cat >> file1.txt
echo "$d" |cat >> file1.txt


sort file1.txt > sfile1

rm file1.txt




echo ""
echo ""





echo "Enter file 2 contents"
echo "Enter two strings"
read a
read b
echo "enter a number"
read d


echo $a |cat >> file2.txt
echo $b |cat >> file2.txt
echo "$d" |cat >> file2.txt

sort file2.txt > sfile2
rm file2.txt


echo "elements common to file1"
comm -23 sfile1 sfile2
echo ""

echo "elements common to file2"
comm -13 sfile1 sfile2
echo ""

echo "common to both files"
comm -12 sfile1 sfile2
echo ""

echo "changes to be made"
diff sfile1 sfile2


