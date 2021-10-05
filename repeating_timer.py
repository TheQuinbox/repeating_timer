import threading

class RepeatingTimer(threading.Thread):
	def __init__(self, interval, function, *args, **kwargs):
		threading.Thread.__init__(self)
		self.interval = interval
		self.function = function
		self.args = args
		self.kwargs = kwargs
		self.stopped = threading.Event()

	def run(self):
		while not self.stopped.wait(self.interval):
			try:
				self.function(*self.args, **self.kwargs)
			except:
				pass

	def stop(self):
		self.stopped.set()
