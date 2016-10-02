class User:
	def __init__(self, name, password):
		self.name = name
		self.password = password
		self.hourtables = []

	def __str__(self):
		return '\n{} \n{}'.format(self.name, self.hourtables)

	def create_user():
		name = input('Choose a name: ')
		password = input('Choose a password: ')
		return User(name, password)

	def add_hourtable(self, hourtable):
		self.hourtables.append(hourtable)