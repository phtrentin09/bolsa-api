# Bolsa de Estudos API

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg) ![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green.svg) ![License](https://img.shields.io/badge/license-MIT-lightgrey.svg) ![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

Uma API RESTful para gerenciar bolsas de estudo e candidatos, construída com **FastAPI** e **SQLite**. Inclui operações CRUD completas, autenticação básica e testes automatizados com **Pytest**. A documentação interativa está disponível em `/docs`.

---

## Funcionalidades Principais

- **Gerenciamento de Bolsas**: Crie, leia, atualize e delete bolsas com nome, valor e descrição.
- **Gerenciamento de Candidatos**: Cadastre candidatos com nome, email e vincule-os a bolsas.
- **Autenticação Básica**: Proteja endpoints de escrita (POST, PUT, DELETE) com usuário e senha.
- **Documentação Automática**: Explore e teste a API diretamente em `/docs`.
- **Testes Automatizados**: Garanta a qualidade com testes completos via Pytest.

---

## Tecnologias Utilizadas

- **FastAPI**: Framework moderno e rápido para APIs em Python.
- **SQLAlchemy**: ORM para interação com o banco SQLite.
- **SQLite**: Banco leve para persistência de dados.
- **Pytest**: Framework de testes para confiabilidade.
- **Uvicorn**: Servidor ASGI para rodar a aplicação.

---

## Instruções de Instalação

Siga os passos abaixo para rodar o projeto localmente:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seuusuario/bolsa-api.git
   cd bolsa-api
   ```

2. **Crie e ative um ambiente virtual**:
   - No Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a API**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a documentação**:
   - Abra `http://127.0.0.1:8000/docs` no navegador para explorar os endpoints.

---

## Exemplos de Uso

### Criar uma Nova Bolsa
- **Endpoint**: `POST /bolsas/`
- **Corpo da Requisição**:
  ```json
  {
    "nome": "Bolsa de Estudos 2025",
    "valor": 1500.0,
    "descricao": "Bolsa para graduação"
  }
  ```
- **Autenticação**: Usuário: `admin`, Senha: `secret123`.
- **Resposta**: `200 OK` com os dados da bolsa.

### Listar Bolsas
- **Endpoint**: `GET /bolsas/`
- **Resposta**: `200 OK` com a lista de bolsas.

### Criar um Candidato
- **Endpoint**: `POST /candidatos/`
- **Corpo da Requisição**:
  ```json
  {
    "nome": "João Silva",
    "email": "joao@example.com",
    "bolsa_id": 1
  }
  ```
- **Autenticação**: Usuário: `admin`, Senha: `secret123`.
- **Resposta**: `200 OK` com os dados do candidato.

---

## Demonstração

Veja a documentação interativa em ação:



![image](https://github.com/user-attachments/assets/404fde33-54a0-407c-8793-6db378d1795e)


---

## Testes

Rode os testes automatizados com:
```bash
pytest
```
Os testes cobrem CRUD e autenticação.

---

## Como Contribuir

1. Faça um **fork** do repositório.
2. Crie uma branch (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona feature'`).
4. Envie para o fork (`git push origin feature/nova-feature`).
5. Abra um **Pull Request**.

---

## Licença

Este projeto está sob a [Licença MIT](LICENSE).

-------------------------------------------------------------
##ENGLISH VERSION

Scholarship API
   
A RESTful API for managing scholarships and applicants, built with FastAPI and SQLite. It includes full CRUD operations, basic authentication, and automated testing with Pytest. Interactive documentation is available at /docs.

Main Features

Scholarship Management: Create, read, update, and delete scholarships with name, value, and description.
Applicant Management: Register applicants with name, email, and link them to scholarships.
Basic Authentication: Secure write endpoints (POST, PUT, DELETE) with username and password.
Automatic Documentation: Explore and test the API directly at /docs.
Automated Testing: Ensure quality with comprehensive tests using Pytest.


Technologies Used

FastAPI: A modern, fast framework for building APIs with Python.
SQLAlchemy: ORM for interacting with the SQLite database.
SQLite: A lightweight database for data persistence.
Pytest: A testing framework for reliability.
Uvicorn: An ASGI server to run the application.


Installation Instructions
Follow these steps to run the project locally:

Clone the repository:
git clone https://github.com/seuusuario/bolsa-api.git
cd bolsa-api


Create and activate a virtual environment:

On Windows:python -m venv venv
venv\Scripts\activate


On macOS/Linux:python3 -m venv venv
source venv/bin/activate




Install the dependencies:
pip install -r requirements.txt


Run the API:
uvicorn main:app --reload


Access the documentation:

Open http://127.0.0.1:8000/docs in your browser to explore the endpoints.




Usage Examples
Create a New Scholarship

Endpoint: POST /scholarships/
Request Body:{
  "name": "2025 Scholarship",
  "amount": 1500.0,
  "description": "Scholarship for undergraduate students"
}


Authentication: Username: admin, Password: secret123.
Response: 200 OK with the scholarship details.

List Scholarships

Endpoint: GET /scholarships/
Response: 200 OK with the list of scholarships.

Create an Applicant

Endpoint: POST /applicants/
Request Body:{
  "name": "John Smith",
  "email": "john@example.com",
  "scholarship_id": 1
}


Authentication: Username: admin, Password: secret123.
Response: 200 OK with the applicant details.


Demonstration
See the interactive documentation in action:

![image](https://github.com/user-attachments/assets/b149b90f-c05b-4794-b2ce-76870e12c238)


Tests
.NETRun the automated tests with:
pytest

The tests cover CRUD operations and authentication.

How to Contribute

Fork the repository.
Create a branch (git checkout -b feature/new-feature).
Commit your changes (git commit -m 'Add new feature').
Push to the fork (git push origin feature/new-feature).
Open a Pull Request.


License
This project is licensed under the MIT License.

