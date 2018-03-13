import subprocess

command = 'service --status-all'

command = subprocess.Popen([command],stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
cmdOutput = thing.stdout.read()
cmdList = output.split('\n')

counter = 0
for x in range(len(cmdList)):
	if '+' in final[x]:
		counter += 1

print("There are " + str(counter) + " services running")
