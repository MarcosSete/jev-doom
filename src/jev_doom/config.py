from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ----- Configurações gerais do projeto -----
    project_name: str = "jev-doom"
    environment: str = "vizdoom"

    # ----- Chave da API do TypeSafe -----
    # Sem default => obrigatória. Se não estiver no .env nem no ambiente,
    # o pydantic-settings levanta um ValidationError claro na inicialização.
    typesafe_api_key: str = Field(
        ...,
        description="Chave de API do TypeSafe (obrigatória).",
    )

    # ----- Configuração do pydantic-settings -----
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",       # ignora variáveis desconhecidas no .env
        case_sensitive=False, # TYPESAFE_API_KEY == typesafe_api_key
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()