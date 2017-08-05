from gpiozero import Motor

max = 1
medium = 0.7


class Astroby:
	"""
	all configuration and interface for Astroby
	L - Left, R - Right
	LW - LeftWheels, RW - RightWheels
	"""

	def __init__(self):
		# wheels and their GPIOpins
		self.L = Motor(5, 6, pwm=True)
		self.R = Motor(19, 26, pwm=True)

		# initial speed
		self.speed = max

		# def __del__(self):
		# 	import RPi.GPIO as GPIO
		# 	GPIO.cleanup()

	def LW_forward(self, pwmvalue=None):
		pwmvalue = self.speed

		self.L.forward(pwmvalue)

	def LW_backward(self, pwmvalue=None):
		pwmvalue = self.speed

		self.L.backward(pwmvalue)

	def LW_stop(self):
		self.L.stop()

	def RW_forward(self, pwmvalue=None):
		pwmvalue = self.speed

		self.R.forward(pwmvalue)

	def RW_backward(self, pwmvalue=None):
		pwmvalue = self.speed

		self.R.backward(pwmvalue)

	def RW_stop(self):
		self.R.stop()

	# control for the wheels together
	def forward(self, pwmvalue=None):
		pwmvalue = self.speed

		self.L_forward(pwmvalue)
		self.R_forward(pwmvalue)

	def backward(self, pwmvalue=None):
		pwmvalue = self.speed

		self.L_backward(pwmvalue)
		self.R_backward(pwmvalue)

	def left(self, pwmvalue=None):
		pwmvalue = self.speed

		self.L_backward(pwmvalue)
		self.R_forward(pwmvalue)

	def right(self, pwmvalue=None):
		pwmvalue = self.speed

		self.R_backward(pwmvalue)
		self.L_forward(pwmvalue)

	def stop(self):
		self.L_stop()
		self.R_stop()

	def toggle_speed(self):
		# toggle current speed of astroby
		self.speed = medium if self.speed == max else max
