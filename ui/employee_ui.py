from ui.widget import UIWidget, UICancelException
from model.employee import Employee
from model.pilot import Pilot
from model.manager import Manager
from model.flight_attendant import FlightAttendant
from model.flight_manager import FlightManager
from logic.logic_wrapper import LogicWrapper

class EmployeeUI(UIWidget):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper

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
        self._prompt_interactive_datalist(
            { "id": 3, "name": 8, "addr.": 10, "phone": 8, "email": 25 }, [
            [ "000", "Testman", "Coolstreet", "581-2345", "test@nanair.is" ],
            [ "000", "Testman", "Coolstreet", "581-2345", "test@nanair.is" ],
            [ "000", "Testman", "Coolstreet", "581-2345", "test@nanair.is" ],
            [ "000", "Testman", "Coolstreet", "581-2345", "test@nanair.is" ],
        ])


    def display_employee(self):
        testdata = [["000", "Testman", "Coolstreet", "581-2345", "test@nanair.is"]]
        self._print_header(message="Employee search by ID")
        employee_id = input("ID of employee: ")
        employee_information = self.logic_wrapper.list_employee(employee_id)
        self._print_datalist(
            { "id": 3, "name":8, "addr.":10, "phone": 8, "email": 25}, employee_information
            )
        input()
        pass

    def register_employee(self):
        try:
            employee_title = self._display_selection([
                "Manager",
                "Pilot",
                "Flight Attendant",
                "Flight Manager",
            ], header_title="Register Employee")

            name         = self._display_prompt("Enter name",         header_title="Register Employee", opt_instruction="Leave empty to cancel")
            password     = self._display_prompt("Enter password",     header_title="Register Employee", opt_instruction="Leave empty to cancel")
            address      = self._display_prompt("Enter address",      header_title="Register Employee", opt_instruction="Leave empty to cancel")
            ssn          = self._display_prompt("Enter SSN",          header_title="Register Employee", opt_instruction="Leave empty to cancel")
            mobile_phone = self._display_prompt("Enter mobile phone", header_title="Register Employee", opt_instruction="Leave empty to cancel")
            email        = self._display_prompt("Enter email",        header_title="Register Employee", opt_instruction="Leave empty to cancel")
            home_phone   = self._display_prompt("Enter home phone",   header_title="Register Employee", opt_instruction="Leave empty to cancel (optional: n to skip)")

            if home_phone == "n":
                home_phone = None

            match employee_title:
                case 0: # Manager
                    work_phone   = self._display_prompt("Enter work phone",   header_title="Register Employee", opt_instruction="Leave empty to cancel")
                    employee = Manager(
                        name=name,
                        password_hash=password,
                        address=address,
                        ssn=ssn,
                        mobile_phone=mobile_phone,
                        email=email,
                        home_phone=home_phone,
                        work_phone=work_phone
                    )
                case 1: # Pilot
                    return # TODO
                case 2: # Flight Attendant
                    return # TODO
                case 3: # Flight Manager
                    work_phone   = self._display_prompt("Enter work phone",   header_title="Register Employee", opt_instruction="Leave empty to cancel")
                    employee = Manager(
                        name=name,
                        password_hash=password,
                        address=address,
                        ssn=ssn,
                        mobile_phone=mobile_phone,
                        email=email,
                        home_phone=home_phone,
                        work_phone=work_phone
                    )

            self.logic_wrapper.create_employee(employee)
        except UICancelException:
            return

    def update_employee(self):
        try:
            employee_id = self._display_prompt("Enter employee id", header_title="Update employee", opt_instruction="Leave empty to cancel")

            
        except UICancelException:
            pass

    def remove_employee(self):
        pass

