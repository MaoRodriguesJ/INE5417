import event

class Handler:
	def __init__(self):
		self.possible_events = []

	#JUST FOR TESTING (SHOWING CONFLICTS)
	def possibilities(self, event1, event2):
		for dates1 in event1.dates:
			for dates2 in event2.dates:
				if((dates1.conflict(dates2))):
					self.possible_events.append('{} {} , {} {}'.format(
						event1.name,
						dates1,
						event2.name,
						dates2))
