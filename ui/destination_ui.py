from ui.widget import UIWidget
from model.destination import Destination
from model.employee import Employee


class DestinationUI(UIWidget):
    def __init__(self, user: Employee):
        self.user = user

    def show(self):
        self._clear_screen()
        self._print_header(add_extra_newline=True)

        while True:
            self._print_options_list([
                "List destinations",
                "List destination",
                "Register destination",
                "Update destination",
                "Remove destination",
                "Back",
            ], True)

            option = input("Choose an option: ")

            match option:
                case "6": # Back
                    break

                case _: # Unknown option, reprompt
                    self._clear_screen()
                    self._print_header(message="Unknown option", add_extra_newline=True)
