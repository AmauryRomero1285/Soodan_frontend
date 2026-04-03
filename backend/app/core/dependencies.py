# app/core/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime

from app.database.connection import SessionLocal
from app.models.profile import Profile
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_db)
) -> Profile:
    """
    Obtiene el usuario actual a partir del token JWT.
    Se usa en endpoints protegidos.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decodificar el token
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )

        user_id_str: Optional[str] = payload.get("sub")
        if user_id_str is None:
            raise credentials_exception

        # Convertir a entero
        try:
            user_id = int(user_id_str)
        except (ValueError, TypeError):
            raise credentials_exception

        # Verificar que el token no ha expirado (aunque jose ya lo valida, es buena práctica)
        if payload.get("exp") and payload["exp"] < datetime.utcnow().timestamp():
            raise credentials_exception

    except JWTError as e:
        print(f"[JWT Error] {e}")   # Para depuración en desarrollo
        raise credentials_exception
    except Exception as e:
        print(f"[Unexpected Error in get_current_user] {e}")
        raise credentials_exception

    # Buscar usuario en la base de datos
    user = db.query(Profile).filter(Profile.id == user_id).first()
    
    if user is None:
        raise credentials_exception

    # Opcional: verificar que la cuenta esté verificada
    if not user.is_verified:
        raise HTTPException(status_code=403, detail="Cuenta no verificada")

    return user