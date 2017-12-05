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
	echo "Your encrypted word: " $newWord
fi

if [ $answer == "2" ]; then
	#Gives a list of all possible decoded words with how much it was shifted
	echo -n "Enter the string you would like to decode: "
	read decodeString
	
	COUNTER=0
	NEWCOUNT=${#alphabet}
	while [ $COUNTER -lt ${#alphabet} ]; do
		newReverseAlpha1=${alphabet:$COUNTER:${#alphabet}}
		newReverseAlpha2=${alphabet:0:$COUNTER}
		newReverseAlpha=$newReverseAlpha1$newReverseAlpha2
		
		newReverseWord=$( echo $decodeString | tr $alphabet $newReverseAlpha )

		echo "Shift" $NEWCOUNT": "$newReverseWord
		let "NEWCOUNT--"
		let "COUNTER++"
	done
fi
