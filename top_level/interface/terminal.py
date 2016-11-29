from top_level.technical.db import DB, Session

from top_level.domain.hourtable import HourTable 
from top_level.domain.date import Date
from top_level.domain.user import User 
from top_level.domain.event import Event 
from top_level.domain.hour import Hour

user_obj = User('','')
hourtable_obj = HourTable('')
event_obj = Event('','', user_obj)

date_obj = Date(0, None, None)

def edit_user(user):
    if user == None:
        user = User('','')
        DB.add(user)
    editing = True
    while editing:
        case = input("\n1 Edit Name\
                      \n2 Edit Email\
                      \n3 Return\n")

        if case == '1':
            new_name = input('New name: ')
            user.name = new_name

        if case == '2':
            new_email = input('New email: ')
            user.email = new_email

        if case == '3':
            DB.flush()
            editing = False

    return user

def edit_event(event):
    editing = True
    while editing:
        case = input("\n1 Edit Name\
                      \n2 Edit Local\
                      \n3 Edit User\
                      \n4 Add Date\
                      \n5 List Dates\
                      \n6 Delete Date\
                      \n7 Return\n")
        if case == '1':
            new_name = input('New name: ')
            event.name = new_name

        if case == '2':
            new_local = input('New local: ')
            event.local = new_local

        if case == '3':
            user = edit_user(event.user)
            event.user = user

        if case == '4':
            weekday = input('When is a possible weekday?')
            starthour = Hour(input('When is the start hour?'))
            finishhour = Hour(input('When in the finish hour?'))
            date = Date(weekday, starthour, finishhour)
            event.add_date(date)

        if case == '5':
            event.list_dates()

        if case == '6':
            _id = int(input('Date ID: '))
            date = DB.search_one(date_obj, _id)
            if date is None:
                print('None date found!\n')
            else:
                DB.delete(date)

        if case == '7':
            DB.flush()
            editing = False    

def user_operations(current_user):
    exit = False
    while not exit:
        case = input("\n1 Create User\
                      \n2 List Users\
                      \n3 Change User\
                      \n4 Edit User\
                      \n5 Delete User\
                      \n6 Return\n")

        if case == '1':
            name = input('UserName: ')
            email = input('E-mail: ')
            user = User(name, email)
            DB.add(user)
            current_user = user

        if case == '2':
            for i in DB.search_all(user_obj):
                print('{} - ID = {}\n'.format(i, i._id))

        if case == '3':
            _id = int(input('UserName ID: '))
            user = DB.search_one(user_obj, _id)
            if user is None:
                print('None user found!\n')
            else:
                print('User changed to {}'.format(user.name))
                current_user = user

        if case == '4':
            _id = int(input('UserName ID: '))
            user = DB.search_one(user_obj, _id)
            if user is None:
                print('None user found!\n')
            else:
                edit_user(user)

        if case == '5':
            _id = int(input('UserName ID: '))
            user = DB.search_one(user_obj, _id)
            if user is None:
                print('None user found!\n')
            else:
                DB.delete(user)
                current_user = None

        if case == '6':
            exit = True

    return current_user
        


def hour_table_operations(current_hour_table, current_user):
    exit = False
    while not exit:
        case = input("\n1 Create HourTable\
                      \n2 List HourTables\
                      \n3 Change HourTable\
                      \n4 Edit HourTable\
                      \n5 Delete HourTable\
                      \n6 Event Operations\
                      \n7 Return\n")

        if case == '1':
            name = input('HourTable name: ')
            hour_table = HourTable(name)
            DB.add(hour_table)
            current_hour_table = hour_table

        if case == '2':
            for i in DB.search_all(hourtable_obj):
                print('{} - ID = {}\n'.format(i, i._id))

        if case == '3':
            _id = int(input('HourTable ID: '))
            hour_table = DB.search_one(hourtable_obj, _id)
            if hour_table is None:
                print('None HourTable found!\n')
            else:
                print('HourTable changed to {}'.format(hour_table.name))
                current_hour_table = hour_table

        if case == '4':
            _id = int(input('HourTable ID: '))
            hour_table = DB.search_one(hourtable_obj, _id)
            if hour_table is None:
                print('None HourTable found!\n')
            else:
                new_name = input('New name: ')
                hour_table.name = new_name
                DB.flush()

        if case == '5':
            _id = int(input('HourTable ID: '))
            hour_table = DB.search_one(hourtable_obj, _id)
            if hour_table is None:
                print('None HourTable found!\n')
            else:
                DB.delete(hour_table)
                current_hour_table = None

        if case == '6':
            if current_hour_table is None or current_user is None:
                print('\n Need a User and Hourtable selected to do event operations!')
            else:
                event_operations(current_hour_table, current_user)

        if case == '7':
            exit = True

    return current_hour_table

def event_operations(current_hour_table, current_user):
    exit = False
    while not exit:
        case = input("\n1 Create Event\
                      \n2 List Events\
                      \n3 Edit Event\
                      \n4 Delete Event\
                      \n5 Check In Common\
                      \n6 Check Non Conflicting Possibilities\
                      \n7 Return\n")

        if case == '1':
            name = input('What is the name of the event?')
            local = input('What is the local of the event?')        
            event = Event(name, local, current_user)
            possible = True
            while possible:
                weekday = input('When is a possible weekday?')
                starthour = Hour(input('When is the start hour?'))
                finishhour = Hour(input('When in the finish hour?'))
                date = Date(weekday, starthour, finishhour)
                event.add_date(date)
                DB.add(event)
                if input('Any more dates? [y/n]') == 'y':
                    possible = True
                else:
                    possible = False

            current_hour_table.add_event(event)
            DB.flush()


        if case == '2':
            current_hour_table.list_events()

        if case == '3':
            _id = int(input('Event ID: '))
            event = DB.search_one(event_obj, _id)
            if event is None:
                print('None event found!\n')
            else:
                edit_event(event)

        if case == '4':
            _id = int(input('Event ID: '))
            event = DB.search_one(event_obj, _id)
            if event is None:
                print('None event found!\n')
            else:
                DB.delete(event)

        if case == '5':
            for i in current_hour_table.check_common():
                print(i)

        if case == '6':
            for i in current_hour_table.check_possibilities():
                print(i)

        if case == '7':
            exit = True

def main():
    DB.create();
    current_hour_table = DB.search_first(hourtable_obj)
    current_user = DB.search_first(user_obj)
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
