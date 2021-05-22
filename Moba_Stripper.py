import re
import subprocess
nem = re.compile("Name:\s+(.*)\s*$")
val = re.compile("Data:\s+(.*)\s*$")
eitheror = 0
with open ("ree.txt", "r") as reader:
	for line in reader:
		if eitheror == 0:
			match = nem.search(line.strip())
			if match:
				print(match.group(1))
				eitheror = 1
		else:
			ratch = val.search(line.strip())
			if ratch:
				parseme = 'python.exe MobaXtermCipher.py dec -p aaaaaaaa ' + ratch.group(1)
				yolo = subprocess.call(parseme, shell=True )
				print(yolo, end='')
				eitheror = 0;
