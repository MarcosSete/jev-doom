from jev_doom.config import Settings


def test_project_configuration() -> None:
    settings = Settings()

    assert settings.project_name == "jev-doom"
    assert settings.environment == "vizdoom"
