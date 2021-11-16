import RPi.GPIO as GPIO
import time

def set(led):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led, GPIO.OUT)
	return led
def ON(led):
	GPIO.output(led, True)
	time.sleep(1)
	GPIO.output(led, False)
	time.sleep(1)
def finish():
	GPIO.cleanup()
