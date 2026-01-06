from level_objects import *
from level import Level

class LevelManager:
    def level1():
        return Level(
            [
                [Ground(),Ground(),Ground(),],
                [Wall(),Conveer(Direction.DOWN),Wall(),],
                [Wall(),Conveer(Direction.DOWN),Wall(),],
                [Wall(),Conveer(Direction.DOWN),Wall(),],
                [Wall(),Conveer(Direction.DOWN),Wall(),],
                [Wall(),Conveer(Direction.DOWN),Wall(),],
                [Carrot(),Ground(),Carrot(),],
                [Ground(),Ground(),Ground(),],
            ],
            0,
            0,
        )
