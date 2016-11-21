import itertools
from top_level.technical.db import DB

class Handler:

    #JUST SHOWING ALL POSSIBILITIES IN BOTH METHODS

    def possibilities(events):
        possibilities = []

        for i in itertools.product(*events):
            aux = {}
            for j, k in enumerate(i):
                aux[DB.search_one(events[0], k.event_id)] = k

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
