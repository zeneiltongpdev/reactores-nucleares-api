from repositories.reactor_repository import ReactorRepository
from models.reactor import Reactor

class ReactorServices:
    def __init__(self):
        self.repository = ReactorRepository()

    def create_reactor(self, data):
        reactor = Reactor(**data)  # Aqui criamos uma instância de Reactor a partir dos dados fornecidos
        reactor_id = self.repository.create_reactor(reactor)
        return reactor_id

    def insert_reactor(self, data):
        return self.repository.insert_reactor(data)

    def get_all_reactors(self):
        return self.repository.get_all_reactors()

    def get_reactor_by_id(self, reactor_id):
        return self.repository.get_reactor_by_id(reactor_id)

    def get_reactor_by_name(self, reactor_name):
        return self.repository.get_reactor_by_name(reactor_name)
    
    def update_reactor(self, reactor_id, data):
        return self.repository.update_reactor(reactor_id, data)

    def delete_reactor(self, reactor_id):
        return self.repository.delete_reactor(reactor_id)
