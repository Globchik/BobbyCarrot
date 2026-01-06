import level_objects
import os
from player import Player
import level_objects


class Level:

    def __init__(self, level_layout: list, player_x: int, player_y: int):
        self.level_layout: list[list[level_objects.PlainLevelObject]] = level_layout
        self.player = Player()
        self.player_x, self.player_y = player_x, player_y

    def get_at(self, x: int, y: int) -> level_objects.PlainLevelObject:
        if len(self.level_layout) <= x or x < 0:
            return None
        if len(self.level_layout[x]) <= y or y < 0:
            return None
        return self.level_layout[x][y]

    def replace_at(self, x: int, y: int, obj: level_objects.PlainLevelObject):
        if self.get_at(x, y) is not None:
            self.level_layout[x][y] = obj


class LevelView:

    def __init__(self, level: Level):
        self._level = level

    def clear_console():
        os.system("cls")

    def display_level(self):
        for x in range(len(self._level.level_layout)):
            for y in range(len(self._level.level_layout[x])):
                if(x == self._level.player_x and y == self._level.player_y):
                    print(self._level.player.display_symbol, end="")
                else:
                    print(self._level.level_layout[x][y].display_symbol, end="")
            print()

    def redraw(self):
        LevelView.clear_console()
        self.display_level()
