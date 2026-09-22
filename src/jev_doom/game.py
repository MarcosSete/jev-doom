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

    game.close()


if __name__ == "__main__":
    main()