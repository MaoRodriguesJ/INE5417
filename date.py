from hour import Hour
from event import Event
from arquivo_onde_esta_o_base import Base, Session
from sqlalchemy import Column, Integer, String, ForeignKey, orm
from sqlalchemy.orm import relationship

class Date(Base):
	__tablename__ = 'date'
	_id = Column(Integer, primary_key=True)
	weekday = Column(Integer)
	start_hour_id = Column(Integer, ForeignKey('hour.id'))
	start_hour = relationship(Hour, foreign_keys=[start_hour_id])
	finish_hour_id = Column(Integer, ForeignKey('hour.id'))
	finish_hour = relationship(Hour, foreign_keys=[finish_hour_id])
	event_id = Column(Integer, ForeignKey('event.id'))
	event = relationship(Event)

	def __init__(self, weekday, start_hour, finish_hour):
		self.weekday = weekday
		self.start_hour = start_hour
		self.finis_hhour = finish_hour

	@orm.constructor
	def init_on_load(self):
		self.start_hour = Session.query(Hour).filter(
											  Hour._id == self.start_hour_id).one()
		self.finish_hour = Session.query(Hour).filter(
											   Hour._id == self.finish_hour_id).one()

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