from level_objects import *
from level import Level
from game_state import GameState

class LevelManager:
    
    levels: list[Level] = [
        Level(
            "Level 1",
            [
                [Ground(),Ground(),Ground(),],
                [Wall(),Conveer(Direction.DOWN),Wall(),],
                [Wall(),Conveer(Direction.DOWN),Wall(),],
                [Wall(),Conveer(Direction.DOWN),Wall(),],
                [Wall(),Conveer(Direction.DOWN),Wall(),],
                [Wall(),Conveer(Direction.DOWN),Wall(),],
                [Carrot(),Ground(),Carrot(),],
                [Ground(),InactiveFlag(),Ground(),],
            ],
            0,
            0,
        ),
        Level(
            "Level 2",
            [
                [Wall(),Ground(),Wall(),ConveerSwitch()],
                [Wall(),Ground(),Wall(),Ground()],
                [Wall(),Ground(),Conveer(Direction.RIGHT),Carrot()],
                [Wall(),Ground(),Wall(),],
                [Wall(),Conveer(Direction.UP),Wall(),],
                [Carrot(),Conveer(Direction.RIGHT), Wall(),],
                [Carrot(),Ground(),Carrot(),],
                [Ground(),InactiveFlag(),Ground(),],
            ],
            0,
            1,
        )
    ]
    
    def get_level_list() -> list[str]:
        return list(map(lambda x: x.name, LevelManager.levels))
    
    def load_level(index: int):
        if(index < 0 or index >= len(LevelManager.levels)):
            return None
        gs = GameState(LevelManager.levels[index])
        gs.run()
        