# auth/auth.py

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from setting import settings
from utilities.security import verify_password

security = HTTPBasic()

# Load users and hashed passwords from environment variables
users_db = {"alice": settings.alice_password_hash, "bob": settings.bob_password_hash}


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password

    if username not in users_db or not verify_password(password, users_db[username]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return username
