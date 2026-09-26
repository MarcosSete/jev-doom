import pytest

from jev_doom.intelligence.client import JevClient
from typesafe_sdk import Choice
from jev_doom.config import  get_settings


@pytest.mark.integration
def test_jev_returns_choice() -> None:
    settings = get_settings()
    state = {
        "npc": {
            "health": 20,
            "ammo": 2,
        },
        "enemies": {
            "count": 4,
            "nearest_distance": 2.0,
        },
    }

    with JevClient(api_key = settings.typesafe_api_key) as client:
        response = client.system_one(
            state=state,
            questions={
                "action": Choice(
                    instructions="What should the NPC do next?",
                    criteria={
                        "attack": "Engage enemies.",
                        "retreat": "Move away from enemies.",
                        "follow": "Move toward the player.",
                    },
                )
            },
        )

    answer = response.answers["action"]

    assert answer.choice in {
        "attack",
        "retreat",
        "follow",
    }

    assert 0 <= answer.confidence <= 1