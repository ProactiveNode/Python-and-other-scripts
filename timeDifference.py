def main():
  insertFile = raw_input("Insert file: ")
  insertTime = raw_input("Enter time: ")
  userGuess = {}
  with open(insertFile) as timeFile:
	for line in timeFile:
                lineSplit = line.split()
		            userGuess[lineSplit[0]] = lineSplit[1]
        
main()
