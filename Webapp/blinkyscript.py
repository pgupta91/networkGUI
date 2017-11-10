import serial
import time
def myComm(inputValue):
	ser = serial.Serial('COM90', 115200, timeout=0)  # open serial port
	#ser.baudrate = 115200  # set baudrate
	print (ser.name)  # print name of serial port
	if inputValue == "1":
		for x in range(0, 50):
			ser.write(b'\x01')
			time.sleep(.1)
	elif inputValue == "0":
		for x in range(0, 50):
			ser.write(b'\x00')
			time.sleep(.1)
#for x in range(0,50):
#	ser.write(b'\x00') # writes byte 0
#	time.sleep(.1)
#	ser.write(b'\x01')
#	time.sleep(.1)
#ser.close() # close port
