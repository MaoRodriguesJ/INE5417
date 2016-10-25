from ..technical.handler import Handler
from ..technical.db import Base
from ..technical.mapper import Mapper

from sqlalchemy import Column, Integer, String, orm

class HourTable(Base):
	__tablename__ = 'hourtable'
	_id = Column(Integer, primary_key=True)
	name = Column(String(250))

	def __init__(self, name):
		self.name = name
		self.events = []
		self.workspace = []
		self.common = []
		self.possibilities = []

	@orm.reconstructor
	def init_on_load(self):
		self.events = Mapper.map_hour_table_events(self._id)

	def __repr__(self):
		return 'HourTable Name: {}'.format(self.name)

	#used for printing
	def list_events(self):
		print('\nHourTable: '+self.name)
		for k in self.events:
			print(k)

	#do not know if its going to be like this		
	def add_event(self):
		from .event import Event
		self.events.append(Event.create_event())

	#not going to be like this
	def check_possibilities(self):
		case_event1 = int(input('Number of first event: '))
		case_event2 = int(input('Number of second event: '))
		possibilities = Handler.possibilities(self.events[case_event1],
													  self.events[case_event2])
		for k in possibilities:
			print(k)

	#not going to be like this
	def check_common(self):
		case_event1 = int(input('Number of first event: '))
		case_event2 = int(input('Number of second event: '))
		common = Handler.incommon(self.events[case_event1],
										  self.events[case_event2])
		for k in common:
			print(k)
