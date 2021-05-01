import time, math

class Pwm:
	def __init__(self,pin, lib, pulse = 0.02):
		self.pin = pin
		self.pwr = 0
		self.start = 0
		self.process = 0
		self.pulse = pulse
		self.lib = lib
		self.lib.setup(self.pin,self.lib.OUT)
	def setDc(self, pwr):
			
		
		if self.process == 0:
			self.pwr = pwr
			self.pwr*=self.pulse
			self.start = time.time()
			self.process = 1
		if time.time()-self.start<self.pwr:
			self.status = 1
		else:
			self.status = 0
			if time.time()-self.start>=self.pulse:
				self.process = 0
		
		self.lib.output(self.pin,self.status)

class Motor:
	def __init__(self,fd,bk, lib, pulse = 0.02):
		self.spin = [[fd,bk],[0,0]]
		self.pwr = 0
		self.start = 0
		self.process = 0
		self.pulse = pulse
		self.lib = lib
		self.lib.setup(self.spin[0],self.lib.OUT)
		
	def setVel(self, pwr):
			
		
		if self.process == 0:
			self.pwr = pwr
			if self.pwr<0:
				self.spin[1] = [0,1]
			elif self.pwr == 0:
				self.spin[1] = [0,0]
			else:
				self.spin[1] = [1,0]
			
			if self.pwr < -1:
				self.pwr = -1
			elif self.pwr > 1:
				self.pwr = 1
			
			self.pwr = math.fabs(self.pwr)
			self.pwr*=self.pulse
			self.start = time.time()
			self.process = 1
		if time.time()-self.start<self.pwr:
			self.status = 1
		else:
			self.status = 0
			if time.time()-self.start>=self.pulse:
				self.process = 0
		
		self.lib.output(self.spin[0],[self.spin[1][0]*self.status,self.spin[1][1]*self.status])
