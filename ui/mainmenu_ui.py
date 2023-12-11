from ui import UIWidget, EmployeeUI, PlaneUI, VoyageUI, DestinationUI
from model import Employee, Manager, FlightManager, FlightAttendant, Pilot
from logic import LogicWrapper

class MainMenuUI(UIWidget):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper

    def show(self):
        while True:
            options = []
            if isinstance(self.user, Manager):
                options.append("Employees")
            if isinstance(self.user, FlightManager):
                options.append("Employees")
                options.append("Voyages")
                options.append("Destinations")
            if isinstance(self.user, Pilot):
                pass
            if isinstance(self.user, FlightAttendant):
                pass

            options.append("My Profile")
            options.append("Log out")

            option = self._display_selection(
                options,
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

                case "My Profile":
                    pass
                    
                case "Log out":
                    return

