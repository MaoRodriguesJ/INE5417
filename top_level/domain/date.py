from .event import Event
from .hour import Hour

from ..technical.db import Base, Session
from sqlalchemy import Column, Integer, String, ForeignKey, orm
from sqlalchemy.orm import relationship

class Date(Base):
	__tablename__ = 'date'
	_id = Column(Integer, primary_key=True)
	weekday = Column(Integer)
	start_hour_id = Column(Integer, ForeignKey('hour._id'))
	start_hour = relationship(Hour, foreign_keys=[start_hour_id])
	finish_hour_id = Column(Integer, ForeignKey('hour._id'))
	finish_hour = relationship(Hour, foreign_keys=[finish_hour_id])
	event_id = Column(Integer, ForeignKey('event._id'))
	event = relationship(Event)

	def __init__(self, weekday, start_hour, finish_hour, event):
		self.weekday = weekday
		self.start_hour = start_hour
		self.finish_hour = finish_hour
		self.event = event

	@orm.reconstructor
	def init_on_load(self):
		self.start_hour = Session.query(Hour).filter(
						  Hour._id == self.start_hour_id).scalar()
		self.finish_hour = Session.query(Hour).filter(
						   Hour._id == self.finish_hour_id).scalar()

	def __repr__(self):
		return '({}, {}/{})'.format(self.weekday, self.start_hour, self.finish_hour)

	def conflict(self, date):
		if date.weekday != self.weekday:
			return False
		else:
			if (date.start_hour < self.finish_hour and
				self.start_hour < date.finish_hour):
				return True
			else:
				return False