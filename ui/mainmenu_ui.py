from enum import Enum
from ui.widget import UIWidget
from model.employee import Employee

class Permissions(Enum):
    Admin           = 0
    Manager         = 1
    FlightManager   = 2
    Pilot           = 3
    FlightAttendant = 3

class MainMenuUI(UIWidget):
    def __init__(self, user: Employee, permissions: Permissions):
        self.user = user
        self.permissions = permissions

    def show(self):
        self._clear_screen()
        self._print_header(message=f"Welcome {self.user.name}!", add_extra_newline=True)

        while True:
            self._print_options_list([
                "Employees",
                "Planes",
                "Voyages",
                "Destinations",
                "Log out",
            ], True)

            option = input("Choose an option: ")

            match option:
                case "5": # Log out
                    break
                
                case _: # Unknown option, reprompt
                    self._clear_screen()
                    self._print_header(message="Unknown option", add_extra_newline=True)
