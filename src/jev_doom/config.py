from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    project_name: str = "jev-doom"
    environment: str = "vizdoom"
