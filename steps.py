#!/usr/bin/python3
'''
This example uses half steps and will rotate in ether direction
when running this example you define rotation by steps, specify
the direction, speed, and number of steps 
# format = python3 steps.py <direction> <speed> <steps>
# <direction> = f (forward) or r (reverse)
# <speed> = 1000 (1 second)
# <steps> = 1 - 4096 (4096 = one rotation)
# example = python3 steps.py f 25 100
'''
import Adafruit_BBIO.GPIO as GPIO
import time
import sys

# Show info if error
def format_error(msg):
	print (msg)
	print ("<direction> 'f' (forward) or 'r' (reverse)")
	print ("<speed> 1000 (1 second)")
	print ("<steps> 4096 (one rotation)")
	exit()

# Set all pins as output
def initialize_pins(StepPins):
	for pin in StepPins:
		GPIO.setup(pin, GPIO.OUT)

# Set all pins to low
def set_all_pins_low(StepPins):
	for pin in StepPins:
		GPIO.output(pin, GPIO.LOW)

StepPins=["P8_8", "P8_10", "P8_12", "P8_14"]

# Get and test Command Arguments from terminal
try:
	sys.argv[1]
	if sys.argv[1].isalpha():
		direction = sys.argv[1]
	else:
		msg = "Incorrect Direction Setting"
		format_error(msg)
except:
	msg = "Direction Value Missing"
	format_error(msg)

try:
	sys.argv[2]
	if float(sys.argv[2]).is_integer():
		if sys.argv[2].isdigit():
			speed = int(sys.argv[2])/float(1000)
		else:
			msg = "Incorrect Speed Setting"
			format_error(msg)
	else:
		msg = "Incorrect Speed Value. Must be whole number"
		format_error(msg)
except:
	msg = "Speed Value Missing"
	format_error(msg)

try:
	sys.argv[3]
	if float(sys.argv[3]).is_integer():
		if sys.argv[3].isdigit():
			steps = int(sys.argv[3])
		else:
			msg = "Incorrect Step Count"
			format_error(msg)
	else:
		msg = "Incorrect Step Value. Must be whole number"
		format_error(msg)
except:
	msg = "Step Value Missing"
	format_error(msg)

if (direction == "f") or (direction == "r"):
	if direction == "f":
		StepDir = 1
	
	if direction == 'r':
		StepDir = -1
else:
	msg = "Incorrect Direction Input"
	format_error(msg)
	
Seq = [[1,0,0,1],[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1]]
step = 0
StepCount = len(Seq)

# Initialise variables
StepCounter = 0

initialize_pins(StepPins)
set_all_pins_low(StepPins)


# Start main loop
while True:

	for pin in range(0, 4):
		xpin = StepPins[pin]
		if Seq[StepCounter][pin]!=0:
			GPIO.output(xpin, GPIO.HIGH)
		else:
			GPIO.output(xpin, GPIO.LOW)

	if step == steps:
		set_all_pins_low(StepPins)
		exit()
	else:
		StepCounter += StepDir
		time.sleep(speed)
		if (StepCounter>=StepCount):
			step += abs(StepDir)
			StepCounter = 0
		else:
			step += abs(StepDir)
			
		if (StepCounter<0):
			StepCounter = StepCount+StepDir
		
		print (step,)
		print (Seq[StepCounter])
