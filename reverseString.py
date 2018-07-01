#!/bin/python
#User inputs a string and reverses that string

def reverseString(orgString):
	revString = []
	counter = 1
	for i in list(orgString):
		revString.append(orgString[len(orgString)-counter])
		counter+=1
	print(''.join(revString))

def main():
	userInput = raw_input("Enter word: ")
	reverseString(userInput)

main()
