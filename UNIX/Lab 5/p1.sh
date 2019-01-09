#!/bin/bash
h=` date +"%H" `
m=` date +"%M" `
mi=` echo "($h*60)+$m" | bc `
if [ $mi -lt '720' ];then
	echo "good morning"
elif [ $mi -ge '720' -a $mi -lt '1080' ];then
	echo "good afternoon"
elif [ $mi -ge '1080' -a $mi -lt '1200' ];then
	echo "good evening"
else
	echo "good night"
fi
