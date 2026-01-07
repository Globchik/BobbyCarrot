from controls import ControlsManager, ControlAction
import os


class MenuManager:

    def clear_console():
        os.system("cls")

    def display_level_select(available_levels: list[str]) -> int:
        selected_index = 0
        while True:
            MenuManager.clear_console()
            print("╔════════════════════════════╗")
            print("║       LEVEL SELECT         ║")
            print("╚════════════════════════════╝")

            for i in range(len(available_levels)):
                if i == selected_index:
                    print(f"  > {available_levels[i]} <")
                else:
                    print(f"    {available_levels[i]}")

            print("\n[UP/DOWN]: Navigate  [ENTER]: Select")

            action = ControlsManager.wait_for_control_action()

            if action == ControlAction.UP:
                selected_index -= 1
                if(selected_index == -1):
                    selected_index = len(available_levels) - 1
            elif action == ControlAction.DOWN:
                selected_index += 1
                if(selected_index == len(available_levels)):
                    selected_index = 0
            elif action == ControlAction.CONFIRM:
                return selected_index

    def display_win_menu(turns: int):
        MenuManager.clear_console()
        print("╔════════════════════════════╗")
        print("║         YOU WIN!           ║")
        print("╚════════════════════════════╝")
        print(f"\nTurns taken: {turns}")
        print("\nPress [ENTER] to return to Level Select.")

        while True:
            action = ControlsManager.wait_for_control_action()
            if action == ControlAction.CONFIRM:
                break

    def display_lose_menu() -> bool:
        MenuManager.clear_console()
        print("╔════════════════════════════╗")
        print("║        GAME OVER           ║")
        print("╚════════════════════════════╝")
        print("\nYou have lost.")
        print("\nPress [ENTER] or [R] to Restart")
        print("Press [ESC] to Quit")

        while True:
            action = ControlsManager.wait_for_control_action()
            if action == ControlAction.CONFIRM or action == ControlAction.RESTART:
                return True
            elif action == ControlAction.CANCEL:
                return False
    
    def display_restart_menu() -> bool:
        MenuManager.clear_console()
        print("╔════════════════════════════╗")
        print("║          Restart           ║")
        print("╚════════════════════════════╝")
        print("\nRestart?")
        print("\nPress [ENTER] or [R] to Restart")
        print("Press [ESC] to Resume")

        while True:
            action = ControlsManager.wait_for_control_action()
            if action == ControlAction.CONFIRM or action == ControlAction.RESTART:
                return True
            elif action == ControlAction.CANCEL:
                return False
    
    def display_quit_menu() -> bool:
        MenuManager.clear_console()
        print("╔════════════════════════════╗")
        print("║            Quit            ║")
        print("╚════════════════════════════╝")
        print("\nQuit?")
        print("\nPress [ENTER] to Quit")
        print("Press [ESC] to Resume")

        while True:
            action = ControlsManager.wait_for_control_action()
            if action == ControlAction.CONFIRM:
                return True
            elif action == ControlAction.CANCEL:
                return False
