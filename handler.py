import event
from pprint import pprint

class Handler:
	def __init__(self, events):
		self.events = events

	def possibilities(self):
		possibilities = {}
		for dates1 in self.events[0].dates:
			for dates2 in self.events[1].dates:
				if(not(dates1.conflict(dates2))):
					possibilities[self.events[0].name+' '+dates1.getHuman()] = (
						self.events[1].name+' '+dates2.getHuman())
		return possibilities

event1 = event.Event.createEvent()
event2 = event.Event.createEvent()
handler1 = Handler([event1, event2])
dicionario = handler1.possibilities()

for k in dicionario.keys():
	pprint((k, dicionario[k]))

#THIS IS NOT REALLY WORKING, JUST A TEST WITH TWO EVENTS TO TRY AND ORGANIZE THE
#COMBINATIONS OF RESULTS, ACTUALLY ANY PROGRESS ;(