AUDIO_FILES = '/boot/audio/loop.mp3 /boot/audio/win.mp3 /boot/audio/lose.mp3'

SENSOR_PIN = 25
#			G  F   E   D   C   A   B   DP
SEGMENTS = [6, 12, 13, 19, 16, 26, 20, 21]
LATCHES = [7, 8, 11]
A, B, C, D, E, F, G = 1 << 5, 1 << 6, 1 << 4, 1 << 3, 1 << 2, 1 << 1, 1
DIGITS = {
	'-': G,
	'0': A | B | F | E | C | D,
	'1': B | C,
	'2': A | B | G | E | D,
	'3': A | B | G | C | D,
	'4': F | G | B | C,
	'5': A | F | G | V | D,
	'6': A | F | G | C | E | D,
	'7': A | B | C,
	'8': A | B | C | D | E | F | G,
	'9': A | F | B | G | C | D,
	' ': 1 << 7,
}

################################
# Settings
################################
LOW_TH = 10			# rpm to start the music
LOW_TIMEOUT = 3		# how long to hold lowest rpm to start the music

HIGH_TH = 50		# rpm to reach in order to win
HIGH_TIMEOUT = 20	# how long to hold highest rpm to win

BLINK_DELAY = 5		# how fast to hold zeroes while spinning up
BLINK_DELAY1 = 10	# when to revert to blank display


