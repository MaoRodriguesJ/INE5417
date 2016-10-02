class Author:
	def __init__(self, name, cpf):
		self.name = name
		self.cpf = cpf

	def __str__(self):
		return '(Name:{}, CPF:{})'.format(self.name, self.cpf)