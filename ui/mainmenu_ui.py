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
        while True:
            option = self._display_selection(
                [
                    "Employees",
                    "Planes",
                    "Voyages",
                    "Destinations",
                    "Log out",
                ],
                header_title=f"Welcome {self.user.name}!",
                include_back=False,
            )

            match option:
                case 0: # Employees
                    employee_ui = EmployeeUI(self.user, self.logic_wrapper)
                    employee_ui.show()

                case 1: # Planes
                    planes_ui = PlaneUI(self.user, self.logic_wrapper)
                    planes_ui.show()

                case 2: # Voyage
                    voyage_ui = VoyageUI(self.user, self.logic_wrapper)
                    voyage_ui.show()

                case 3: # Planes
                    destination_ui = DestinationUI(self.user, self.logic_wrapper)
                    destination_ui.show()
                    
                case 4: # Log out
                    return

