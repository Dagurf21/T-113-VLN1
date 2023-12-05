from ui.widget import UIWidget
from model.plane import Plane # Dont think we need this ??
from model.employee import Employee
from logic.logic_wrapper import LogicWrapper

class PlaneUI(UIWidget):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper

    def show(self):
        self._clear_screen()
        self._print_header(add_extra_newline=True)

        while True:
            self._print_options_list([
                "List planes",
                "List plane",
                "Register plane", 
                "Remove plane", 
                "Back",
            ], True)

            option = input("Choose an option: ")

            match option:
                case "1": # List Planes
                    self._clear_screen()
                    self._print_header(message="List all planes")
                    self.list_planes()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case "2": # List a plane
                    self._clear_screen()
                    self._print_header(message="List a singular plane")
                    self.list_plane()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case "3": # Register plane
                    self._clear_screen()
                    self._print_header(message="Register a plane")
                    self.register_plane()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case "4": # Remove plane
                    self._clear_screen()
                    self._print_header(message="Removing a plane")
                    self.remove_plane()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case "5": # Back
                    break

                case _: # Unkown option, reprompt
                    self._clear_screen()
                    self._print_header(message="Unknown option", add_extra_newline=True)

    def list_planes(self):
        print ("We are listing all planes here")

    def list_plane(self):
        print ("We are printing a singular plane here")

    def register_plane(self):
        print ("We are registering a single plane here")

    def remove_plane(self):
        print ("We are removing a plane here")
