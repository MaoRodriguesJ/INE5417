from hour import Hour
import date
from user import User
import hourtable
from main import Session
from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, orm
from sqlalchemy.orm import relationship

class Event(Base):
	__tablename__ = 'event'
	_id = Column(Integer, primary_key=True)
	name = Column(String(250))
	local = Column(String(250))
	user_id = Column(Integer, ForeignKey('user._id'))
	user = relationship(User)
	hourtable_id = Column(Integer, ForeignKey('hourtable._id'))
	hourtable = relationship(hourtable.HourTable)

	def __init__(self, name, dates, local, user):
		self.name = name
		self.dates = dates
		self.local = local
		self.user = user

	@orm.reconstructor
	def init_on_load(self):
		self.dates = Session.query(Date).filter(
										 Date.event_id == self._id).all()
		self.user = Session.query(User).filter(
										User._id == self.user_id).one()


	def __str__(self):
		return '\nName: {}\nLocal: {}\nUser: {}\nPossible dates: {}'.format(
			self.name, self.local, self.user, self.dates)

	def create_event():
		name = input('What is the name of the event?')
		local = input('What is the local of the event?')
		user1 = User.create_user()
		dates = []
		possible = True
		while possible:
			weekday = input('When is a possible weekday?')
			starthour = Hour(input('When is the start hour?'))
			finishhour = Hour(input('When in the finish hour?'))
			date1 = date.Date(weekday, starthour, finishhour)
			dates.append(date1)
			if input('Any more dates?') == 'y':
				possible = True
			else:
				possible = False

		return Event(name, dates, local, user1)
