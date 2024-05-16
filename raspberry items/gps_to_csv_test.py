import time
import csv
from pymavlink import mavutil

master = mavutil.mavlink_connection('/dev/ttyS0', baud = 57600)

with open('gps_data.csv', 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(['Timestamp', 'Latitude', 'Longitude', 'Altitude'])
	
	try:
		while True:
			msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
			
			timestamp = time.time()
			latitude = msg.lat / 1e7
			longitude = msg.lon /1e7
			altitude = msg.alt / 1000
			
			csvwriter.writerow([timestamp, latitude, longitude, altitude])
			
			print(f'Time: {timestamp}, Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude}')
			
			time.sleep(1)
			
	except KeyboardInterrupt:
		print("Interrupted, closing the CSV file.")
