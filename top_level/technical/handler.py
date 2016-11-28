import itertools
from top_level.technical.db import DB

class Handler:

    @staticmethod
    def in_common_nested_loop(date, dict):
        for possible_date in dict.values():
            if(not(date.conflict(possible_date))):
                return False
        return True

    @staticmethod
    def possibilities_nested_loop(date, dict):
        for possible_date in dict.values():
            if(date.conflict(possible_date)):
                return False
        return True

    @staticmethod
    def possibilities(events):
        possibilities = []

        for cartesian_dates in itertools.product(*events):
            aux = {}
            for date in cartesian_dates:
                test = Handler.possibilities_nested_loop(date, aux)
                if test == True:
                    aux[DB.search_one(events[0], date.event_id)] = date
                else:
                    aux = {}
                    break
                                     
            possibilities.append(aux)      

        return possibilities

    @staticmethod
    def in_common(events):
        in_common = []

        for cartesian_dates in itertools.product(*events):
            aux = {}
            for date in cartesian_dates:
                test = Handler.in_common_nested_loop(date, aux)
                if test == True:
                    aux[DB.search_one(events[0], date.event_id)] = date
                else:
                    aux = {}
                    break
                                     
            in_common.append(aux)      

        return in_common
