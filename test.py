from top_level.technical.db import Base, Session, Engine
from top_level.technical.mapper import Mapper
from top_level.domain import hourtable, date, user, event, hour

Mapper.create_all()

hour_table = hourtable.HourTable(name='test1')
user = user.User(name='user1', email='email@1')
event = event.Event(name='event1', local='local1', user=user)
event.hour_table = hour_table
hour_start = hour.Hour('10:15')
hour_finish = hour.Hour('11:45')
date = date.Date(weekday=2, start_hour=hour_start, finish_hour=hour_finish)
date.event = event
Session.add(date)
Session.commit()

#Mapper.clear()