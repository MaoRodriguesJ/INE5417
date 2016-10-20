from base import Base
from sqlalchemy import Column, Integer, String

class User(Base):
	__tablename__ = 'user'
	_id = Column(Integer, primary_key=True)
	name = Column(String(250))
	email = Column(String(250))

	def __init__(self, name, email):
		self.name = name
		self.email = email

	def __str__(self):
		return '\n{} \n{}'.format(self.name, self.email)

	def create_user():
		name = input('Choose a name: ')
		email = input('Choose a email: ')
		return User(name, email)
