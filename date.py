class Date:
	def __init__(self, weekday, starthour, finishhour):
		self.weekday = weekday
		self.starthour = starthour
		self.finishhour = finishhour

	def conflict(self, date):
		if(date.weekday != self.weekday):
			return False
		else:
			print('building')