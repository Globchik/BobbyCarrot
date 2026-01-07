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
                [Wall(),Ground(),Wall(),Ground(),ConveerSwitch()],
                [Wall(),Ground(),Wall(),Ground(),Ground()],
                [Wall(),Ground(),Conveer(Direction.RIGHT),Carrot(),Wall()],
                [Wall(),Ground(),Wall(),Ground(),Ground()],
                [Wall(),Conveer(Direction.UP),Wall(),Ground(),Carrot()],
                [Carrot(),Conveer(Direction.RIGHT), Ground(), Wall(), Wall()],
                [Carrot(),Ground(),Carrot(),Wall(),Wall()],
                [Ground(),InactiveFlag(),Ground(),Wall(),Wall()],
            ],
            0,
            1,
        ),
        Level(
            "Level 3: Locks",
            [
                [Wall(), Wall(),Carrot(), ConveerSwitch(), Key("Key"),Wall(),Wall(),Wall(),Wall()],
                [Conveer(Direction.UP),Conveer(Direction.RIGHT),Ground(),InactiveFlag(),Ground(),Conveer(Direction.LEFT),Ground(),Carrot(),Wall()],
                [Carrot(), Wall(),Wall(),HiddenSpike(),Wall(),Wall(),Wall(),Ground(),Wall()],
                [Conveer(Direction.UP), Wall(),Wall(),HiddenSpike(),Wall(),Wall(),Wall(),Conveer(Direction.UP),Wall()],
                [Conveer(Direction.LEFT), Lock("Key"), Ground(), Ground(),Ground(),HiddenSpike(),Ground(),ConveerSwitch(),Ground()],
                [Wall(), Wall(),Carrot(),Carrot(),Carrot(),Wall(),Carrot(),Ground(),Carrot()],
            ],
            4,
            3,
        ),
    ]
    
    def get_level_list() -> list[str]:
        return list(map(lambda x: x.name, LevelManager.levels))
    
    def load_level(index: int):
        if(index < 0 or index >= len(LevelManager.levels)):
            return None
        gs = GameState(LevelManager.levels[index])
        gs.run()
        