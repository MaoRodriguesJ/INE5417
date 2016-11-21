from top_level.technical.handler import Handler
from top_level.technical.db import Base, Session

from top_level.domain.event import Event

from sqlalchemy import Column, Integer, String, orm
from sqlalchemy.orm import relationship

class HourTable(Base):
    __tablename__ = 'hourtable'
    _id = Column(Integer, primary_key=True)
    name = Column(String(250))

    events = relationship("Event", backref="hourtable",
                          cascade="all, delete-orphan", single_parent=True)

    def __init__(self, name):
        self.name = name
        self.events = []

    @orm.reconstructor
    def init_on_load(self):
        self.events = Session.query(Event).filter(Event.hourtable_id == self._id).\
                      all()

    def __repr__(self):
        return 'HourTable Name: {}'.format(self.name)

    def add_event(self, event):
        self.events.append(event)

    def check_possibilities(self):
        return Handler.possibilities(self.events)

    def check_common(self):
        return Handler.incommon(self.events)

    #used for printing and testing
    def list_events(self):
        print('\nHourTable: '+self.name)
        for k in self.events:
            print(k)
