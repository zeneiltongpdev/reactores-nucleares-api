from pymongo import MongoClient
from models.location import Location

class LocationRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['reactores_nucleares']
        self.collection = self.db['ubicaciones']

    def insert_location(self, location):
        self.collection.insert_one(location.__dict__)

    def get_all_locations(self):
        locations = []
        for item in self.collection.find():
            location = Location(
                country=item['country'],
                city=item['city']
            )
            locations.append(location)
        return locations
