from ui.widget import UIWidget
from model.employee import Employee

class EmployeeUI(UIWidget):
    def __init__(self, user: Employee):
        self.user = user

    def show(self):
        self._clear_screen()
        self._print_header(add_extra_newline=True)

        while True:
            self._print_options_list([
                "List employees",
                "List employee",
                "Register employee",
                "Update employee",
                "Remove employee",
                "Back",
            ], True)

            option = input("Choose an option: ")

            match option:

                case "1": # List employees
                    self._clear_screen()
                    self._print_header(message="List all employees")
                    EmployeeUI.list_employees()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                    
                case "2": # List an employee
                    self._clear_screen()
                    self._print_header(message="List a single employee")
                    EmployeeUI.list_employee()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                    
                case "3": # Register employees
                    self._clear_screen()
                    self._print_header(message="Register employee")
                    EmployeeUI.register_employee()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                    
                case "4": # Update employees
                    self._clear_screen()
                    self._print_header(message="Update employees")
                    EmployeeUI.update_employee()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                    
                case "5": # Remove employees
                    self._clear_screen()
                    self._print_header(message="Remove employee")
                    EmployeeUI.remove_employee()
                    self._clear_screen()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case "6": # Back
                    break

                case _: # Unknown option, reprompt
                    self._clear_screen()
                    self._print_header(message="Unknown option", add_extra_newline=True)



    def list_employees():
        print ("We are printing all employees")
    
    def list_employee():
        print ("We are showing a single employee here")
    
    def register_employee():
        print ("we are registering an employee here")

    def update_employee():
        print ("we are updating a employee here")
    
    def remove_employee():
        print ("We are removing an employee here")

