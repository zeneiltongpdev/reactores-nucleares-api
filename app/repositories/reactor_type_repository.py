from pymongo import MongoClient
from models.reactor_type import ReactorType

class ReactorTypeRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['reactores_nucleares']
        self.collection = self.db['type']

    def insert_reactor_type(self, reactor_type):
        self.collection.insert_one(reactor_type.__dict__)

    def get_all_reactor_types(self):
        reactor_types = []
        for item in self.collection.find():
            reactor_type = ReactorType(
                type=item['type']
            )
            reactor_types.append(reactor_type)
        return reactor_types
