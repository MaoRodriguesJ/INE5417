from top_level.technical.db import Base, Session

from top_level.domain.date import Date 
from top_level.domain.user import User

from sqlalchemy import Column, Integer, String, ForeignKey, orm
from sqlalchemy.orm import relationship

class Event(Base):
    __tablename__ = 'event'
    _id = Column(Integer, primary_key=True)
    name = Column(String(250))
    local = Column(String(250))
    hourtable_id = Column(Integer, ForeignKey('hourtable._id'))
    user_id = Column(Integer, ForeignKey('user._id'))
    user = relationship("User")

    dates = relationship("Date", backref="event", cascade="all, delete-orphan",
                         single_parent=True)

    def __init__(self, name, local, user):
        self.name = name
        self.local = local
        self.user = user
        self.dates = []

    @orm.reconstructor
    def init_on_load(self):
        self.dates = Session.query(Date).filter(Date.event_id == self._id).all()
        self.user = Session.query(User).filter(User._id == self.user_id).scalar()

    def __str__(self):
        return '\nID: {}\nEvent Name: {}\nEvent Local: {}\n{}\nPossible dates: {}'.format(
                self._id, self.name, self.local, self.user, self.dates)

    def __repr__(self):
        return self.name

    def __iter__(self):
        return iter(self.dates)

    def add_date(self, date):
        self.dates.append(date)

    #testing
    def list_dates(self):
        for i in self.dates:
            print('\nID: {}\nDate: {}'.format(i._id, i))
