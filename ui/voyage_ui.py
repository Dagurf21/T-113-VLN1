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
                case "1": # Listing all voyages
                    self._clear_screen()
                    self._print_header(message="List all voyages")
                    VoyageUI.list_voyages()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully")
                
                case "2": # Listing a single voyage
                    self._clear_screen()
                    self._print_header(message="List a voyage")
                    VoyageUI.list_voyage()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully")

                case "3": # Update Voyage
                    self._clear_screen()
                    self._print_header(message="List all voyages")
                    VoyageUI.update_voyage()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully")

                case "4": # Cancel a voyage
                    self._clear_screen()
                    self._print_header(message="Cancel a voyage")
                    VoyageUI.cancel_voyage()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully")
                
                case "5": # Duplicating voyage
                    self._clear_screen()
                    self._print_header(message="Duplicate Voyage")
                    VoyageUI.duplicate_voyage()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully")

                case "6": # Back
                    break
            
                case _: # Unkown option, reprompt
                    self._clear_screen()
                    self._print_header(message="Unknown option", add_extra_newline=True)

    def list_voyages():
        print ("List all voyages")
    
    def list_voyage():
        print ("List a singular voyage")

    def update_voyage():
        print ("Updating a voyage")

    def cancel_voyage():
        print ("Cancelling a single voyage")
    
    def duplicate_voyage():
        print ("Duplicating a single voyage")

