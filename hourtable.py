from event import Event
from date import Date
from user import User
from handler import Handler
from arquivo_onde_esta_o_base import Base, Session
from sqlalchemy import Column, Integer, String, orm

class HourTable(Base):
	__tablename__ = 'hourtable'
	_id = Column(Integer, primary_key=True)
	name = Column(String(250))

	def __init__(self, name):
		self.name = name
		self.events = []
		self.common = []
		self.possibilities = []

	@orm.reconstructor
	def init_on_load(self):
		self.events = Session.query(Event).filter(
										   Event.hourtable_id == self._id).all()

	def __repr__(self):
		return self.name

	#used for printing
	def list_events(self):
		print('\nHourTable: '+self.name)
		for k in self.events:
			print(k)

	def add_event(self):
		self.events.append(Event.create_event())

	def check_possibilities(self):
		case_event1 = int(input('Number of first event: '))
		case_event2 = int(input('Number of second event: '))
		possibilities = Handler.possibilities(self.events[case_event1],
													  self.events[case_event2])
		for k in possibilities:
			print(k)

	def check_common(self):
		case_event1 = int(input('Number of first event: '))
		case_event2 = int(input('Number of second event: '))
		common = Handler.incommon(self.events[case_event1],
										  self.events[case_event2])
		for k in common:
			print(k)

	def load_premade(self):
		name1 = local1 = 'a'
		date1 = Date(2, '13:00', '14:00')
		date2 = Date(3, '14:00', '15:00')
		dates1 = [date1, date2]
		user1 = User('a', 'a@a.com')
		event1 = Event(name1, dates1, local1, user1)

		name2 = local2 = 'b'
		date3 = Date(2, '14:00', '15:00')
		date4 = Date(3, '14:00', '15:00')
		dates2 = [date3, date4]
		user2 = User('b', 'b@b.com')
		event2 = Event(name2, dates2, local2, user2)

		self.events.append(event1)
		self.events.append(event2)
