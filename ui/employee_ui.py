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
        employees = self.logic_wrapper.list_all_employees()
        employee_data = []

        for employee in employees:
            employee_data.append([
                employee.id,
                employee.name,
                employee.address,
                employee.mobile_phone,
                employee.email
            ])

        self._prompt_interactive_datalist(
            { "id": 3, "name": 8, "addr.": 10, "phone": 8, "email": 25 }, 
            employee_data
        )


    def display_employee(self):
        self._print_header("List Employee", add_extra_newline=True)

        while True:
            try:
                employee_id = self._display_prompt("Enter employee id", opt_instruction="Leave empty to cancel", clear_screen=False)
                employee_id = int(employee_id)
                
                employee = self.logic_wrapper.list_employee(employee_id)

                if employee == None:
                    self._print_header("List Employee", add_extra_newline=True)
                    self._print_centered(f"Employee with id {employee_id} doesn't exist", add_newline_after=True)
                    continue

                self._print_header(f"List Employee [id:{employee.id}]", add_extra_newline=True)
                self._print_options_list([
                    f"Id:     {employee.id}",
                    f"Name:   {employee.name}",
                    f"Email:  {employee.email}",
                    f"SSN:    {employee.ssn}",
                    f"Mobile: {employee.mobile_phone}",
                    f"Home:   {employee.home_phone}"
                ], add_newline_after=True)

            except ValueError:
                self._print_header("List Employee", add_extra_newline=True)
                self._print_centered("Id has to be a number", add_newline_after=True)
                continue
            except UICancelException:
                return

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
        self._print_header("Update Employee", add_extra_newline=True)

        while True:
            try:
                employee_id = self._display_prompt("Enter employee id", opt_instruction="Leave empty to cancel", clear_screen=False)
                employee_id = int(employee_id)
            except ValueError:
                self._print_header("List Employee", add_extra_newline=True)
                self._print_centered("Id has to be a number", add_newline_after=True)
                continue
                
            try:
                employee = self.logic_wrapper.list_employee(employee_id)

                if employee == None:
                    self._print_header("List Employee", add_extra_newline=True)
                    self._print_centered(f"Employee with id {employee_id} doesn't exist", add_newline_after=True)
                    continue

                employee_fields = [
                    "Name",
                    "Password",
                    "Address",
                    "Mobile Phone",
                    "Email",
                    "Home Phone",
                ]

                if isinstance(employee, Pilot):
                    pass # TODO
                elif isinstance(employee, FlightAttendant):
                    pass # TODO
                elif isinstance(employee, Manager):
                    employee_fields.append("Work Phone")
                elif isinstance(employee, FlightManager):
                    employee_fields.append("Work Phone")

                field_to_update = self._display_selection(employee_fields, header_title="Update Employee")

                match field_to_update:
                    case 0: # Name
                        employee.name = self._display_prompt("Enter new name", opt_instruction="Leave empty to cancel")
                    case 1: # Password
                        employee.password_hash = self._display_prompt("Enter new password", opt_instruction="Leave empty to cancel")
                    case 2: # Address
                        employee.address = self._display_prompt("Enter new address", opt_instruction="Leave empty to cancel")
                    case 3: # Mobile Phone
                        employee.mobile_phone = self._display_prompt("Enter new mobile phone", opt_instruction="Leave empty to cancel")
                    case 4: # Email
                        employee.email = self._display_prompt("Enter new email", opt_instruction="Leave empty to cancel")
                    case 5: # Home Phone
                        employee.home_phone = self._display_prompt("Enter new home phone", opt_instruction="Leave empty to cancel")
                    case 6: # Field 6 [Manager, FlightManager, Pilot, FlightAttendant]
                        if isinstance(employee, Pilot):
                            return # TODO
                        elif isinstance(employee, FlightAttendant):
                            return # TODO
                        elif isinstance(employee, Manager):
                            employee.work_phone = self._display_prompt("Enter new work phone", opt_instruction="Leave empty to cancel")
                        elif isinstance(employee, FlightManager):
                            employee.work_phone = self._display_prompt("Enter new work phone", opt_instruction="Leave empty to cancel")
                    case 7: # Field 7 [Pilot]
                        return # Todo

                self.logic_wrapper.update_employee(employee)

                return
            except UICancelException:
                return

    def remove_employee(self):
        pass

