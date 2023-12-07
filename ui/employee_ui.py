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
        while True:
            try:
                option = self._display_selection(
                    [
                        "List employees",
                        "List employee",
                        "Register employee",
                        "Update employee",
                        "Remove employee",
                    ],
                    header_title="Employees",
                    include_back=True
                )
            except UICancelException:
                return

            match option:
                case 0: # List employees
                    self.display_employee_list()

                case 1: # List employee
                    self.display_employee()

                case 2: # Register employee
                    self.register_employee()

                case 3: # Update employee
                    self.update_employee()

                case 4: # Remove employee
                    self.remove_employee()

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

        self._display_interactive_datalist(
            { "id": 3, "name": 8, "addr.": 10, "phone": 8, "email": 25 }, 
            employee_data,
            title="Employees",
        )


    def display_employee(self):
        self._print_header(
            message="List Employee",
            add_extra_newline=True
        )

        while True:
            try:
                employee_id = self._prompt(
                    "Enter employee id",
                    opt_instruction="Leave empty to cancel",
                    clear_screen=False
                )
            except UICancelException:
                return

            try:
                employee_id = int(employee_id)
            except ValueError:
                self._print_header("List Employee", add_extra_newline=True)
                self._print_centered("Id has to be a number", add_newline_after=True)
                continue
                
            employee = self.logic_wrapper.get_employee(employee_id)

            if employee == None:
                self._print_header("List Employee", add_extra_newline=True)
                self._print_centered(f"Employee with id {employee_id} doesn't exist", add_newline_after=True)
                continue

            self._print_header(f"List Employee [id:{employee.id}]", add_extra_newline=True)
            self._print_list([
                f"Id:     {employee.id}",
                f"Name:   {employee.name}",
                f"Email:  {employee.email}",
                f"SSN:    {employee.ssn}",
                f"Mobile: {employee.mobile_phone}",
                f"Home:   {employee.home_phone}"
            ], add_newline_after=True)


    def register_employee(self):
        try:
            employee_title = self._display_selection([
                "Manager",
                "Pilot",
                "Flight Attendant",
                "Flight Manager",
            ], header_title="Register Employee")

            name         = self._prompt("Enter name",         header_title="Register Employee", opt_instruction="Leave empty to cancel")
            password     = self._prompt("Enter password",     header_title="Register Employee", opt_instruction="Leave empty to cancel")
            address      = self._prompt("Enter address",      header_title="Register Employee", opt_instruction="Leave empty to cancel")
            ssn          = self._prompt("Enter SSN",          header_title="Register Employee", opt_instruction="Leave empty to cancel")
            mobile_phone = self._prompt("Enter mobile phone", header_title="Register Employee", opt_instruction="Leave empty to cancel")
            email        = self._prompt("Enter email",        header_title="Register Employee", opt_instruction="Leave empty to cancel")
            home_phone   = self._prompt("Enter home phone",   header_title="Register Employee", opt_instruction="Leave empty to cancel (optional: n to skip)")

            if home_phone == "n":
                home_phone = None

            match employee_title:
                case 0: # Manager
                    work_phone   = self._prompt(
                        "Enter work phone",
                        header_title="Register Employee",
                        opt_instruction="Leave empty to cancel"
                    )
                    employee = Manager(
                        name=name,
                        password=password,
                        address=address,
                        ssn=ssn,
                        mobile_phone=mobile_phone,
                        email=email,
                        home_phone=home_phone,
                        work_phone=work_phone
                    )
                case 1: # Pilot
                    employee = Pilot(
                        name=name,
                        password=password,
                        address=address,
                        ssn=ssn,
                        mobile_phone=mobile_phone,
                        email=email,
                        home_phone=home_phone,
                        license="C750",
                        assignments=[]
                    )
                case 2: # Flight Attendant
                    employee = FlightAttendant(
                        name=name,
                        password=password,
                        address=address,
                        ssn=ssn,
                        mobile_phone=mobile_phone,
                        email=email,
                        home_phone=home_phone,
                        assignments=[]
                    )
                case 3: # Flight Manager
                    work_phone   = self._prompt(
                        "Enter work phone",
                        header_title="Register Employee",
                        opt_instruction="Leave empty to cancel"
                    )
                    employee = FlightManager(
                        name=name,
                        password=password,
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
        self._print_header(
            "Update Employee",
            add_extra_newline=True
        )

        while True:
            try:
                employee_id = self._prompt(
                    "Enter employee id",
                    opt_instruction="Leave empty to cancel",
                    clear_screen=False
                )
                employee_id = int(employee_id)
            except ValueError:
                self._print_header("List Employee", add_extra_newline=True)
                self._print_centered("Id has to be a number", add_newline_after=True)
                continue
                
            try:
                employee = self.logic_wrapper.get_employee(employee_id)

                if employee == None:
                    self._print_header("List Employee", add_extra_newline=True)
                    self._print_centered(f"Employee with id {employee_id} doesn't exist", add_newline_after=True)
                    continue

                employee_fields = [
                    "Password",
                    "Address",
                    "Mobile Phone",
                    "Email",
                    "Home Phone",
                ]

                # Add options depending on the employee type
                if isinstance(employee, Pilot):
                    pass # TODO
                elif isinstance(employee, FlightAttendant):
                    pass # TODO
                elif isinstance(employee, Manager):
                    employee_fields.append("Work Phone")
                elif isinstance(employee, FlightManager):
                    employee_fields.append("Work Phone")

                field_to_update = self._display_selection(
                    employee_fields,
                    header_title=f"Update Employee [{employee.name}]"
                )

                match field_to_update:
                    case 0: # Password
                        employee.password = self._prompt(
                            "Enter new password",
                            opt_instruction="Leave empty to cancel"
                        )
                    case 1: # Address
                        employee.address = self._prompt(
                            "Enter new address",
                            opt_instruction="Leave empty to cancel"
                        )
                    case 2: # Mobile Phone
                        employee.mobile_phone = self._prompt(
                            "Enter new mobile phone",
                            opt_instruction="Leave empty to cancel"
                        )
                    case 3: # Email
                        employee.email = self._prompt(
                            "Enter new email",
                            opt_instruction="Leave empty to cancel"
                        )
                    case 4: # Home Phone
                        employee.home_phone = self._prompt(
                            "Enter new home phone",
                            opt_instruction="Leave empty to cancel"
                        )
                    case 5: # Field 5 [Manager, FlightManager, Pilot, FlightAttendant]
                        if isinstance(employee, Pilot):
                            return # TODO
                        elif isinstance(employee, FlightAttendant):
                            return # TODO
                        elif isinstance(employee, Manager):
                            employee.work_phone = self._prompt(
                                "Enter new work phone",
                                opt_instruction="Leave empty to cancel"
                            )
                        elif isinstance(employee, FlightManager):
                            employee.work_phone = self._prompt(
                                "Enter new work phone",
                                opt_instruction="Leave empty to cancel"
                            )
                    case 6: # Field 6 [Pilot]
                        return # Todo

                self.logic_wrapper.update_employee(employee)

                return
            except UICancelException:
                return

    def remove_employee(self):
        self._print_header("Remove Employee", add_extra_newline=True)

        while True:
            try:
                employee_id = self._prompt("Enter employee id", opt_instruction="Leave empty to cancel", clear_screen=False)
                employee_id = int(employee_id)
            except ValueError:
                self._print_header("Remove Employee", add_extra_newline=True)
                self._print_centered("Id has to be a number", add_newline_after=True)
                continue
                
            try:
                employee = self.logic_wrapper.get_employee(employee_id)

                if employee == None:
                    self._print_header("Remove Employee", add_extra_newline=True)
                    self._print_centered(f"Employee with id {employee_id} doesn't exist", add_newline_after=True)
                    continue

                should_delete = self._display_selection(
                    [
                        "Delete"
                    ],
                    header_title=f"Delete {employee.name}?",
                    allow_cancel=False
                )

                if should_delete == 0:
                    self.logic_wrapper.delete_employee(employee_id)
    
                return
            except UICancelException:
                return

