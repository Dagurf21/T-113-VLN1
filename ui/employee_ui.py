from ui.widget import UIWidget
from model.employee import Employee
from logic.logic_wrapper import Logic_Wrapper

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
        while True:
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
            self._print_centered("q: return - n: next page - p: prev page", add_newline_after=True, add_newline_before=True)

            opt = input("Choose an option: ")
            match opt:
                case "q": # Return
                    break
                
                case "n": # Next page
                    continue

                case "p": # Prev page
                    continue

                case _: # Unknown option
                    continue


    def display_employee(self):
        testdata = [["000", "Testman", "Coolstreet", "581-2345", "test@nanair.is"]]
        self._clear_screen()
        self._print_header(message="Employee search by ID")
        employee_id = input("ID of employee: ")
        employee_information = Logic_Wrapper.list_employee(employee_id)
        self._print_datalist(
            { "id": 3, "name":8, "addr.":10, "phone": 8, "email": 25}, employee_information
            )
        input()
        pass

    def register_employee(self):
        pass

    def update_employee(self):
        pass

    def remove_employee(self):
        pass

