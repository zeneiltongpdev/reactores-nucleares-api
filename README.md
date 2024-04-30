# Documentação da Aplicação Reactores Nucleares
## Descrição
A aplicação de Reactores Nucleares é um sistema para gerenciar informações sobre reatores nucleares, permitindo a criação, atualização, exclusão e consulta desses reatores. Ela utiliza um banco de dados $ MongoDB $ para armazenar os dados dos reatores.

## Funcionalidades
- Criação de reatores
- Atualização de informações de reatores
- Exclusão de reatores
- Consulta de reatores por diferentes critérios

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver a aplicação.
- **Flask**: Framework web utilizado para criar as rotas e endpoints da API.
- **MongoDB**: Banco de dados NoSQL utilizado para armazenar os dados dos reatores.
- **Flask-Swagger-UI**: Biblioteca utilizada para gerar a interface Swagger para documentar a API.
- **Pymongo**: Biblioteca Python para interagir com o MongoDB.

## Execução
### Pré-requisitos
- Python 3 instalado no sistema.
- MongoDB instalado e em execução na porta padrão (`27017`).

### Instalação das Dependências
**Clone o repositório da aplicação via SSH:**
```bash
git clone git@github.com:zeneiltongpdev/reactores-nucleares-api.git
```
**Clone o repositório da aplicação via HTTPS:**
```bash
git clone https://github.com/zeneiltongpdev/reactores-nucleares-api.git
```
**Navegue até o diretório do projeto:**
```bash
cd reactores-nucleares-api
```
**Instale as dependências utilizando pip:**
```bash
pip install -r requirements.txt
```
### Execução da Aplicação
**Execute o arquivo app.py:**
```bash
python app.py
```
**Acesse a documentação da API através do navegador:**
```bash
http://localhost:5000/api
```
## Rotas da API

- **GET /reactors**: Retorna todos os reatores cadastrados.
- **GET /reactors/{`reactor_id`}**: Retorna informações sobre um reator específico.
- **POST /reactors**: Cria um novo reator.
- **PUT /reactors/{`reactor_id`}**: Atualiza as informações de um reator existente.
- **DELETE /reactors/{`reactor_id`}**: Exclui um reator existente.

## Estrutura do Projeto

**O projeto possui a seguinte estrutura de diretórios:** 

- app: Contém os arquivos principais da aplicação.
- controllers: Controladores da aplicação.
- models: Modelos de dados da aplicação.
- repositories: Repositórios para interação com o banco de dados.
- services: Serviços para execução de operações específicas.
- static: Contém scripts utilitários de configuração do Swagger.

### Considerações Finais:
A aplicação Reactores Nucleares é uma solução simples para gerenciamento de informações sobre reatores nucleares, com funcionalidades básicas de CRUD. Ela pode ser estendida e aprimorada conforme necessário.

### Ferramentas Utilizadas
- **Visual Studio Code**: Editor de código utilizado para desenvolver a aplicação.
- **Postman**: Ferramenta utilizada para testar as rotas da API.
- **MongoDB Compass**: Cliente MongoDB utilizado para visualizar e gerenciar o banco de dados.

![python](https://img.shields.io/badge/python-3.6-blue.svg)
![flask](https://img.shields.io/badge/flask-1.1.2-blue.svg)
![mongodb](https://img.shields.io/badge/mongodb-4.4.1-blue.svg)
![pymongo](https://img.shields.io/badge/pymongo-3.11.0-blue.svg)
![flask-swagger-ui](https://img.shields.io/badge/flask--swagger--ui-3.25.0-blue.svg)
![postman](https://img.shields.io/badge/postman-8.0.3-blue.svg)
![swagger](https://img.shields.io/badge/swagger-4.11.1-blue.svg)