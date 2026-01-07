import level_objects
import os
from player import Player
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_state import GameState


class Level:

    def __init__(self, name, level_layout: list, player_x: int, player_y: int):
        self.level_layout: list[list[level_objects.PlainLevelObject]] = level_layout
        self.player = Player()
        self.name = name
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

    def __init__(self, game_state: "GameState"):
        self.game_state = game_state

    def clear_console():
        os.system("cls")

    def display_level(self):
        print(f"| {self.game_state.level.name} |")
        print(
            f"Turn: {self.game_state.turn_count} | Collectibles Left: {self.game_state.collectibles_left}"
        )
        items_str = ""
        if len(self.game_state.level.player.items) == 0:
            items_str = "No Items"
        else:
            items_str = ", ".join(self.game_state.level.player.items)
        print(f"Items: {items_str}")

        width = len(max(self.game_state.level.level_layout, key=len))

        print("╔" + "══" * width + "╗")

        for x in range(len(self.game_state.level.level_layout)):
            print("║", end="")
            for y in range(len(self.game_state.level.level_layout[x])):
                symbol = ""
                if (
                    x == self.game_state.level.player_x
                    and y == self.game_state.level.player_y
                ):
                    symbol = self.game_state.level.player.display_symbol
                else:
                    symbol = self.game_state.level.level_layout[x][y].display_symbol
                print(symbol, end="")
            fill_count = width - len(self.game_state.level.level_layout[x])
            fill_count *= 2
            print(" " * fill_count + "║")

        print("╚" + "══" * width + "╝")

    def redraw(self):
        LevelView.clear_console()
        self.display_level()
