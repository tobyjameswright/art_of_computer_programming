#!/bin/bash


num1=2166
num2=6099

if [ $num1 -lt $num2 ]
then
	temp=$num1
	num1=$num2
	num2=$temp
fi

remainder=$(($num1 % $num2))

while [ $remainder -gt 0 ]
do
	next_remainder=$(($num2 % $remainder))
	num2=$remainder
	remainder=$next_remainder
done

echo $num2 "is the highest common divisor"
