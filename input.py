import time

class AnalogIn:
	def __init__(self, pin, lib):
		self.pin = pin
		self.start = 0
		self.lib = lib
		self.process = 0
	def getTime(self):
		if self.process == 0:
			self.start = time.time()
			self.lib.setup(self.pin,self.lib.OUT)
			self.process = 1
		if self.process == 1:
			if time.time() - self.start < 0.1:
				self.lib.output(self.pin, 0)
				pass
			else:
				self.process = 2
				self.start = time.time()
				self.lib.setup(self.pin, self.lib.IN)
		if self.process == 2:
			if self.lib.input(self.pin) == True:
				self.process = 0
				return time.time() - self.start
