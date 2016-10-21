from top_level.technical.db import Session
from top_level.domain import hourtable, date, user, event, hour

hourtable = Session.query(hourtable.HourTable).first()
if hourtable is not None:
	for i in hourtable.events:
		print('{} {}'.format(hourtable, i))