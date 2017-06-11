from aupyom import Sampler, Sound
from aupyom.util import example_audio_file

class Player:
	def __init__(self, fname='06-Touching_Tongues.mp3'):
		self.sampler = Sampler()
		self.sound = Sound.from_file(fname)

	def play(self):
		self.sampler.play(self.sound)

	def stop(self):
		self.sampler.remove(self.sound)

	@property
	def pitch(self):
		return self.sound.pitch_shift

	@pitch.setter
	def pitch(self, value):
		self.sound.pitch_shift = value

	@property
	def stretch(self):
		return self.sound.stretch_factor

	@stretch.setter
	def stretch(self, value):
		self.sound.stretch_factor = value

