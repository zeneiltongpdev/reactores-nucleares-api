import csv
from collections import OrderedDict
from models.reactor import Reactor
from pymongo import MongoClient

class ReactorRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['reactores_nucleares']
        self.collection = self.db['reactores']
        self.next_id = 1

    def has_data(self):
        return self.collection.count_documents({}) > 0

    def insert_reactor(self, reactor):
        reactor_id = str(self.next_id)
        reactor.id = reactor_id
        reactor_dict = reactor.__dict__
        reactor_dict_ordered = OrderedDict(reactor_dict)
        reactor_dict_ordered.move_to_end('id', last=False)
        self.collection.insert_one(dict(reactor_dict_ordered))
        self.next_id += 1

    def get_all_reactors(self):
        reactors = []
        for item in self.collection.find():
            reactor = Reactor(
                name=item['nombre'],
                country=item['pais'],
                city=item['ciudad'],
                type=item['tipo'],
                thermal_power_kw=item['potencia_termica_kw'],
                status=item['estado'],
                first_reaction_date=item['fecha_primera_reaccion']
            )
            reactors.append(reactor)
        return reactors
    
    def import_data_csv(self, archivo_csv):
        with open(archivo_csv, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                reactor = Reactor(
                    name=row[0],
                    country=row[1],
                    city=row[2],
                    type=row[3],
                    thermal_power_kw=float(row[4]),
                    status=row[5],
                    first_reaction_date=row[6]
                )
                self.insert_reactor(reactor)
