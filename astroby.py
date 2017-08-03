from gpiozero import Motor


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

	def LW_forward(self, pwmvalue=1):
		self.LF.forward(pwmvalue)
		self.LR.forward(pwmvalue)

	def LW_reverse(self, pwmvalue=1):
		self.LF.reverse(pwmvalue)
		self.LR.reverse(pwmvalue)

	def LW_stop(self):
		self.LF.stop()
		self.LR.stop()

	def RW_forward(self, pwmvalue=1):
		self.RF.forward(pwmvalue)
		self.RR.forward(pwmvalue)

	def RW_reverse(self, pwmvalue=1):
		self.RF.reverse(pwmvalue)
		self.RR.reverse(pwmvalue)

	def RW_stop(self):
		self.RF.stop()
		self.RR.stop()

	# control for the wheels together
	def forward(self, pwmvalue=1):
		self.LW_forward(pwmvalue)
		self.RW_forward(pwmvalue)

	def reverse(self, pwmvalue=1):
		self.LW_reverse(pwmvalue)
		self.RW_reverse(pwmvalue)

	def stop(self):
		self.LW_stop()
		self.RW_stop()
