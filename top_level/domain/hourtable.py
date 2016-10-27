from ..technical.handler import Handler
from ..technical.db import Base, Session
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

	def add_event(self, event):
		self.events.append(event)

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

	#used for printing and testing
	def list_events(self):
		print('\nHourTable: '+self.name)
		for k in self.events:
			print(k)
