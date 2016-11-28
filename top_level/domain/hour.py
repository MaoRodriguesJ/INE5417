from top_level.technical.db import Base

from sqlalchemy import Column, Integer, String

class Hour(Base):
    __tablename__ = 'hour'
    _id = Column(Integer, primary_key=True)
    hour = Column(Integer)
    minute = Column(Integer)

    def __init__(self, hour):
        self.hour = int(hour.split(':')[0])
        self.minute = int(hour.split(':')[1])

    def __gt__(self, other):
        if self.hour >= other.hour:
            if self.hour > other.hour:
                return True
            else:
                if self.minute > other.minute:
                    return True
                else:
                    return False
        else:
            return False

    def __lt__(self, other):
        if self.hour <= other.hour:
            if self.hour < other.hour:
                return True
            else:
                if self.minute < other.minute:
                    return True
                else:
                    return False
        else:
            return False

    def __eq__(self, other):
        return (self.hour == other.hour and self.minute == other.minute)

    def __str__(self):
        return '{}:{}'.format(self.hour, self.minute)
