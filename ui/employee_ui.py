import datetime
from ui import UIElement, UICancelException
from model import Employee, Pilot, Manager, FlightAttendant, FlightManager, Voyage, Destination, Flight
from logic import LogicWrapper

class EmployeeUI(UIElement):
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
                case "List employees":
                    self.list_employees()

                case "List employee":
                    self.display_employee()

                case "Register employee":
                    self.register_employee()

                case "Update employee":
                    self.update_employee()

                case "Remove employee":
                    self.remove_employee()

    def list_employees(self):
        while True:
            try:
                option = self._display_selection(
                    [
                        "List all employees",
                        "List all pilots",
                        "List all flight attendants",
                        "List all employees available on.",
                        "List all employees unavailable on.",
                    ],
                    header_title="Employees",
                    include_back=True
                )
            except UICancelException:
                return

            match option:
                case "List all employees":
                    self.list_all_employees()
                case "List all pilots":
                    self.list_all_pilots()
                case "List all flight attendants":
                    self.list_all_flight_attendants()
                case "List all employees available on.":
                    self.list_all_available_employees_on()
                case "List all employees unavailable on.":
                    self.list_all_unavailable_on()

    def list_all_employees(self):
        employees = self.logic_wrapper.get_all_employees()
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

    def list_all_pilots(self):
        employees = self.logic_wrapper.get_employees_by_job("Pilot")

        while True:
            try:
                option = self._display_selection(
                    [
                        "ID",
                        "Name",
                        "License",
                    ],
                    header_title="List Pilots",
                    include_back=True
                )
            except UICancelException:
                return

            match option:
                case "ID":
                    employees.sort(key=lambda e: e.id)
                case "Name":
                    employees.sort(key=lambda e: e.name)
                case "License":
                    employees.sort(key=lambda e: e.license)

            employee_data = []

            for employee in employees:
                employee_data.append([
                    employee.id,
                    employee.name,
                    employee.address,
                    employee.mobile_phone,
                    employee.license,
                    employee.email
                ])

            self._display_interactive_datalist(
                { "id": 3, "name": 8, "addr.": 10, "phone": 8, "license": 8, "email": 25 }, 
                employee_data,
                title="Employees",
            )

    def list_all_flight_attendants(self):
        employees = self.logic_wrapper.get_employees_by_job("FlightAttendant")
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

    def list_all_available_employees_on(self):
        try:
            date = self._prompt(
                "Pick date (yyyy-mm-dd)",
                opt_instruction="Leave empty to cancel",
                header_title="List employees available on.",
                validator=self.validate_date,
            )
            date = self.parse_date(date)
            employees = self.logic_wrapper.get_employee_by_not_workday(date)
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
        except UICancelException:
            pass
    
    def list_all_unavailable_on(self):
        try:
            date = self._prompt(
                "Pick date (yyyy-mm-dd)",
                opt_instruction="Leave empty to cancel",
                header_title="List employees available on.",
                validator=self.validate_date,
            )
            date = self.parse_date(date)
            employees_destinations = self.logic_wrapper.get_employee_by_workday(date)
            employee_data = []

            for (employee, destination) in employees_destinations:
                employee_data.append([
                    employee.id,
                    employee.name,
                    employee.address,
                    employee.mobile_phone,
                    f"-> {destination.country} ({destination.airport})"
                ])

            self._display_interactive_datalist(
                { "id": 3, "name": 8, "addr.": 10, "phone": 8, "email": 25 }, 
                employee_data,
                title="Employees",
            )
        except UICancelException:
            pass

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

            table = [
                f"Id:      {employee.id}",
                f"Name:    {employee.name}",
                f"Email:   {employee.email}",
                f"SSN:     {employee.ssn}",
                f"Mobile:  {employee.mobile_phone}",
                f"Home:    {employee.home_phone}"
            ]

            if isinstance(employee, Manager):
                table.append(f"Work:    {employee.work_phone}")
            if isinstance(employee, FlightManager):
                table.append(f"Work:    {employee.work_phone}")
            if isinstance(employee, Pilot):
                table.append(f"Assign:  {', '.join(employee.assignments)}")
                table.append(f"License: {employee.license}")
            if isinstance(employee, FlightAttendant):
                table.append(f"Assign:  {employee.assignments}")

            self._print_header(f"List Employee [id:{employee.id}]", add_extra_newline=True)
            self._print_list(table, add_newline_after=True)


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
            ssn          = self._prompt("Enter SSN",          header_title="Register Employee", opt_instruction="Leave empty to cancel", validator=self._validate_ssn)
            mobile_phone = self._prompt("Enter mobile phone", header_title="Register Employee", opt_instruction="Leave empty to cancel", validator=self._validate_phone_number)
            email        = self._prompt("Enter email",        header_title="Register Employee", opt_instruction="Leave empty to cancel", validator=self._validate_email)
            home_phone   = self._prompt("Enter home phone",   header_title="Register Employee", opt_instruction="Leave empty to cancel (optional: n to skip)", validator=self._validate_optional_phone_number)

            if home_phone == "n":
                home_phone = None

            match employee_title:
                case "Manager":
                    work_phone   = self._prompt(
                        "Enter work phone",
                        header_title="Register Employee",
                        opt_instruction="Leave empty to cancel",
                        validator=self._validate_phone_number
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
                case "Pilot":
                    license = self._prompt(
                        "Enter license",
                        header_title="Register Employee",
                        opt_instruction="Leave empty to cancel",
                    )
                    employee = Pilot(
                        name=name,
                        password=password,
                        address=address,
                        ssn=ssn,
                        mobile_phone=mobile_phone,
                        email=email,
                        home_phone=home_phone,
                        license=license,
                        assignments=[]
                    )
                case "Flight Attendant":
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
                case "Flight Manager":
                    work_phone = self._prompt(
                        "Enter work phone",
                        header_title="Register Employee",
                        opt_instruction="Leave empty to cancel",
                        validator=self._validate_phone_number
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
            except UICancelException:
                return
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
                    employee_fields.append("Assignments")
                    employee_fields.append("License")
                elif isinstance(employee, FlightAttendant):
                    employee_fields.append("Assignments")
                elif isinstance(employee, Manager):
                    employee_fields.append("Work Phone")
                elif isinstance(employee, FlightManager):
                    employee_fields.append("Work Phone")

                field_to_update = self._display_selection(
                    employee_fields,
                    header_title=f"Update Employee [{employee.name}]"
                )

                match field_to_update:
                    case "Password":
                        employee.password = self._prompt(
                            "Enter new password",
                            opt_instruction="Leave empty to cancel"
                        )
                    case "Address":
                        employee.address = self._prompt(
                            "Enter new address",
                            opt_instruction="Leave empty to cancel"
                        )
                    case "Mobile Phone":
                        employee.mobile_phone = self._prompt(
                            "Enter new mobile phone",
                            opt_instruction="Leave empty to cancel",
                            validator=self._validate_phone_number
                        )
                    case "Email":
                        employee.email = self._prompt(
                            "Enter new email",
                            opt_instruction="Leave empty to cancel",
                            validator=self._validate_email
                        )
                    case "Home Phone":
                        employee.home_phone = self._prompt(
                            "Enter new home phone",
                            opt_instruction="Leave empty to cancel",
                            validator=self._validate_phone_number
                        )
                    case "Assignments": # Field 5 [Manager, FlightManager, Pilot, FlightAttendant]
                        employee.assignments = self._prompt_assignments("Update employee")
                    case "Work Phone":
                        employee.work_phone = self._prompt(
                            "Enter new work phone",
                            opt_instruction="Leave empty to cancel",
                            validator=self._validate_phone_number
                        )
                    case "License":
                        employee.license = self._prompt(
                            "Enter new license",
                            opt_instruction="Leave empty to cancel",
                        )

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
            except UICancelException:
                return
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

                if should_delete == "Delete":
                    self.logic_wrapper.delete_employee(employee_id)
    
                return
            except UICancelException:
                return

    def _prompt_assignments(self, title):
        def format_voyage(elem):
            voyage: Voyage = self.logic_wrapper.get_voyage(elem)
            departure: Flight = self.logic_wrapper.get_flight(voyage.departure_flight)
            departure_location: Destination = self.logic_wrapper.get_destination(departure.departure)
            destination_location: Destination = self.logic_wrapper.get_destination(departure.destination)
            return f"{departure_location.country} ({departure_location.airport}) -> {destination_location.country} ({destination_location.airport})"

        assignments = self._prompt_list(
            "Enter assignment id",
            title,
            element_display=format_voyage,
            validator=self._validate_assignment
        )
        return list(map(int, assignments))

    def _validate_ssn(self, ssn):
        if self.logic_wrapper.validate_ssn(ssn):
            return None
        
        return "Invalid ssn format"

    def _validate_email(self, email):
        if self.logic_wrapper.validate_email(email):
            return None
        
        return "Invalid email format"
    
    def _validate_phone_number(self, number):
        if self.logic_wrapper.validate_phone_number(number):
            return None
        
        return "Invalid phone number format"

    def _validate_optional_phone_number(self, number):
        if number == "n" or self.logic_wrapper.validate_phone_number(number):
            return None
        
        return "Invalid phone number format"

    def _validate_assignment(self, assignment_id):
        try:
            assignment_id = int(assignment_id)
            assignment = self.logic_wrapper.get_voyage(assignment_id)
            if assignment == None:
                return f"Assignment with id {assignment_id} doesn't exist"
            return None
        except ValueError:
            return "ID must be number"

    def validate_date(self, inp):
        if len(inp) != 10:
            return "Invalid date format"
        
        try:
            self.parse_date(inp)
        except:
            return "Invalid date format"

    def parse_date(self, date):
        year, month, day = date.split('-')
        return datetime.date(int(year), int(month), int(day))
