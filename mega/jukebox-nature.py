#!/usr/bin/env python
 
import subprocess
from time import sleep
from RPi import GPIO
from datetime import datetime
 
GPIO.setmode(GPIO.BCM)
 
buttons = [ 
	(21, "/boot/audio/sound1.mp3"),
	(20, "/boot/audio/sound2.mp3"),
	(26, "/boot/audio/sound3.mp3"),
	(16, "/boot/audio/sound4.mp3"),
	(19, "/boot/audio/sound5.mp3"),
	(13, "/boot/audio/sound6.mp3"),
]
for pin, _ in buttons:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(04, GPIO.OUT)
GPIO.output(04, GPIO.HIGH)

play = False
while True:
	for pin, sound in buttons:
		if not GPIO.input(pin) and not play:
			print 'playing: ', sound
			play = True
			subprocess.call(['killall', 'mpg123'])
			sleep(.1)
			subprocess.Popen(['mpg123','-a', 'hw:1,0', sound])
			while not GPIO.input(pin):
				pass
			sleep(1)
			while not GPIO.input(pin):
				pass
			play = False
	else:
		sleep(0.1);
