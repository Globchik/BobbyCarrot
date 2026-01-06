from level import Level, LevelView
from controls import ControlsManager, ControlAction
from level_objects import Direction

class GameState:
    def __init__(self, level: Level):
        self.collectibles_left = 0
        self.turn_count = 0
        self.level = level
        self.level_view = LevelView(level)
        self.direction_moving: Direction = None
        self.is_running = False
        self.skip_input = False
        
        for row in level.level_layout:
            for item in row:
                if(item.is_collectible):
                    self.collectibles_left+=1
        

    def get_direction(control_action: ControlAction):
        if control_action == ControlAction.LEFT:
            return Direction.LEFT
        if control_action == ControlAction.RIGHT:
            return Direction.RIGHT
        if control_action == ControlAction.UP:
            return Direction.UP
        if control_action == ControlAction.DOWN:
            return Direction.DOWN
        return None

    def get_target_coordinates(x: int, y: int, dir: Direction | None):
        if dir == Direction.LEFT:
            return x, y - 1
        if dir == Direction.RIGHT:
            return x, y + 1
        if dir == Direction.UP:
            return x - 1, y
        if dir == Direction.DOWN:
            return x + 1, y
        return x, y

    def wait_for_input(self):
        action = ControlsManager.wait_for_control_action()
        self.direction_moving = GameState.get_direction(action)

    def tick(self):
        if(self.direction_moving is None):
            return
        
        player_x, player_y = self.level.player_x, self.level.player_y
        x, y = GameState.get_target_coordinates(player_x, player_y, self.direction_moving)

        target_obj = self.level.get_at(x, y)
        if target_obj is None or not target_obj.is_passable:
            return

        exiting_obj = self.level.get_at(player_x, player_y)
        exiting_obj.on_exit(player_x, player_y, self)
        
        x, y = GameState.get_target_coordinates(player_x, player_y, self.direction_moving)
        self.level.player_x, self.level.player_y = x, y
        
        target_obj.on_enter(x, y, self)
        self.turn_count += 1
       
    
    def run(self):
        self.is_running = True
        self.level_view.redraw()
        
        while(self.is_running):
            if(self.skip_input):
                self.skip_input = False
                ControlsManager.wait(0.5)
            else:
                self.wait_for_input()
            self.tick()
            self.level_view.redraw()