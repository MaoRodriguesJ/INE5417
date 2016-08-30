import date

class Event:
	def __init__(self, name, dates, local, author):
		self.name = name
		self.dates = dates
		self.local = local
		self.author = author

date1 = date.Date(1, '19:30', '20:30')
date2 = date.Date(2, '19:30', '20:30')

seccom = Event('palestra1', [date1, date2], 'EPS', 'PET')
print(seccom.dates[1].weekday)