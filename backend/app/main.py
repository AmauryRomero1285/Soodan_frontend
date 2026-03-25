# app/main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

# Importar routers
from app.api.v1.auth import router as auth_router
# Aquí irán los demás routers más adelante:
# from app.api.v1.medic import router as medic_router
# from app.api.v1.patient import router as patient_router
# from app.api.v1.appointment import router as appointment_router

# Importar configuración y dependencias
from app.core.config import settings
from app.database.connection import engine, Base
from app.core.dependencies import get_current_user

# Crear todas las tablas (solo en desarrollo - en producción usa Alembic)
Base.metadata.create_all(bind=engine)

# Instancia principal de FastAPI
app = FastAPI(
    title="MediApp API",
    description="API para aplicación médica - Gestión de pacientes, médicos y citas",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

# ====================== MIDDLEWARE ======================

# CORS - Configuración recomendada para frontend (React, Vue, Flutter, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],                    # Cambia esto en producción por tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Opcional: Servir archivos estáticos (avatares, documentos, etc.)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# ====================== RUTAS ======================

# Prefijo principal de la API
API_V1_PREFIX = "/api/v1"

app.include_router(auth_router, prefix=API_V1_PREFIX)

# Ejemplos de cómo agregar más routers en el futuro:
# app.include_router(medic_router, prefix=API_V1_PREFIX, dependencies=[Depends(get_current_user)])
# app.include_router(patient_router, prefix=API_V1_PREFIX, dependencies=[Depends(get_current_user)])
# app.include_router(appointment_router, prefix=API_V1_PREFIX, dependencies=[Depends(get_current_user)])

# ====================== RUTAS DE PRUEBA / HEALTH CHECK ======================

@app.get("/", tags=["health"])
async def root():
    return {
        "message": "Bienvenido a la API de MediApp",
        "docs": "/api/v1/docs",
        "version": "1.0.0"
    }


@app.get("/api/v1/health", tags=["health"])
async def health_check():
    return {
        "status": "healthy",
        "database": "connected",
        "api_version": "1.0.0"
    }


# Ruta protegida de ejemplo (para probar autenticación)
@app.get("/api/v1/me", tags=["users"])
async def get_current_user_info(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "name": current_user.name,
        "lastname": current_user.lastname,
        "role": current_user.role,
        "is_verified": current_user.is_verified
    }


# ====================== EJECUCIÓN ======================

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,           # Solo en desarrollo
        log_level="info"
    )