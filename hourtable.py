import event
import handler

class HourTable:
	def __init__(self):
		self.events = []

#main
exit = False
hour_table = HourTable()
while not exit:
	case = input('\n1 Create event\n2 List events\n3 Check conflict\n4 Exit\n')
	if case == '1':
		hour_table.events.append(event.Event.create_event())
	if case == '2':
		for k in hour_table.events:
			print(k)
	if case == '3':
		handler_test = handler.Handler()
		case_event1 = int(input('Number of first event: '))
		case_event2 = int(input('Number of second event: '))
		handler_test.possibilities(hour_table.events[case_event1],
									hour_table.events[case_event2])
		for k in handler_test.possible_events:
			print(k)

	if case == '4':
		exit = True