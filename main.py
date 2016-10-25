from top_level.technical.db import Base, Session, Engine
from top_level.technical.mapper import Mapper
from top_level.domain import hourtable, date, user, event, hour

def user_operations():

def hour_table_operations():

def event_operations():

if __name__ == '__main__':
	current_hour_table = None
	current_user = None
	exit = False
	while not exit:
	case = input("\n1 User Operations\
				  \n2 HourTable Operations\
				  \n3 Exit\n")


def user_interaction():
	current_hour_table = None
	current_user = None
	exit = False
	while not exit:
		case = input("\n1 Create HourTable\
					  \n2 Select HourTable\
					  \n3 Show Users and HourTables\
					  \n4 List Events From Current HourTable\
					  \n5 Create event At Current HourTable\
					  \n6 Possible Combination\
				  	  \n7 In Common Combination\
				  	  \n8 Exit\n")

		if case == '1':
			x = hourtable.HourTable(input('Choose a name: '))
			user.hourtables.append(x)
			select = input('Select this hourtable?')
			if select == 'y':
				current_hour_table = len(user.hourtables)-1
				print('Current hourtable: '+user.hourtables[current_hour_table].name)
			else:
				if current_hour_table == -2:
					print('Any hourtable selected.')
					current_hour_table = -1
				else:
					print('Your current hourtable is: '+user.hourtables[current_hour_table].name)
		if case == '2':
			if current_hour_table == -2:
				print('\nYou need to create a hourtable first.')
			else:
				name = input('What is the hourtable name?')
				table_found = False
				for i, k in enumerate(user.hourtables):
					if k.name == name:
						current_hour_table = i
						table_found = True
						print('Your current hourtable is: '+user.hourtables[current_hour_table].name)
				if not table_found:
					print('Hourtable not found.')

		if case == '3':
			print(user)

		if case == '4':
			if current_hour_table == -1:
				print('\nYou need to select a hourtable first.')
			elif current_hour_table == -2:
				print('\nYou need to create a hourtable first.')
			else:
				user.hourtables[current_hour_table].list_events()

		if case == '5':
			if current_hour_table == -1:
				print('\nYou need to select a hourtable first.')
			elif current_hour_table == -2:
				print('\nYou need to create a hourtable first.')
			else:
				user.hourtables[current_hour_table].load_premade()

		if case == '6':
			if current_hour_table == -1:
				print('\nYou need to select a hourtable first.')
			elif current_hour_table == -2:
				print('\nYou need to create a hourtable first.')
			else:
				user.hourtables[current_hour_table].add_event()


		if case == '7':
			if current_hour_table == -1:
				print('\nYou need to select a hourtable first.')
			elif current_hour_table == -2:
				print('\nYou need to create a hourtable first.')
			else:
				user.hourtables[current_hour_table].check_possibilities()

		if case == '8':
			if current_hour_table == -1:
				print('\nYou need to select a hourtable first.')
			elif current_hour_table == -2:
				print('\nYou need to create a hourtable first.')
			else:
				user.hourtables[current_hour_table].check_common()

		if case == '9':
			exit = True
