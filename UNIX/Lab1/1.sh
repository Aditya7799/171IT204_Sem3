#!/bin/sh
echo "Enter the Principal"
read p
echo "Enter the Rate"
read r
echo "Enter the time"
read t

si=$(echo "scale=2;$p*$r*$t/100"|bc)
echo "Simple Intrest is: $si"

echo "Enter the radius"
read R
Area=$(echo "scale=2;3.14*$R*$R"|bc)
echo "The Area is $Area"

