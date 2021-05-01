DOCUMENTATION

1. Inputs

Introduction:
	Analog inputs can be collected from a wide range of sensors including photocells, joysticks, and potentiometers. The Raspberry pi and the Jetson Nano don't have the ability to read analog signals. They can, however, process digital inputs. This library, along with some circuits equips them with the ability to read analog data.

How It Works:
	Analog sensors can be connected to the Jetson Nano and the Raspberry Pi using the method shown in the image input.png. Note that while the image only demonstrates this connection using a photocell, a similar setup should work for other analog sensors. Note that with the Jetson Nano, an external 3v power source is recommended because the Jetson Nano does not supply the analog circuit with adequate current for sensitive analog readings. This circuit is designed to fill the capacitor to its full capacity. When the capacitor is full, the GPIO pin will detect a high. The time taken to fill the capacitor up since the last time it was filled will be measured and returned by the getTime() function. The lower the resistance from the analog sensor, the faster the capacitor will fill up, and the lower the time for the capacitor to charge fully will be.

For Users:

to import analog input functions from the analog_mod library:
from analog_mod.input import *

to create an analog input object (parameter pin refers to which GPIO pin the circuit is utilizing, parameter lib refers to which GPIO library is being used):
var = AnalogIn(pin, lib)

to get the time it took for the capacitor to charge (Note: this function will often return None if the value is extracted when the capacitor is not completely charged):
getTime()

Line By Line Explanation of input.py:

# for counting time to charge the capacitor
import time

# a class for analog sensors
class AnalogIn:
	# init function, pin takes an integer argument for GPIO pin, lib takes a library argument (can be Jetson.GPIO or RPi.GPIO). Note: the library for the argument needs to be imported before use. Refer to the Test->Inputs folder for examples and demonstrations.
	def __init__(self, pin, lib):
		# GPIO pin
		self.pin = pin
		# indicator to start the counting process
		self.start = 0
		# library being used
		self.lib = lib
		# indicator of which process is being undertaken
		self.process = 0
	# getTime function
	def getTime(self):
		# process 0: preparing to discharge the capacitor
		if self.process == 0:
			self.start = time.time()
			self.lib.setup(self.pin,self.lib.OUT)
			self.process = 1
		# process 1: discharging the capacitor
		if self.process == 1:
			if time.time() - self.start < 0.1:
				self.lib.output(self.pin, 0)
				pass
			else:
				self.process = 2
				self.start = time.time()
				self.lib.setup(self.pin, self.lib.IN)
		# process 2: measuring time to charge the capacitor
		if self.process == 2:
			if self.lib.input(self.pin) == True:
				self.process = 0
				return time.time() - self.start



2. Outputs


