from game_state import GameState
from levels_manager import LevelManager
from menu_manager import MenuManager

while True:
    level_select = LevelManager.get_level_list()
    index = MenuManager.display_level_select(level_select)
    LevelManager.load_level(index)
