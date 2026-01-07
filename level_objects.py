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
        super().__init__("██", False)

class Empty(PlainLevelObject):
    def __init__(self):
        super().__init__("  ", False)

class Carrot(PlainLevelObject):
    def __init__(self):
        super().__init__("🥕")
        self.is_collectible = True

    def on_enter(self, self_x, self_y, gs):
        gs.collectible_found()
        gs.level.replace_at(self_x, self_y, Ground())

class Conveer(PlainLevelObject):
    def __init__(self, direction: Direction):
        self.direction = direction
        super().__init__(self.get_symbol())
    
    def get_symbol(self):
        symb: str
        if self.direction == Direction.LEFT:
            symb = "⇐⇐"
        elif self.direction == Direction.RIGHT:
            symb = "⇒⇒"
        elif self.direction == Direction.UP:
            symb = "⇑⇑"
        elif self.direction == Direction.DOWN:
            symb = "⇓⇓"
        else:
            symb = "!?"
        return symb
    
    def swap_direction(self):
        if(self.direction == Direction.LEFT):
            self.direction = Direction.RIGHT
        elif(self.direction == Direction.RIGHT):
            self.direction = Direction.LEFT
        elif(self.direction == Direction.UP):
            self.direction = Direction.DOWN
        elif(self.direction == Direction.DOWN):
            self.direction = Direction.UP
        self.display_symbol = self.get_symbol()

    def on_enter(self, self_x, self_y, gs):
        gs.skip_input = True
        gs.direction_moving = self.direction
    
class ConveerSwitch(PlainLevelObject):
    def __init__(self):
        super().__init__("🟡")
    
    def on_enter(self, self_x, self_y, gs):
        gs.level.replace_at(self_x,self_y, Ground())
        for x, row in enumerate(gs.level.level_layout):
            for y, obj in enumerate(row):
                if isinstance(obj, Conveer):
                    obj.swap_direction()
    
class InactiveFlag(PlainLevelObject):
    def __init__(self):
        super().__init__("🚩")
    
    def activate(self, self_x, self_y, gs: "GameState"):
        gs.level.replace_at(self_x,self_y,ActiveFlag())

class ActiveFlag(PlainLevelObject):
    def __init__(self):
        super().__init__("🏁")
    
    def on_enter(self, self_x, self_y, gs):
        gs.win()

class Key(PlainLevelObject):
    def __init__(self, key_name):
        super().__init__("🗝️")
        self.item_name = key_name
    
    def on_enter(self, self_x, self_y, gs):
        gs.level.replace_at(self_x,self_y, Ground())
        gs.level.player.items.append(self.item_name)
        for x, row in enumerate(gs.level.level_layout):
            for y, obj in enumerate(row):
                if isinstance(obj, Lock):
                    if(obj.lock_name == self.item_name):
                        obj.unlock()

class Lock(PlainLevelObject):
    def __init__(self, lock_name):
        super().__init__("🔒", False)
        self.lock_name = lock_name
    
    def unlock(self):
        self.is_passable = True
    
    def lock(self):
        self.is_passable = False
    
    def on_enter(self, self_x, self_y, gs):
        gs.level.replace_at(self_x,self_y, Ground())
        if(gs.level.player.has_item(self.lock_name)):
            gs.level.player.remove_item(self.lock_name)
        
        if(gs.level.player.has_item(self.lock_name)):
            return
        
        for x, row in enumerate(gs.level.level_layout):
            for y, obj in enumerate(row):
                if isinstance(obj, Lock):
                    if(obj.lock_name == self.lock_name):
                        obj.lock()
        
class Spike(PlainLevelObject):
    def __init__(self):
        super().__init__("^^")
    
    def on_enter(self, self_x, self_y, gs):
        gs.lose()

class HiddenSpike(PlainLevelObject):
    def __init__(self):
        super().__init__("__")
    
    def on_enter(self, self_x, self_y, gs):
        gs.level.replace_at(self_x,self_y, Spike())

