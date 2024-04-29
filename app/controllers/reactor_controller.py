from flask import jsonify
from services.reactor_service import ReactorServices

class ReactorController:
    def __init__(self):
        self.service = ReactorServices()

    def insert_reactor(self, reactor_data):
        self.service.insert_reactor(reactor_data)

    def get_all_reactors(self):
        reactors = self.service.get_all_reactors()
        return jsonify([reactor.__dict__ for reactor in reactors])
    
    def get_reactor_by_id(self, reactor_id):
        reactor = self.service.get_reactor_by_id(reactor_id)
        return jsonify(reactor.__dict__)

    def get_reactor_by_names(self, reactor_names):
        reactors = self.service.get_reactors_by_names(reactor_names)
        return jsonify([reactor.__dict__ for reactor in reactors])
    
    def update_reactor(self, reactor_id, reactor_data):
        self.service.update_reactor(reactor_id, reactor_data)

    def delete_reactor(self, reactor_id):
        self.service.delete_reactor(reactor_id)