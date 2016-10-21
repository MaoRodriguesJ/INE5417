class Handler:

	#JUST FOR TESTING (SHOWING CONFLICTS) NEED FULL ALGORITHM IN FINAL PROJECT
	@staticmethod
	def possibilities(event1, event2):
		possible_events = []
		for dates1 in event1.dates:
			for dates2 in event2.dates:
				if(not(dates1.conflict(dates2))):
					possible_events.append('{} {} , {} {}'.format(
						event1.name,
						dates1,
						event2.name,
						dates2))
		return possible_events

	#JUST FOR TESTING (SHOWING CONFLICTS) NEED FULL ALGORITHM IN FINAL PROJECT
	@staticmethod
	def incommon(event1, event2):
		incommon_events = []
		for dates1 in event1.dates:
			for dates2 in event2.dates:
				if((dates1.conflict(dates2))):
					incommon_events.append('{} {} , {} {}'.format(
						event1.name,
						dates1,
						event2.name,
						dates2))
		return incommon_events
