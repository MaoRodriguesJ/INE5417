from top_level.technical.db import Session
from top_level.domain import hourtable, date, user, event, hour

hours = Session.query(hour.Hour).all()
for i in hours:
	print(i)

hourtable = Session.query(hourtable.HourTable).first()
for i in hourtable.events:
	print(i)