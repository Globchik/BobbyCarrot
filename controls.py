from msvcrt import getch
from enum import Enum
import time

class ControlAction(Enum):
    CANCEL = -1
    CONFIRM = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

class ControlsManager:

    def get_control_from_key(key: bytes):
        if key in (b"\x00", b"\xe0"):
            key = getch()
            if key == b"K":
                return ControlAction.LEFT
            if key == b"M":
                return ControlAction.RIGHT
            if key == b"H":
                return ControlAction.UP
            if key == b"P":
                return ControlAction.DOWN
        else:
            key = key.decode().upper()
            if key == "A":
                return ControlAction.LEFT
            if key == "D":
                return ControlAction.RIGHT
            if key == "W":
                return ControlAction.UP
            if key == "S":
                return ControlAction.DOWN
            if key == "\x1b":
                return ControlAction.CANCEL
            if key == "\r":
                return ControlAction.CONFIRM
            else:
                return None

    def wait_for_control_action() -> ControlAction | None:
        while True:
            key = getch()
            action = ControlsManager.get_control_from_key(key)
            if action is not None:
                return action
    
    def wait(sec):
        time.sleep(sec)
