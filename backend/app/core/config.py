"""Application configuration settings."""

import os
from typing import Literal

from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    APP_NAME: str = "DERTOUR Portfolio Control Tower"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: Literal["development", "staging", "production"] = "development"

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/dertour"

    # JWT Security
    JWT_SECRET: str = ""
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:5173"]

    @field_validator("JWT_SECRET")
    @classmethod
    def validate_jwt_secret(cls, v: str) -> str:
        """Validate JWT secret is not empty or using default values."""
        if not v:
            raise RuntimeError("JWT_SECRET environment variable must be set")
        if v.lower() in ("changeme", "secret", "default", "password", "admin"):
            raise RuntimeError(
                f"JWT_SECRET cannot be set to insecure value: '{v}'. "
                "Please set a strong random secret."
            )
        if len(v) < 32:
            raise RuntimeError(
                f"JWT_SECRET must be at least 32 characters long. Current length: {len(v)}"
            )
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Global settings instance
settings = Settings()
