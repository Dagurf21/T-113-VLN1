from ui.widget import UIWidget, UICancelException
from model.destination import Destination
from model.employee import Employee
from logic.logic_wrapper import LogicWrapper

class DestinationUI(UIWidget):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper

    def show(self):
        while True:
            try:
                option = self._display_selection(
                    [
                        "List destinations",
                        "List destination",
                        "Register destination",
                        "Update destination",
                        "Remove destination",
                    ],
                    header_title="Destinations"
                )
            except UICancelException:
                return

            match option:
                case 0: # List Destinations
                    self.list_destinations()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case 1: # List a Destination
                    self.list_destination()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                
                case 2: # Register Destination
                    self.register_destination()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                
                case 3: # Update Destination
                    self.update_destination()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                
                case 4: # Remove destination
                    self.remove_destination()
                    self._print_header(message="Completed Successfully") # Not sure, may change

    def list_destinations(self):
        self._print_header(message="List all Destinations")
    
    def list_destination(self):
        self._print_header(message="List a Destination")

    def register_destination(self):
        self._print_header(message="Register Destination")
    
    def update_destination(self):
        self._print_header(message="Update Destination")

    def remove_destination(self):
        self._print_header(message="Remove Destination")

