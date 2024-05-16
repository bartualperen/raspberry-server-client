import os
import time
import csv

def measure_temp():
	temp = os.popen("vcgencmd measure_temp").readline()
	return (temp.replace("temp=",""))

	
f = open("testn.csv", "w", newline="")
wc = csv.writer(f)


while True:
	wc.writerow([measure_temp()])
	print(measure_temp())
	time.sleep(1)


f.close()
