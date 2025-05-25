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
