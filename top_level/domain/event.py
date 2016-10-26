from .hourtable import HourTable
from .user import User

from ..technical.db import Base
from ..technical.mapper import Mapper

from sqlalchemy import Column, Integer, String, ForeignKey, orm
from sqlalchemy.orm import relationship

class Event(Base):
	__tablename__ = 'event'
	_id = Column(Integer, primary_key=True)
	name = Column(String(250))
	local = Column(String(250))
	user_id = Column(Integer, ForeignKey('user._id'))
	user = relationship(User)
	hour_table_id = Column(Integer, ForeignKey('hourtable._id'))
	hour_table = relationship(HourTable)

	def __init__(self, name, local, user):
		self.name = name
		self.local = local
		self.user = user
		self.dates = []

	@orm.reconstructor
	def init_on_load(self):
		self.dates = Mapper.map_event_dates(self._id)
		self.user = Mapper.map_event_user(self._id)


	def __str__(self):
		return '\nEvent Name: {}\nEvent Local: {}\n{}\nPossible dates: {}'.format(
			self.name, self.local, self.user, self.dates)
