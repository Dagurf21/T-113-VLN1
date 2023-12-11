from ui import UIWidget, EmployeeUI, PlaneUI, VoyageUI, DestinationUI
from model import Employee
from logic import LogicWrapper

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
                case "Employees":
                    employee_ui = EmployeeUI(self.user, self.logic_wrapper)
                    employee_ui.show()

                case "Planes":
                    planes_ui = PlaneUI(self.user, self.logic_wrapper)
                    planes_ui.show()

                case "Voyages":
                    voyage_ui = VoyageUI(self.user, self.logic_wrapper)
                    voyage_ui.show()

                case "Destinations":
                    destination_ui = DestinationUI(self.user, self.logic_wrapper)
                    destination_ui.show()
                    
                case "Log out":
                    return

