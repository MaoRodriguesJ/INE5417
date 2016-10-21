from main import Session
from hourtable import HourTable
from date import Date
from user import User
from event import Event
from hour import Hour

hours = Session.query(Hour).all()
for i in hours:
	print(i)

hourtable = Session.query(HourTable).first()
for i in hourtable.events:
	print(i)