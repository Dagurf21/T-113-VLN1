from ui.widget import UIWidget, UICancelException
from model.voyage import Voyage
from model.employee import Employee
from logic.logic_wrapper import LogicWrapper

class VoyageUI(UIWidget):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
    
    def show(self):
        while True:
            try:
                option = self._display_selection(
                    [
                        "List voyages",
                        "List voyage",
                        "Update voyage",
                        "Cancel voyage",
                        "Duplicate voyage", 
                        "Back"
                    ],
                    header_title="Voyages"
                )
            except UICancelException:
                return

            match option:
                case 0: # Listing all voyages
                    self.list_voyages()
                    self._print_header(message="Completed Successfully")
                
                case 1: # Listing a single voyage
                    self.list_voyage()
                    self._print_header(message="Completed Successfully")

                case 2: # Update Voyage
                    self.update_voyage()
                    self._print_header(message="Completed Successfully")

                case 3: # Cancel a voyage
                    self.cancel_voyage()
                    self._print_header(message="Completed Successfully")
                
                case 4: # Duplicating voyage
                    self.duplicate_voyage()
                    self._print_header(message="Completed Successfully")

    def list_voyages(self):
        self._print_header(message="List all voyages")
    
    def list_voyage(self):
        self._print_header(message="List a voyage")

    def update_voyage(self):
        self._print_header(message="List all voyages")

    def cancel_voyage(self):
        self._print_header(message="Cancel a voyage")
    
    def duplicate_voyage(self):
        self._print_header(message="Duplicate Voyage")

