import hour
import date
import author

class Event:
	def __init__(self, name, dates, local, author):
		self.name = name
		self.dates = dates
		self.local = local
		self.author = author

	def __str__(self):
		return '\nName: {}\nLocal: {}\nAuthor: {}\nPossible dates: {}'.format(
			self.name, self.local, self.author, self.dates)

	def create_event():
		name = input('What is the name of the event?')
		local = input('What is the local of the event?')
		author_name = input('Who is the author of the event?')
		author_cpf = input('What is the author CPF?')
		author1 = author.Author(author_name, author_cpf)
		dates = []
		possible = True
		while possible:
			weekday = input('When is a possible weekday?')
			starthour = hour.Hour(input('When is the start hour?'))
			finishhour = hour.Hour(input('When in the finish hour?'))
			date1 = date.Date(weekday, starthour, finishhour)
			dates.append(date1)
			if input('Any more dates?') == 'y':
				possible = True
			else:
				possible = False

		return Event(name, dates, local, author1)
