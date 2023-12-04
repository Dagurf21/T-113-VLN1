from ui.widget import UIWidget
from model.voyage import Voyage
from model.employee import Employee

class VoyageUI(UIWidget):
    def __init__(self, user: Employee):
        self.user = user
    
    def show(self):
        self._clear_screen()
        self._print_header(add_extra_newline=True)

        while True:
            self._print_options_list([
                "List voyages",
                "List voyage",
                "Update voyage",
                "Cancel voyage",
                "Duplicate voyage", 
                "Back"
            ], True)

            option = input("Choose an option: ")

            match option:
                case "6": # Back
                    break
            
                case _: # Unkown option, reprompt
                    self._clear_screen()
                    self._print_header(message="Unknown option", add_extra_newline=True)


