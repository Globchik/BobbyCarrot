from game_state import GameState
from levels_manager import LevelManager

gs = GameState(LevelManager.level1())
gs.run()