from .db import Session

class Mapper:

	@staticmethod
	def map_hour_table_events(_id):
		from ..domain.event import Event
		return Session.query(Event).filter(Event.hour_table_id == _id).all()

	@staticmethod
	def map_event_dates(_id):
		from ..domain.date import Date
		return Session.query(Date).filter(Date.event_id == _id).all()

	@staticmethod	
	def map_event_user(_id):
		from ..domain.user import User
		return Session.query(User).filter(User._id == _id).scalar()

	@staticmethod	
	def map_date_start_hour(start_hour_id):
		from ..domain.hour import Hour
		return Session.query(Hour).filter(Hour._id == start_hour_id).scalar()

	@staticmethod	
	def map_date_finish_hour(finish_hour_id):
		from ..domain.hour import Hour
		return Session.query(Hour).filter(Hour._id == finish_hour_id).scalar()
