from level import Level, LevelView
from controls import ControlsManager, ControlAction
from level_objects import Direction, InactiveFlag
from menu_manager import MenuManager
from copy import deepcopy


class GameState:
    def __init__(self, level: Level):
        self.collectibles_left = 0
        self.turn_count = 0
        self._original_level = level
        self.level = deepcopy(level)
        self.level_view = LevelView(self)
        self.direction_moving: Direction = None
        self.is_running = False
        self.skip_input = False

        for row in level.level_layout:
            for item in row:
                if item.is_collectible:
                    self.collectibles_left += 1

    def reset_level(self):
        self.collectibles_left = 0
        self.turn_count = 0
        self.level = deepcopy(self._original_level)
        self.direction_moving: Direction = None
        self.is_running = True
        self.skip_input = False

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

        if self.direction_moving is None:
            match action:
                case ControlAction.CANCEL:
                    self.quit()
                case ControlAction.RESTART:
                    self.restart()

    def tick(self):
        if self.direction_moving is None:
            return

        player_x, player_y = self.level.player_x, self.level.player_y
        x, y = GameState.get_target_coordinates(
            player_x, player_y, self.direction_moving
        )

        target_obj = self.level.get_at(x, y)
        if target_obj is None or not target_obj.is_passable:
            return

        exiting_obj = self.level.get_at(player_x, player_y)
        exiting_obj.on_exit(player_x, player_y, self)

        x, y = GameState.get_target_coordinates(
            player_x, player_y, self.direction_moving
        )
        self.level.player_x, self.level.player_y = x, y

        target_obj.on_enter(x, y, self)
        self.turn_count += 1

    def run(self):
        self.is_running = True

        while self.is_running:
            self.level_view.redraw()

            if self.skip_input:
                self.skip_input = False
                ControlsManager.wait(0.2)
            else:
                self.wait_for_input()

            self.tick()

    def collectible_found(self):
        self.collectibles_left -= 1
        if self.collectibles_left == 0:
            self.activate_flags()

    def activate_flags(self):
        for x, row in enumerate(self.level.level_layout):
            for y, obj in enumerate(row):
                if isinstance(obj, InactiveFlag):
                    obj.activate(x, y, self)

    def win(self):
        MenuManager.display_win_menu(self.turn_count)
        self.is_running = False

    def lose(self):
        restart = MenuManager.display_lose_menu()
        if restart:
            self.reset_level()
        else:
            self.is_running = False

    def restart(self):
        restart = MenuManager.display_restart_menu()
        if restart:
            self.reset_level()

    def quit(self):
        quit = MenuManager.display_quit_menu()
        if quit:
            self.is_running = False
