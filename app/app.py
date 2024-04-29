from flask import Flask,jsonify, request
from bson import ObjectId
from flask_swagger_ui import get_swaggerui_blueprint
from controllers.reactor_controller import ReactorController
from repositories.reactor_repository import ReactorRepository

app = Flask(__name__)
reactor_controller = ReactorController()
reactor_repository = ReactorRepository()

archivo_csv = 'IAEA_Reactores_Nucleares_Investigacion.csv'
if not reactor_repository.has_data():
    print('Importing CSV data for Mongodb ...')
    reactor_repository.import_data_csv(archivo_csv)
else:
    print('The data have been imported earlier.Jumping the import ...')

# Reactor endpoints

@app.route('/')
def index():
    return '<h1>Welcome to the API Nuclear Reactors!</h1>\n<h2>Veja a documentação da API completa em:</h2>\n<h3>localhost:5000/api</h3>'

@app.route('/reactors', methods=['GET'])
def get_all_reactors():
    """
    Get all reactors.
    ---
    responses:
        200:
          description: All reactors.
    """
    return reactor_controller.get_all_reactors()


# Rota para criar um novo reator no banco de dados passando os dados no corpo da requisição como nome, país, cidade, tipo, modelo e potência 
@app.route('/reactors', methods=['POST'])
def insert_reactor():
    data = request.json
    reactor_controller.insert_reactor(data)
    return jsonify({'message': 'Reactor created successfully'}), 201


# Rota para obter todos os reatores
# @app.route('/reactors', methods=['GET'])
# def get_all_reactors():
#     reactors = reactor_controller.get_all_reactors()
#     return jsonify(reactors)

# Rota para obter um reator pelo seu ID
@app.route('/reactors/<reactor_id>', methods=['GET'])
def get_reactor_by_id(reactor_id):
    reactor = reactor_controller.get_reactor_by_id(reactor_id)
    return jsonify(reactor)

# Rota para atualizar um reator existente
@app.route('/reactors/<reactor_id>', methods=['PUT'])
def update_reactor(reactor_id):
    data = request.json
    reactor_controller.update_reactor(reactor_id, data)
    return jsonify({'message': 'Reactor updated successfully'}), 200

# Rota para excluir um reator existente
@app.route('/reactors/<reactor_id>', methods=['DELETE'])
def delete_reactor(reactor_id):
    reactor_controller.delete_reactor(reactor_id)
    return jsonify({'message': 'Reactor deleted successfully'}), 200

# Rota para obter um reator pelo seu nome
@app.route('/reactors/name/<reactor_name>', methods=['GET'])
def get_reactor_by_name(reactor_name):
    reactor = reactor_controller.get_reactor_by_name(reactor_name)
    return jsonify(reactor)

## Swagger documentation

SWAGGER_URL = '/api'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Nuclear Reactors"
    },
)

app.register_blueprint(swaggerui_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

