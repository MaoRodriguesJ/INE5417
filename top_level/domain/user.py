from top_level.technical.db import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    _id = Column(Integer, primary_key=True)
    name = Column(String(250))
    email = Column(String(250))

    events = relationship("Event", single_parent=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return 'User Name: {} \nUser E-mail: {}'.format(self.name, self.email)
