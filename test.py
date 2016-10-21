from top_level.technical.db import Base, Session, Engine
from top_level.domain import hourtable, date, user, event, hour
from date import Date
from user import User
from event import Event
from hour import Hour

Base.metadata.create_all(Engine)

hour_table = hourtable.HourTable(name='test1')
user = User(name='user1', email='email@1')
event = Event(name='event1', local='local1', user=user, hourtable=hour_table)
hour_start = Hour('10:15')
hour_finish = Hour('11:45')
date = Date(weekday=2, start_hour=hour_start, finish_hour=hour_finish, event=event)
Session.add(date)
Session.commit()