from aupyom import Sampler, Sound
from aupyom.util import example_audio_file
import processing
from threading import Lock
import time
import pigpio
import RPi.GPIO as GPIO 
from datetime import datetime


class Player:
	def __init__(self, files):
		self.sampler = Sampler()
		self._sounds = []
		for i in files:
			self.load(i)
		
	def load(self, fname):
		self._sounds += [Sound.from_file(fname)]
		return len(self._sounds) - 1

	def play(self, index):
		self.sampler.play(self._sounds[index])

	def is_playing(self, index):
		return self._sounds[index].playing

	def stop(self, index=None):
		if index:
			self.sampler.remove(self._sounds[index])
		else:
			for i in self._sounds:
				self.sampler.remove(i)

	def pitch(self, index):
		return self._sounds[index].pitch_shift

	def stretch(self, index):
		return self._sounds[index].stretch_factor

	def sound(self, index):
		return self._sounds[index]
	

class Display:
	SEGMENTS = []
	LATCHES = []
	DIGITS = {
		'-': 0x00,
		'0': 0x00,
		'1': 0x00,
		'2': 0x00,
		'3': 0x00,
		'4': 0x00,
		'5': 0x00,
		'6': 0x00,
		'7': 0x00,
		'8': 0x00,
		'9': 0x00,
	}

	def __init__(self):
		for pin in SEGMENTS + LATCHES:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, GPIO.LOW)
	
	def set(self, number):
		for l, v in zip(self.LATCHES, '###' if number is None else '%03i' % number)
			self._set(l, self.DIGITS.get(v))
		
	def _set(self, latch, pattern):
		if pattern is None:
			pattern = 0x00
			
		binary = '%08b' % pattern
		for pin, b in zip(self.SEGMENTS, binary)
			pigpio.set(pin, b == '1')
		pigpio.set(latch, pigio.HIGH)
		pigpio.set(latch, pigio.LOW)


class LoadingCursor(Display):
	def __init__(self):
		pass

	LOOP = []

	@property
	def is_looping(self):
		return True
	
	def _loop(self):
		while self.is_looping:
			time.sleep(.3):
		
	def start(self):
		pass
		
	def stop(self):
		pass
	

class App:
	SENSOR_PIN = 0
	
	REV_IO = 4
	LOW_TH = 10
	HIGH_TH = 50
	LOW_TIMEOUT = 3
	HIGH_TIMEOUT = 20

	def __init__(self, loop, win, lose)
		GPIO.setmode(GPIO.BCM) 
		self.lock = Lock()

		cursor = LoadingCursor()
		cursor.start()
		
		self.player = Player([loop, win, loose])
		self.player.sounds[0].loop = True
		
		cursor.stop()
		del cursor
		
		self.display = Display()
		self.display.set(None)

		self._counter = 0
		
		GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=self.counter_handler)

	@property
	def counter(self):
		with self.lock:
			_counter, self._counter = self._counter, 0
			return _counter, datetime.now()
			
	def counter_handler(self, pin)
		with self.lock:
			self._counter += 1

	def _win(self):
		self.player.play(1)
		self.player.stop(0)
		time.sleep(10)
		self.player.stop()
		
	def _lose(self):
		self.player.play(2)
		self.player.stop(0)
		time.sleep(10)
		self.player.stop()

	def run(self):
		low_start = None
		high_start = None
		reset = True
		old_revs, start = self.counter()
		while True:
			time.sleep(.1)
			new_revs, time  = self.counter()
			rpm = (new_revs - old_revs) * 60 / (time - start).total_seconds() 
			old_revs, start = new_revs, time
			print("rpm={}".format(rpm))
			self.display.set(rpm)
			
			if reset:
				if rpm == 0:
					low_start, high_start, reset = None, None, False
			else:
				now = datetime.now()
				if rpm > self.LOW_TH:
					if not low_start:
						low_start = now
					
					if (now - low_start).total_seconds() > self.LOW_TIMEOUT:
						if not self.player.is_playing(0):
							self.player.play(0)
						else:
							self.player.stretch(max(1, 1 + min(self.HIGH_TH, rpm) / float(self.HIGH_TH)))

					if rpm > self.HIGH_TH:
						if not high_start:
							high_start = now
							
						if (now - high_start).total_seconds() > self.HIGH_TIMEOUT:
							low_start, high_start, reset = None, None, True
							self._win()
							old_revs, start = self.counter()
				else:
					low_start, high_start = None, None
					if low_start and (now - low_start).total_seconds() > self.LOW_TIMEOUT:
						self._lose()
						old_revs, start = self.counter()

	
if __name__ == '__main__':
	App('/boot/audio/loop.mp3 /boot/audio/win.mp3 /boot/audio/lose.mp3'.split()).run()
	