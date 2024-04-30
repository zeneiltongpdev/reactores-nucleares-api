# Documentación de la Aplicación Reactores Nucleares
## Descripción

La aplicación Reactores Nucleares es un sistema para gestionar información sobre reactores nucleares, permitiendo la creación, actualización, eliminación y consulta de estos reactores. Utiliza una base de datos $ MongoDB $ para almacenar los datos de los reactores.

## Funcionalidades
- Creación de reactores
- Actualización de información de reactores
- Eliminación de reactores
- Consulta de reactores por diferentes criterios

## Tecnologías Utilizadas
- **Python**: Lenguaje de programación utilizado para desarrollar la aplicación.
- **Flask**: Framework web utilizado para crear las rutas y endpoints de la API.
- **MongoDB**: Base de datos NoSQL utilizada para almacenar los datos de los reactores.
- **Flask-Swagger-UI**: Biblioteca utilizada para generar la interfaz Swagger para documentar la API.
- **Pymongo**: Biblioteca Python para interactuar con MongoDB.

## Ejecución
Prerrequisitos
- Python instalado en el sistema.
- MongoDB instalado y en ejecución en el puerto predeterminado `(27017)`.

### Instalación de Dependencias
1. Clona el repositorio de la aplicación:
```bash
git clone https://github.com/laura-152020/examen_4-project_laura.git
```
2. Navega hasta el directorio del proyecto:
```
cd examen_4-project_laura
```
3. Instala las dependencias utilizando pip:
```
pip install -r requirements.txt
```
4. Entrar a la carpeta app
```
cd app
```
### Ejecución de la Aplicación
1. Ejecuta el archivo app.py:
```
python app.py
```
2. Accede a la documentación de la API a través del navegador:
```
http://localhost:5000/api
```
### Rutas de la API
- **GET /reactors**: Retorna todos los reactores registrados.
- **GET /reactors/{`reactor_id`}**: Retorna información sobre un reactor específico.
- **POST /reactors**: Crea un nuevo reactor.
- **PUT /reactors/{`reactor_id`}**: Actualiza la información de un reactor existente.
- **DELETE /reactors/{`reactor_id`}**: Elimina un reactor existente.

### Estructura del Proyecto
El proyecto tiene la siguiente estructura de directorios:

- app: Contiene los archivos principales de la aplicación.
- controllers: Controladores de la aplicación.
- models: Modelos de datos de la aplicación.
- repositories: Repositorios para la interacción con la base de datos.
- services: Servicios para la ejecución de operaciones específicas.
- static: Contiene scripts utilitarios de configuración del Swagger.

### Consideraciones Finales:
La aplicación Reactores Nucleares es una solución simple para la gestión de información sobre reactores nucleares, con funcionalidades básicas de $ CRUD $. Puede ser extendida y mejorada según sea necesario.

### Hierramientas Utilizadas
- **Visual Studio Code**: Editor de código utilizado para desarrollar la aplicación.
- **Postman**: Herramienta utilizada para probar las rutas de la API.
- **MongoDB Compass**: Cliente de MongoDB utilizado para visualizar y administrar la base de datos.

![python](https://img.shields.io/badge/python-3.6-blue.svg)
![flask](https://img.shields.io/badge/flask-1.1.2-blue.svg)
![mongodb](https://img.shields.io/badge/mongodb-4.4.1-blue.svg)
![pymongo](https://img.shields.io/badge/pymongo-3.11.0-blue.svg)
![flask-swagger-ui](https://img.shields.io/badge/flask--swagger--ui-3.25.0-blue.svg)
![postman](https://img.shields.io/badge/postman-8.0.3-blue.svg)
![swagger](https://img.shields.io/badge/swagger-4.11.1-blue.svg)


