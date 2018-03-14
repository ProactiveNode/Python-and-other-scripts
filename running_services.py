import subprocess

def main():
	command = 'service --status-all'

	command = subprocess.Popen([command],stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
	cmdOutput = command.stdout.read()
	cmdList = cmdOutput.split('\n')

	counter = 0
	listServices = []
	for x in range(len(cmdList)):
		if '+' in cmdList[x]:
			counter += 1
			tempSplit = cmdList[x].split()
			listServices.append(tempSplit[3])

	print("There are " + str(counter) + " services running:")
	for i in range(len(listServices)):
		print(listServices[i])

main()
