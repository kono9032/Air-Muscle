# -*- coding: utf-8 -*-

import socket
import threading
import serial
import time


from struct import pack, unpack, calcsize

import RPi.GPIO as GPIO

airpresure = 0.0
lengh = 0.0
set_lengh_value = 0.0

input_on_delay = 0
input_off_delay = 0
output_on_delay = 0
output_off_delay = 0


y = ""
ser = serial.Serial(                 
        port='/dev/ttyAMA1',         
        baudrate=9600,               
        parity=serial.PARITY_NONE,      
        stopbits=serial.STOPBITS_ONE,   
        bytesize=serial.EIGHTBITS,        
        timeout=0.2                      
        )

def SerialRead():
	global airpresure,lengh,y
	newcode = ""
	while 1:
		if(ser.inWaiting() > 0):
			msg= ser.read().decode('utf-8')
			if(len(msg)>0):
					for i in range(0, len(msg), 1):
						y = y + msg[i]
						if(msg[i] == "Z"):
							newcode = y
							#print(newcode)
							y = ""
			tmp = newcode.split(',')
			if(len(tmp)>1):
				airpresure = float(tmp[0])
				lengh = float(tmp[1])
			#print(airpresure, lengh)
			
def Relay_control_1():
	try:
		while 1:
			GPIO.output(6, 1)
			time.sleep(input_on_delay)
			GPIO.output(6, 0)
			time.sleep(input_off_delay)

	except KeyboardInterrupt:
		GPIO.cleanup()

def set_lengh():
	global set_lengh_value
	while 1:
		for i in range(0,25):
			set_lengh_value = 18-(i*0.2)
			time.sleep(0.5)

		for i in range(0,25):
			set_lengh_value = 13+(i*0.2)
			time.sleep(0.5)

def make_function(x):
	y = (-0.0837*x*x*x*x) + (4.9478*x*x*x) - (108.18*x*x) + (1029.5*x) - 3539.1
	return y

def main():
	global input_on_delay, input_off_delay, output_on_delay, output_off_delay
	input_off_delay = 2
	input_on_delay = 0.5
	output_on_delay = 0
	output_off_delay = 0
	while 1:
		value = make_function(set_lengh_value)

		if(value > airpresure):
			GPIO.output(13, 0)
			GPIO.output(6, 1)
		else:
			GPIO.output(13, 1)
			GPIO.output(6, 0)
		print(airpresure, value, lengh, set_lengh_value)

if __name__ == '__main__':
	import sys
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)

	name = [SerialRead, Relay_control_1, set_lengh]
	for i in name:
		globals()["{}",format(i)] = threading.Thread(target=i, args=())
		globals()["{}",format(i)].daemon = True
		globals()["{}",format(i)].start()

	main()
	GPIO.cleanup()
	sys.exit()


