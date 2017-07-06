#!/usr/bin/env python
 
import subprocess
from time import sleep
import RPi.GPIO as GPIO
import random
import os

GPIO.setmode(GPIO.BCM)
random.seed()
pins = [21, 20, 26, 16, 19, 13, 12, 06] #, 05, 07, 8, 11, 25, 9, 10, 24]
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
GPIO.setup(04, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.output(04, GPIO.HIGH)
GPIO.output(23, GPIO.LOW)

subprocess.call(['killall', 'mpg123'])
sounds = ['/boot/audio/' + file for file in os.listdir('/boot/audio/') if file.endswith('.mp3')]


def set(s):
	for pin, on in zip(pins, s):
		GPIO.output(pin, GPIO.HIGH if on=='1' else GPIO.LOW)

def lightning():
	print 'flashing'
	N = len(pins)
	for i in range(N):
		set('1' * i + '0' * N)
		sleep(.01)
	set('0' * N)
	sleep(.05)
	set('1' * N)
	sleep(.1)
	set('0' * N)
	sleep(.07)
	set('1' * N)
	sleep(.3)
	set('0' * N)

lightning()
sleep(random.sample([1, 2, 3], 1)[0])
subprocess.Popen(['mpg123', '-a', 'hw:1,0', random.sample(sounds, 1)[0]])
sleep(random.sample([2, 3], 1)[0])
lightning()
sleep(random.sample([4, 5, 6], 1)[0])
lightning()
