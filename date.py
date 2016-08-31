import hour

class Date:
	def __init__(self, weekday, starthour, finishhour):
		self.weekday = weekday
		self.starthour = starthour
		self.finishhour = finishhour

	def __repr__(self):
		return '({}, {}/{})'.format(self.weekday, self.starthour, self.finishhour)

	def conflict(self, date):
		if date.weekday != self.weekday:
			return False
		else:
			if (date.starthour < self.finishhour and
				self.starthour < date.finishhour):
				return True
			else:
				return False
