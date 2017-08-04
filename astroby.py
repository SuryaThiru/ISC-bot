from gpiozero import Motor

max = 1
medium = 0.7


class Astroby():
	"""
	all configuration and interface for Astroby
	L - Left, R - Right, F - Front, R - Rear
	LW - LeftWheels, RW - RightWheels
	"""

	def __init__(self):
		# wheels and their GPIOpins
		self.LF = Motor(2, 3, pwm=True)
		self.LR = Motor(17, 27, pwm=True)
		self.RF = Motor(14, 15, pwm=True)
		self.RR = Motor(23, 24, pwm=True)

		# initial speed
		self.speed = 1

		# def __del__(self):
		# 	import RPi.GPIO as GPIO
		# 	GPIO.cleanup()

		def LW_forward(self, pwmvalue=self.speed):
			self.LF.forward(pwmvalue)
			self.LR.forward(pwmvalue)

		def LW_backward(self, pwmvalue=self.speed):
			self.LF.backward(pwmvalue)
			self.LR.backward(pwmvalue)

		def LW_stop(self):
			self.LF.stop()
			self.LR.stop()

		def RW_forward(self, pwmvalue=self.speed):
			self.RF.forward(pwmvalue)
			self.RR.forward(pwmvalue)

		def RW_backward(self, pwmvalue=self.speed):
			self.RF.backward(pwmvalue)
			self.RR.backward(pwmvalue)

		def RW_stop(self):
			self.RF.stop()
			self.RR.stop()

		# control for the wheels together
		def forward(self, pwmvalue=self.speed):
			self.LW_forward(pwmvalue)
			self.RW_forward(pwmvalue)

		def backward(self, pwmvalue=self.speed):
			self.LW_backward(pwmvalue)
			self.RW_backward(pwmvalue)

		def left(self, pwmvalue=self.speed):
			self.LW_backward(pwmvalue)
			self.RW_forward(pwmvalue)

		def right(self, pwmvalue=self.speed):
			self.RW_backward(pwmvalue)
			self.LW_forward(pwmvalue)

		def stop(self):
			self.LW_stop()
			self.RW_stop()

		def toggle_speed(self):
			# toggle current speed of astroby
			self.speed = medium if self.speed == max else max
