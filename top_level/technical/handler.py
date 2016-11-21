import itertools
from top_level.technical.db import DB

class Handler:

    def nested_loop(date, dict):
        for possible_date in dict.values():
            if((date.conflict(possible_date))):
                return False
        return True

    def possibilities(events):
        possibilities = []

        for cartesian_dates in itertools.product(*events):
            aux = {}
            for date in cartesian_dates:
                test = Handler.nested_loop(date, aux)
                if test == True:
                    aux[DB.search_one(events[0], date.event_id)] = date
                else:
                    aux = {}
                    break
                                     
            possibilities.append(aux)      

        return possibilities

    def incommon(events):
        possibilities = []

        for i in itertools.product(*events):
            aux = {}
            for j, k in enumerate(i):
                aux[DB.search_one(events[0], k.event_id)] = k

            possibilities.append(aux)     

        return possibilities
