from ui.widget import UIWidget
from ui.employee_ui import EmployeeUI
from ui.planes_ui import PlaneUI
from ui.voyage_ui import VoyageUI
from ui.destination_ui import DestinationUI
from model.employee import Employee
from logic.logic_wrapper import LogicWrapper

class MainMenuUI(UIWidget):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper

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
                case "1": # Employees
                    employee_ui = EmployeeUI(self.user, self.logic_wrapper)
                    employee_ui.show()
                    self._clear_screen()
                    self._print_header(add_extra_newline=True)

                case "2": # Planes
                    planes_ui = PlaneUI(self.user, self.logic_wrapper)
                    planes_ui.show()
                    self._clear_screen()
                    self._print_header(add_extra_newline=True)

                case "3": # Voyage
                    voyage_ui = VoyageUI(self.user, self.logic_wrapper)
                    voyage_ui.show()
                    self._clear_screen()
                    self._print_header(add_extra_newline=True)

                case "4": # Planes
                    destination_ui = DestinationUI(self.user, self.logic_wrapper)
                    destination_ui.show()
                    self._clear_screen()
                    self._print_header(add_extra_newline=True)
                    
                case "5": # Log out
                    break
                
                case _: # Unknown option, reprompt
                    self._clear_screen()
                    self._print_header(message="Unknown option", add_extra_newline=True)
