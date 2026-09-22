from pathlib import Path

import vizdoom
from vizdoom import DoomGame


def get_basic_config() -> Path:
    package_path = Path(vizdoom.__file__).resolve().parent
    return package_path / "scenarios" / "basic.cfg"


def main() -> None:
    game = DoomGame()

    config_path = get_basic_config()

    game.load_config(str(config_path))
    game.init()

    print("ViZDoom iniciado.")

    game.new_episode()

    while not game.is_episode_finished():
        game.make_action([0, 0, 0])

    game.close()


if __name__ == "__main__":
    main()