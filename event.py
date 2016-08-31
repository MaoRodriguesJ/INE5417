import hour
import date

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
		author = input('Who is the author of the event?')
		dates = []
		possible = True
		while possible:
			weekday = input('When is a possible weekday?')
			starthour = hour.Hour(input('When is the start hour?'))
			finishhour = hour.Hour(input('When in the finish hour?'))
			x = date.Date(weekday, starthour, finishhour)
			dates.append(x)
			if input('Any more dates?') == 'yes':
				possible = True
			else:
				possible = False

		return Event(name, dates, local, author)
