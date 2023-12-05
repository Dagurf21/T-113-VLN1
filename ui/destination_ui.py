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
                case "1": # List Destinations
                    self._clear_screen()
                    self._print_header(message="List all Destinations")
                    self.list_destinations()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case "2": # List a Destination
                    self._clear_screen()
                    self._print_header(message="List a Destination")
                    self.list_destination()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                
                case "3": # Register Destination
                    self._clear_screen()
                    self._print_header(message="Register Destination")
                    self.register_destination()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                
                case "4": # Update Destination
                    self._clear_screen()
                    self._print_header(message="Update Destination")
                    self.update_destination()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                
                case "5": # Remove destination
                    self._clear_screen()
                    self._print_header(message="Remove Destination")
                    self.remove_destination()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case "6": # Back
                    break

                case _: # Unknown option, reprompt
                    self._clear_screen()
                    self._print_header(message="Unknown option", add_extra_newline=True)

    def list_destinations(self):
        print ("We are listing all destinations here")
    
    def list_destination(self):
        print ("We are showing a single destination here")

    def register_destination(self):
        print("We are registering a single destination here")
    
    def update_destination(self):
        print ("We are updating a destination here")

    def remove_destination(self):
        print ("We are removing a single destination here")

