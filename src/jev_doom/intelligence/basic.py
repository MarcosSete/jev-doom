from typesafe_sdk import Choice, Score, Noul, TypeSafeClient
from jev_doom.config import get_settings

def main() -> None:
    settings = get_settings()

    state = {
        "npc": {
            "health": 25,
            "ammo": 4,
        },
        "enemies": {
            "count": 3,
            "nearest_distance": 3.2,
        },
    }

    with TypeSafeClient(api_key = settings.typesafe_api_key) as client:
        response =  client.system_one(
            state = state,
            questions={
                "action": Choice(
                    instructions="What should the NPC do next?",
                    criteria={
                        "attack": "Engage the nearby enemies.",
                        "retreat": "Move away from the enemies.",
                        "follow": "Move toward the player.",
                        "search": "Explore the environment.",
                    },
                ),
               "danger": Score(
                   instructions= "How dangerous is the current situation for the NPC?",
                   criteria=[
                       "Safe",
                       "Moderately dangerous",
                       "Dangerous",
                       "Critical",
                   ],
               ),
              "prioritize_survival": Noul(
                  instructions="Should the NPC prioritize survival over combat?",
              ),

            },
        )

        action = response.answers["action"]
        danger = response.answers["danger"]
        survival = response.answers["prioritize_survival"]

        print("Action:")
        print(f"  choice: {action.choice}")
        print(f"  confidence: {action.confidence}")
        print(f"  probabilities: {action.probabilities}")

        print("\nDanger:")
        print(f"  score: {danger.score}")
        print(f"  confidence: {danger.confidence}")
        print(f"  probabilities: {danger.probabilities}")

        print("\nPrioritize survival:")
        print(f"  noul: {survival.noul}")


if __name__ == "__main__":
    main()