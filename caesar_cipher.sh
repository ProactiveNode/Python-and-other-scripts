#!/bin/bash
#Work in Progress
#Tested in Ubuntu 14

echo -n "Do you want to encode[1] or decode[2]: "
read answer

while [[ $answer != "1" && $answer != "2" ]]; do
	echo "***Incorrect Input***"
	echo "Correct input is to enter the number"
	echo -n "Do you want to encode[1] or decode[2]: "
	read answer

done

alphabet=abcdefghijklmnopqrstuvwxyz
if [ $answer == "1" ]; then
	echo -n "Enter the string you would like to encode: "
	read encodeString

	echo -n "Enter the amount you would like to shift: "
	read encodeShift
		

	newAlpha1=${alphabet:encodeShift:${#alphabet}}
	newAlpha2=${alphabet:0:encodeShift}
	newAlpha=$newAlpha1$newAlpha2

	newWord=$( echo $encodeString | tr $alphabet $newAlpha )
	#echo $newAlpha
	echo "Your encrypted word: " $newWord
fi
