from aupyom import Sampler, Sound
import multiprocessing
from threading import Lock, Thread
import time
import RPi.GPIO as GPIO 
from itertools import cycle, takewhile
from datetime import datetime

try:
	from settings import *
except:
	from defaults import *

GPIO.setmode(GPIO.BCM) 

class Player(object):
	def __init__(self, files):
		self.sampler = Sampler(44100)
		self._sounds = []
		for i in files:
			self.load(i)
		
	def load(self, fname):
		print('loading', fname)
		self._sounds += [Sound.from_file(fname).resample(44100)]
		return len(self._sounds) - 1

	def play(self, index):
		self.sampler.play(self._sounds[index])

	def is_playing(self, index):
		try:
			return self._sounds[index].playing
		except:
			return False

	def stop(self, index=None):
		try:
			if index:
				self.sampler.remove(self._sounds[index])
			else:
				for i in self._sounds:
					self.sampler.remove(i)
		except:
			pass

	def pitch(self, index, val):
		self._sounds[index].pitch_shift = val

	def stretch(self, index, val):
		self._sounds[index].stretch_factor = val

	def sound(self, index):
		return self._sounds[index]
	

class Display(object):
	def __init__(self):
		for pin in SEGMENTS + LATCHES:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, GPIO.LOW)
		super(Display, self).__init__()
	
	def set(self, number):
		for l, v in zip(LATCHES, '###' if number is None else '{:03}'.format(number)):
			self._set(l, DIGITS.get(v, 0))
		
	def _set(self, latch, pattern):
		GPIO.output(latch, GPIO.HIGH)
		binary = '{:08b}'.format(pattern)
		for pin, b in zip(SEGMENTS, binary):
			GPIO.output(pin, b == '1')
		GPIO.output(latch, GPIO.LOW)


class LoadingCursor(Display, multiprocessing.Process):
	def __init__(self):
		super(LoadingCursor, self).__init__()
		self.event = multiprocessing.Event()
		self.is_looping = True
		self.event.set()

	LOOP  = zip(
		[A, A, A, B, C, D, D, D, E, F] ,
		[0, 1, 2, 2, 2, 2, 1, 0, 0, 0]
	)

	@property
	def is_looping(self):
		return self.event.is_set()
		
	@is_looping.setter
	def is_looping(self, value):
		if value:
			self.event.set()
		else:
			self.event.clear()
	
	def run(self):
		last = 0
		for segment, latch in takewhile(lambda x: self.is_looping, cycle(self.LOOP)):
			if last != latch:
				self._set(LATCHES[last], 0)
			self._set(LATCHES[latch], segment)
			last = latch
			time.sleep(.03)

class App(Thread):
	def __init__(self, files):
		loop, win, lose = files
		self.lock = Lock()

		cursor = LoadingCursor()
		cursor.start()
		
		self.player = Player([loop, win, lose])
		self.player._sounds[0].loop = True

		cursor.is_looping = False
		time.sleep(1)
		del cursor
		
		self.display = Display()
		self.display.set(None)
		self.low_start = None

		self._counter = 0

		GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=self.counter_handler)
		super(App, self).__init__()

	@property
	def counter(self):
		with self.lock:
			_counter, self._counter = self._counter, 0
			return _counter, datetime.now()
			
	def counter_handler(self, pin):
		with self.lock:
			self._counter += 1

	def _loop(self, rpm):
		stretch = max(0.0, STRETCH_MULTIPLIER * min(HIGH_TH, rpm) / float(HIGH_TH))
		print 'looping', stretch
		if not self.player.is_playing(0):
			self.player.play(0)
		self.player.stretch(0, stretch)

	def run(self):
		print 'thread running'
		while True:
			time.sleep(.05)
			if SHOW_RPM:
				self.display.set(int(10 * self.rpm))
			else:
				if self.low_start:
					self.display.set(max(0, int(10 * (HIGH_TIMEOUT - (datetime.now() - self.low_start).total_seconds()))))
				else:
					self.display.set(0)

	def _win(self):
		print 'Winner !'
		self.player.stop()
		self.player.play(1)
		time.sleep(WIN_SOUND_WAIT)
		self.player.stop()
		
	def _lose(self):
		print 'Loser!'
		self.player.stop()
		self.player.play(2)
		time.sleep(LOSE_SOUND_WAIT)
		self.player.stop()

	def go(self):
		self.low_start = None
		self.rpm = 0
		self.start()
		reset = True
		old_revs, start = self.counter
		print 'go is running'
		while True:
			time.sleep(MEASURE_TIME)
			new_revs, timestamp  = self.counter
			self.rpm = new_revs / (timestamp - start).total_seconds()
			old_revs, start = new_revs, timestamp

			now = datetime.now()
			
			if reset and self.rpm > 0:
				continue
			reset = False

			if self.rpm > LOW_TH:
				if not self.low_start:
					print 'Low reached'
					self.low_start = now
				
				self._loop(self.rpm)

				if self.rpm > HIGH_TH:
					print 'High reached'
					self.low_start, reset = None, True
					self._win()
					old_revs, start = self.counter
			if self.low_start and (now - self.low_start).total_seconds() > HIGH_TIMEOUT:
				print 'High reached'
				self.low_start, reset = None, True
				self._lose()
				old_revs, start = self.counter

	
if __name__ == '__main__':
	App(AUDIO_FILES.split()).go()
	
