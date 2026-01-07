from game_state import GameState
from levels_manager import LevelManager
from menu_manager import MenuManager

level_select = LevelManager.get_level_list()
while True:
    index = MenuManager.display_level_select(level_select)
    if(index is not None):
        LevelManager.load_level(index)
    else:
        break
