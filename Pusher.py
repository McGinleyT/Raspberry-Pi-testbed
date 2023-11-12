import os
import datetime
import random

f = open("data.txt", "w")
randomData = random.randbytes(20)
f.write("Thomas McGinley")
f.write("\nRandom data: "+str(randomData))
f.write("\nDate and time: "+str(datetime.datetime.now()))
f.close()

os.system("cd /home/scf/Desktop/Raspberry-Pi-testbed")
os.system("git add data.txt")
os.system('git commit -m "Updated data.txt"')
os.system("git push")
