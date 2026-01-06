from enum import Enum
from controls import ControlsManager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_state import GameState

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

class PlainLevelObject:
    def __init__(self, symbol="!?", is_passable = True):
        self.display_symbol = symbol
        self.is_passable = is_passable
        self.is_collectible: bool = False

    @property
    def display_symbol(self):
        return self._display_symbol

    @display_symbol.setter
    def display_symbol(self, new_val: str):
        if len(new_val) > 2:
            raise ValueError
        self._display_symbol = new_val

    def on_enter(self, self_x: int, self_y: int, gs: "GameState"):
        pass

    def on_exit(self, self_x: int, self_y: int, gs: "GameState"):
        pass

class Ground(PlainLevelObject):
    def __init__(self):
        super().__init__("..")

class Wall(PlainLevelObject):
    def __init__(self):
        super().__init__("||", False)

class Carrot(PlainLevelObject):
    def __init__(self):
        super().__init__("🥕")
        self.is_collectible = True

    def on_enter(self, self_x, self_y, gs):
        gs.collectibles_left -= 1
        gs.level.replace_at(self_x, self_y, Ground())

class Conveer(PlainLevelObject):
    def __init__(self, direction: Direction):
        symb = ""
        self.direction = direction
        if direction == Direction.LEFT:
            symb = "⇐⇐"
        elif direction == Direction.RIGHT:
            symb = "⇒⇒"
        elif direction == Direction.UP:
            symb = "⇑⇑"
        elif direction == Direction.DOWN:
            symb = "⇓⇓"
        else:
            symb = "!?"
        super().__init__(symb)

    def on_enter(self, self_x, self_y, gs):
        gs.skip_input = True
        gs.direction_moving = self.direction