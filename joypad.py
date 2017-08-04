import pygame


class Joystick:
	"""
	joystick controls for astroby
	"""

	def __init__(self):
		pygame.init()
		pygame.joystick.init()
		self.j = pygame.joystick.Joystick(0)
		self.j.init()

		# buttons and their functions
		self.FORWARD = 0
		self.BACKWARD = 2
		self.LEFT = 3
		self.RIGHT = 1
		self.LFORWARD = 4
		self.LBACKWARD = 6
		self.RFORWARD = 5
		self.RBACKWARD = 7
		self.TOGGLE_SPEED = 8

	def handle_que(self, callback):
		"""
		function handles all events generated in the que
		"""

		while True:
			for event in pygame.event.get():
				button = event.__dict__['button']

				if event.type == pygame.JOYBUTTONDOWN and button == self.FORWARD:
					# move bot forward
					print('bot is moving forward')
					callback('forward')

				elif event.type == pygame.JOYBUTTONUP and button == self.FORWARD:
					# stop bot
					print('bot stopped')
					callback('stop')

				elif event.type == pygame.JOYBUTTONDOWN and button == self.BACKWARD:
					# move bot backwards
					print('bot is moving backward')
					callback('backward')

				elif event.type == pygame.JOYBUTTONUP and button == self.BACKWARD:
					# stop bot
					print('bot stopped')
					callback('stop')

				elif event.type == pygame.JOYBUTTONDOWN and button == self.LEFT:
					# move bot backwards
					print('bot is turning left')
					callback('left')

				elif event.type == pygame.JOYBUTTONUP and button == self.LEFT:
					# stop bot
					print('bot stopped turning left')
					callback('stop')

				elif event.type == pygame.JOYBUTTONDOWN and button == self.RIGHT:
					# move bot backwards
					print('bot is turning right')
					callback('right')

				elif event.type == pygame.JOYBUTTONUP and button == self.RIGHT:
					# stop bot
					print('bot stopped turning right')
					callback('stop')

				# left set of wheels
				elif event.type == pygame.JOYBUTTONDOWN and button == self.LFORWARD:
					print('left wheels forward')
					callback('lforward')

				elif event.type == pygame.JOYBUTTONUP and button == self.LFORWARD:
					print('left wheels stop')
					callback('lstop')

				elif event.type == pygame.JOYBUTTONDOWN and button == self.LBACKWARD:
					print('left wheels backward')
					callback('lbackward')

				elif event.type == pygame.JOYBUTTONUP and button == self.LBACKWARD:
					print('left wheels stop')
					callback('lstop')

				# right set of wheels
				elif event.type == pygame.JOYBUTTONDOWN and button == self.RFORWARD:
					print('right wheels forward')
					callback('rforward')

				elif event.type == pygame.JOYBUTTONUP and button == self.RFORWARD:
					print('right wheels stop')
					callback('rstop')

				elif event.type == pygame.JOYBUTTONDOWN and button == self.RBACKWARD:
					print('right wheels backward')
					callback('rbackward')

				elif event.type == pygame.JOYBUTTONUP and button == self.RBACKWARD:
					print('right wheels stop')
					callback('rstop')

				elif event.type == pygame.JOYBUTTONDOWN and button == self.TOGGLE_SPEED:
					print('toggle speed')
					callback('toggle_speed')


def run_joypad_event_loop(callback):
	j = Joystick()
	j.handle_que(callback)
