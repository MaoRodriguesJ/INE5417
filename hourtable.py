import event
from user import User
from handler import Handler
from main import Session
from base import Base
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
		self.events.append(event.Event.create_event())

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
