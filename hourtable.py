import event
import date
import author
import handler

class HourTable:
	def __init__(self, name):
		self.name = name
		self.events = []
		self.common = []
		self.possibilities = []

	def __repr__(self):
		return self.name

	#used for printing
	def list_events(self):
		print('\nHourTable: '+self.name)
		for k in self.events:
			print(k)
		return ''

	def add_event(self):
		self.events.append(event.Event.create_event())

	def check_possibilities(self):
		case_event1 = int(input('Number of first event: '))
		case_event2 = int(input('Number of second event: '))
		possibilities = handler.Handler.possibilities(self.events[case_event1],
													  self.events[case_event2])
		for k in possibilities:
			print(k)

	def check_common(self):
		case_event1 = int(input('Number of first event: '))
		case_event2 = int(input('Number of second event: '))
		common = handler.Handler.incommon(self.events[case_event1],
										  self.events[case_event2])
		for k in common:
			print(k)

	def load_premade(self):
		name1 = local1 = author1 = 'a'
		date1 = date.Date(2, '13:00', '14:00')
		date2 = date.Date(3, '14:00', '15:00')
		dates1 = [date1, date2]
		event1 = event.Event(name1, dates1, local1, author1)

		name2 = local2 = author2 = 'b'
		date3 = date.Date(2, '14:00', '15:00')
		date4 = date.Date(3, '14:00', '15:00')
		dates2 = [date3, date4]
		event2 = event.Event(name2, dates2, local2, author2)

		self.events.append(event1)
		self.events.append(event2)
