# app/core/security.py
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import settings
import hashlib


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    prepared_password = hashlib.sha256(password.encode()).hexdigest() 
    return pwd_context.hash(prepared_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # 1. Transform the incoming plain password to SHA-256 hex string
    prepared_password = hashlib.sha256(plain_password.encode()).hexdigest()
    
    # 2. Verify the hex string against the stored bcrypt hash
    return pwd_context.verify(prepared_password, hashed_password)

def create_access_token(subject: dict, expires_delta: timedelta = None):
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=1440))

    to_encode = subject.copy()
    
    if "sub" in to_encode:
        to_encode["sub"] = str(to_encode["sub"])

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt