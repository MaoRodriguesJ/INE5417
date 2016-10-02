import event
import date
import author
import handler

class HourTable:
	def __init__(self):
		self.events = []
		self.common = []
		self.possibilities = []

#main
exit = False
hour_table = HourTable()
while not exit:
	case = input("\n1 Create event\
				  \n2 List events\
				  \n3 Load Premade Events\
				  \n4 Possible Combination\
				  \n5 In Common COmbination\
				  \n6 Exit\n")
	if case == '1':
		hour_table.events.append(event.Event.create_event())

	if case == '2':
		for k in hour_table.events:
			print(k)

	if case == '3':
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

		hour_table.events.append(event1)
		hour_table.events.append(event2)

	if case == '4':
		case_event1 = int(input('Number of first event: '))
		case_event2 = int(input('Number of second event: '))
		possibilities = handler.Handler.possibilities(hour_table.events[case_event1],
									hour_table.events[case_event2])
		for k in possibilities:
			print(k)

	if case == '5':
		case_event1 = int(input('Number of first event: '))
		case_event2 = int(input('Number of second event: '))
		common = handler.Handler.incommon(hour_table.events[case_event1],
								  hour_table.events[case_event2])
		for k in common:
			print(k)

	if case == '6':
		exit = True