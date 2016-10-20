from hourtable import Hourtable

def user_interaction(user):
	signout = False
	current_hour_table = -2
	while not signout:
		case = input("\n1 Create Hourtable\
					  \n2 Select Hourtable\
					  \n3 Show user and hourtables\
					  \n4 List Events\
					  \n5 Load Premade Events\
					  \n6 Create event\
					  \n7 Possible Combination\
				  	  \n8 In Common Combination\
				  	  \n9 Sign Out\n")

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
			signout = True

exit = False
while not exit:
	