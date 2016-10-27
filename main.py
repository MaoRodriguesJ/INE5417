from top_level.technical.db import DB

from top_level.domain.hourtable import HourTable 
from top_level.domain.date import Date
from top_level.domain.user import User 
from top_level.domain.event import Event 
from top_level.domain.hour import Hour

def user_operations(current_user):
	exit = False
	while not exit:
		case = input("\n1 Create User\
					  \n2 List Users\
					  \n3 Change User\
					  \n4 Return\n")

		if case == '1':
			name = input('UserName: ')
			email = input('E-mail: ')
			user = User(name, email)
			DB.add(user)
			current_user = user

		if case == '2':
			for i in DB.search_all(User('','')):
				print('{} - ID = {}\n'.format(i, i._id))

		if case == '3':
			_id = int(input('UserName ID: '))
			user = DB.search_one(User('',''), _id)
			if user is None:
				print('None user found!\n')
			else:
				print('User changed to {}'.format(user.name))
				current_user = user

		if case == '4':
			exit = True

	return current_user
		


def hour_table_operations(current_hour_table, current_user):
	exit = False
	while not exit:
		case = input("\n1 Create HourTable\
					  \n2 List HourTables\
					  \n3 Change HourTable\
					  \n4 Event Operations\
					  \n5 Return\n")

		if case == '1':
			name = input('HourTable name: ')
			hour_table = HourTable(name)
			DB.add(hour_table)
			current_hour_table = hour_table

		if case == '2':
			for i in DB.search_all(HourTable('')):
				print('{} - ID = {}\n'.format(i, i._id))

		if case == '3':
			_id = int(input('HourTable ID: '))
			hour_table = DB.search_one(HourTable(''), _id)
			if hour_table is None:
				print('None HourTable found!\n')
			else:
				print('HourTable changed to {}'.format(hour_table.name))
				current_hour_table = hour_table

		if case == '4':
			if current_hour_table is None or current_user is None:
				print('\n Need a User and Hourtable selcted to do\
					   event operations!')
			else:
				event_operations(current_hour_table, current_user)

		if case == '5':
			exit = True

	return current_hour_table

def event_operations(current_hour_table, current_user):
	exit = False
	while not exit:
		case = input("\n1 Create Event\
					  \n2 List Events\
					  \n3 Check In Common\
					  \n4 Check Non Conflicting Possibilities\
					  \n5 Return\n")

		if case == '1':
			name = input('What is the name of the event?')
			local = input('What is the local of the event?')		
			event = Event(name, local, current_user)
			event.hour_table = current_hour_table
			possible = True
			while possible:
				weekday = input('When is a possible weekday?')
				starthour = Hour(input('When is the start hour?'))
				finishhour = Hour(input('When in the finish hour?'))
				date = Date(weekday, starthour, finishhour)
				event.add_date(date)
				date.event = event
				DB.add(date)
				if input('Any more dates? [y/n]') == 'y':
					possible = True
				else:
					possible = False

			current_hour_table.add_event(event)


		if case == '2':
			current_hour_table.list_events()

		if case == '3':
			current_hour_table.check_common()

		if case == '4':
			current_hour_table.check_possibilities()

		if case == '5':
			exit = True

if __name__ == '__main__':
	DB.create();
	current_hour_table = DB.search_one(HourTable(''), 1)
	current_user = DB.search_one(User('',''), 1)
	exit = False
	while not exit:
		case = input("\n1 User Operations\
					  \n2 HourTable Operations\
					  \n3 Clear DataBase\
					  \n4 Exit\n")
		if case == '1':
			current_user = user_operations(current_user)

		if case == '2':
			current_hour_table = hour_table_operations(current_hour_table, \
													   current_user)

		if case == '3':
			DB.clear()

		if case == '4':
			exit =True
