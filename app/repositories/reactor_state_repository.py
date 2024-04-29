from pymongo import MongoClient
from models.reactor_state import ReactorState

class ReactorStateRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['reactores_nucleares']
        self.collection = self.db['estados']

    def insert_reactor_state(self, reactor_state):
        self.collection.insert_one(reactor_state.__dict__)

    def get_all_reactor_states(self):
        reactor_states = []
        for item in self.collection.find():
            reactor_state = ReactorState(
                estado=item['estado']
            )
            reactor_states.append(reactor_state)
        return reactor_states
