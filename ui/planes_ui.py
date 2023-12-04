from ui.widget import UIWidget
from model.plane import Plane
from model.employee import Employee

class PlaneUI(UIWidget):
    def __init__(self, user: Employee):
        self.user = user

    def show(self):
        self._clear_screen()
        self._print_header(add_extra_newline=True)

        while True:
            self._print_options_list([
                "List all planes",
                "List a plane",
                "Register plane", 
                "Remove plane", 
                "Back",
            ], True)

            option = input("Choose an option: ")

            match option:
                case "5": #Back
                    break
                case _:
                    self._clear_screen()
                    self._print_header(message="Unknown option", add_extra_newline=True)
