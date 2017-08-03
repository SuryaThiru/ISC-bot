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

		#buttons and their functions
		self.FORWARD = 0
		self.BACKWARD = 2

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


def run_joypad_event_loop(callback):
	j = Joystick()
	j.handle_que(callback)