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
            ], numbered=True)

            option = input("Choose an option: ")

            match option:
                case "1": # List employees
                    self.display_employee_list()
                    self._clear_screen()
                    self._print_header(add_extra_newline=True)

                case "2": # List employee
                    self.display_employee()
                    self._clear_screen()
                    self._print_header(add_extra_newline=True)

                case "3": # Register employee
                    self.register_employee()
                    self._clear_screen()
                    self._print_header(add_extra_newline=True)

                case "4": # Update employee
                    self.update_employee()
                    self._clear_screen()
                    self._print_header(add_extra_newline=True)

                case "5": # Remove employee
                    self.remove_employee()
                    self._clear_screen()
                    self._print_header(add_extra_newline=True)
                    
                case "6": # Back
                    break

                case _: # Unknown option, reprompt
                    self._clear_screen()
                    self._print_header(message="Unknown option", add_extra_newline=True)

    def display_employee_list(self):
        self._clear_screen()
        self._print_header(message="Employees", add_extra_newline=True)
        # TODO: Insert data
        self._print_datalist(
            { "id": 3, "name": 8, "addr.": 10, "phone": 8, "email": 25 }, [
            [ "000", "Testman", "Coolstreet", "581-2345", "test@nanair.is" ],
            [ "000", "Testman", "Coolstreet", "581-2345", "test@nanair.is" ],
            [ "000", "Testman", "Coolstreet", "581-2345", "test@nanair.is" ],
            [ "000", "Testman", "Coolstreet", "581-2345", "test@nanair.is" ],
        ])
        input()

    def display_employee(self):
        pass

    def register_employee(self):
        pass

    def update_employee(self):
        pass

    def remove_employee(self):
        pass

