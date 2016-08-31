class Hour:
	def __init__(self, hour):
		self.hour = hour.split(':')[0]
		self.minute = hour.split(':')[1]

	def __gt__(self, other):
		if self.hour >= other.hour:
			if self.hour > other.hour:
				return True
			else:
				if self.minute > other.minute:
					return True
				else:
					return False
		else:
			return False

	def __lt__(self, other):
		if self.hour <= other.hour:
			if self.hour < other.hour:
				return True
			else:
				if self.minute < other.minute:
					return True
				else:
					return False
		else:
			return False

	def __eq__(self, other):
		return (self.hour == other.hour and self.minute == other.minute)

	#for debbuging
	def __str__(self):
		return '{}:{}'.format(self.hour, self.minute)
