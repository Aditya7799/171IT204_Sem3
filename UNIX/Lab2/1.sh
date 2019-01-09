#!/bin/sh

x=0

if (( $1 <= 0 || $2 <= 0))
then
echo "Invalid Input,Please Try Again"
elif [ $1 -gt $2 ]
then
echo "scale=2; $2/$1" | bc
else
echo "scale=2; $1/$2" | bc
fi
