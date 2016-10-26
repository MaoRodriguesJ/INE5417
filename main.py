from top_level.technical.db import Session
from top_level.technical.mapper import Mapper

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
			Session.add(user)
			Session.commit()

		if case == '2':
			for i in Session.query(User).all():
				print('{} - ID = {}\n'.format(i, i._id))

		if case == '3':
			_id = int(input('UserName ID: '))
			user = Session.query(User).filter(User._id == _id).scalar()
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
					  \n5 In Common\
					  \n6 Possible Combination\
					  \n7 Return\n")

		if case == '1':
			name = input('HourTable name: ')
			hour_table = HourTable(name)
			Session.add(hour_table)
			Session.commit()

		if case == '2':
			for i in Session.query(HourTable).all():
				print('{} - ID = {}\n'.format(i, i._id))

		if case == '3':
			_id = int(input('HourTable ID: '))
			hour_table = Session.query(HourTable).\
						 filter(HourTable._id == _id).scalar()
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
			hour_table = Session.query(HourTable).\
						 filter(HourTable._id == current_hour_table._id).scalar()
			print('The session to access the database is not working well yet, '+\
				  'so if this returns a error even tough you know it should not' +\
				  'you can reopen the application that will work.\n')
			hour_table.check_common()

		if case == '6':
			hour_table = Session.query(HourTable).\
						 filter(HourTable._id == current_hour_table._id).scalar()
			print('The session to access the database is not working well yet, '+\
				  'so if this returns a error even tough you know it should not' +\
				  'you can reopen the application that will work.\n')
			hour_table.check_possibilities()

		if case == '7':
			exit = True

	return current_hour_table

def event_operations(current_hour_table, current_user):
	exit = False
	while not exit:
		case = input("\n1 Create Event\
					  \n2 List Events\
					  \n3 Return\n")

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
				date.event = event
				Session.add(date)
				if input('Any more dates?') == 'yes':
					possible = True
				else:
					possible = False
			Session.commit()


		if case == '2':
			events = Session.query(Event).\
					 filter(Event.hour_table_id == current_hour_table._id).all()
			if events is not None:
				for i in events:
					print('{} - ID = {}\n'.format(i, i._id))

			print('If the dates returns an empty list It is because ' +\
				  'We did not learn how to handle sessions into the ' +\
				  'database very well. Try to return to the previous ' +\
				  'menu and come back that will work.\n')

		if case == '3':
			exit = True

if __name__ == '__main__':
	current_hour_table = Session.query(HourTable).first()
	current_user = Session.query(User).first()
	Mapper.create_all();
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
			Mapper.clear_all()

		if case == '4':
			exit =True

		if case == '5':
			for i in Session.query(Date).all():
				print(i)
