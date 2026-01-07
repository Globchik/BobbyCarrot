from level_objects import *
from level import Level
from game_state import GameState

class LevelManager:
    
    levels: list[Level] = [
        Level(
            "Level 1: Start",
            [
                [Ground(),Wall(),Wall(),Ground(),HiddenSpike(), Carrot(),HiddenSpike(), Carrot(),HiddenSpike(),],
                [Ground(),Conveer(Direction.RIGHT),Conveer(Direction.RIGHT),Ground(),Wall(),HiddenSpike(), Carrot(),Wall(),Carrot()],
                [InactiveFlag(),Wall(),Wall(),Ground(),Wall(),Carrot(),HiddenSpike(), Carrot(),HiddenSpike(),],
                [Ground(),Wall(),Wall(),Ground(),HiddenSpike(),HiddenSpike(), Carrot(),HiddenSpike(),Wall()],
                [Ground(),Conveer(Direction.LEFT),Conveer(Direction.LEFT),Ground(),Wall(),Wall(),HiddenSpike(),Carrot(),Wall()],
                [Ground(),Wall(),Wall(),Ground(),Wall(),Wall(),Wall(),Wall(),Wall()],
            ],
            0,
            0,
        ),
        Level(
            "Level 2: Conveer Switch",
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
        ),
        Level(
            "Level 3: Locks",
            [
                [Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()],
                [Wall(), Ground(), Ground(), Key("Key 1"), Ground(), Lock("Key 1"), Carrot()],
                [Wall(), Wall(), Wall(), Wall(), Wall(), Ground(), Wall()],
                [Wall(), InactiveFlag(), Lock("Key 2"), Key("Key 2"), Carrot(), Ground(), Wall()],
                [Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()],
            ],
            1,
            1,
        ),
    ]
    
    def get_level_list() -> list[str]:
        return list(map(lambda x: x.name, LevelManager.levels))
    
    def load_level(index: int):
        if(index < 0 or index >= len(LevelManager.levels)):
            return None
        gs = GameState(LevelManager.levels[index])
        gs.run()
        