from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440   # 24h para medic/admin, más para patient
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # Email config (SMTP)
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_USER: str
    EMAIL_PASSWORD: str
    EMAIL_FROM: str
    EMAIL_FROM_NAME: str
    
    # Database config
    DB_CONNECTION: str
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env",
        extra = "ignore"

settings = Settings()