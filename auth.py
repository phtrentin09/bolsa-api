from fastapi import HTTPException, status
from fastapi.security import HTTPBasicCredentials
import secrets

# Simulação de usuário/senha (em produção, use banco ou serviço de autenticação)
USERS = {"admin": "secret123"}

def authenticate(credentials: HTTPBasicCredentials):
    correct_password = USERS.get(credentials.username)
    if not correct_password or not secrets.compare_digest(credentials.password, correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )