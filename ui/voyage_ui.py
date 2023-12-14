from ui import UIElement, UICancelException
from model import Voyage, Employee, FlightAttendant, Pilot, VoyageStatus
from logic import LogicWrapper
import datetime
from copy import deepcopy


class VoyageUI(UIElement):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper

    def show(self):
        while True:
            try:
                option = self._display_selection(
                    [
                        "Create Voyage",
                        "List voyages",
                        "List voyage",
                        "Update voyage",
                        "Cancel voyage",
                        "Duplicate voyage",
                        "Staff voyage",
                    ],
                    header_title="Voyages",
                )
            except UICancelException:
                return

            match option:
                case "Create Voyage":
                    self.create_voyage()

                case "List voyages":
                    self.list_voyages()

                case "List voyage":
                    self.list_voyage()

                case "Update voyage":
                    self.update_voyage()

                case "Cancel voyage":
                    self.cancel_voyage()

                case "Duplicate voyage":
                    self.duplicate_voyage()

                case "Staff voyage":
                    self.staff_voyage()

    def create_voyage(self):
        try:
            plane = self._prompt(
                "Enter plane ID",
                header_title="Create voyage",
                opt_instruction="Leave empty to cancel",
                validator=self.validate_plane,
            )
            destination = self._prompt(
                "Enter destination ID of voyage",
                header_title="Create voyage",
                opt_instruction="Leave empty to cancel",
                validator=self.validate_destination,
            )
            date = self._prompt(
                "Enter date of voyage (yyyy-mm-dd)",
                header_title="Create voyage",
                opt_instruction="Leave empty to cancel",
                validator=self.validate_date,
            )
            departure_time = self._prompt(
                "Enter time of departure (hh:mm)",
                header_title="Create voyage",
                opt_instruction="Leave empty to cancel",
                validator=self.validate_time,
            )
            return_date = self._prompt(
                "Enter Return date of voyage (yyyy-mm-dd)",
                header_title="Create voyage",
                opt_instruction="Leave empty to cancel",
                validator=self.validate_date,
            )
            return_departure_time = self._prompt(
                "Enter departure time of arrival flight (hh:mm)",
                header_title="Create voyage",
                opt_instruction="Leave empty to cancel",
                validator=self.validate_time,
            )
            sold_seats = self._prompt(
                "Enter the amount of sold seats",
                header_title="Create voyage",
                opt_instruction="Leave empty to cancel",
                validator=self.validate_number,
            )
            flight_attendants = self._prompt_list(
                "Enter flight attendant ID",
                header_title="Create voyage",
                validator=self.validate_flight_attendant,
            )
            pilots = self._prompt_list(
                "Enter lead pilot ID's",
                header_title="Create voyage",
                validator=self.validate_pilot,
            )

            self.logic_wrapper.create_voyage(
                int(plane),
                int(destination),
                self.parse_date(date),
                self.parse_date(return_date),
                self.parse_time(departure_time),
                self.parse_time(return_departure_time),
                int(sold_seats),
                list(map(int, flight_attendants)),
                list(map(int, pilots)),
            )

            return  # TODO

        except UICancelException:
            return

    def list_voyages(self):
        voyages: list[Voyage] = self.logic_wrapper.get_all_voyages()

        while True:
            try:
                option = self._display_selection(
                    [
                        "All",
                        "On day",
                        "In week",
                    ],
                    header_title="List Voyages [Filter]",
                    include_back=True
                )
            except UICancelException:
                return
            
            try:
                match option:
                    case "On day":
                        date = self._prompt(
                            "Specity date (yyyy-mm-dd)",
                            opt_instruction="Leave empty to cancel",
                            header_title="List Voyages on day",
                            validator=self.validate_date
                        )
                        date = self.parse_date(date)
                        voyages = [voyage for voyage in voyages if voyage.departure_date == date]

                    case "In week":
                        date = self._prompt(
                            "Specity first day of week (yyyy-mm-dd)",
                            opt_instruction="Leave empty to cancel",
                            header_title="List Voyages on day",
                            validator=self.validate_date
                        )
                        date = self.parse_date(date)
                        end_date = date + datetime.timedelta(weeks=1)
                        voyages = [voyage for voyage in voyages if date <= voyage.departure_date <= end_date]

                    case "Back":
                        return
            except UICancelException:
                continue

            voyage_data = []

            for voyage in voyages:
                plane = self.logic_wrapper.get_plane(voyage.plane)

                voyage_data.append(
                    [
                        voyage.id,
                        voyage.departure_flight,
                        voyage.return_flight,
                        f"{voyage.sold_seats} / {plane.capacity}",
                        voyage.departure_date,
                        voyage.return_date,
                        voyage.status,
                    ]
                )

            self._display_interactive_datalist(
                {
                    "id": 3,
                    "From": 6,
                    "Dest": 6,
                    "Seats": 9,
                    "Date": 10,
                    "Return date": 11,
                    "Status": 15,
                },
                voyage_data,
                title="Voyages",
            )

    def list_voyage(self):
        self._print_header(message="List a voyage", add_extra_newline=True)

        while True:
            try:
                voyage_id = self._prompt(
                    "Enter voyage id",
                    opt_instruction="Leave empty to cancel",
                    clear_screen=False,
                )
            except UICancelException:
                return

            try:
                voyage_id = int(voyage_id)
            except ValueError:
                self._print_header("List voyage", add_extra_newline=True)
                self._print_centered("ID has to be a number", add_newline_after=True)
                continue

            voyage = self.logic_wrapper.get_voyage(voyage_id)

            if voyage == None:
                self._print_header("List voyage", add_extra_newline=True)
                self._print_centered(
                    f"Voyage with id {voyage_id} doesn't exist", add_newline_after=True
                )
                continue

            pilot_repr = self.format_employee_list(voyage.pilots, 14, "Pilots: ", 2, 2)
            attendant_repr = self.format_employee_list(voyage.flight_attendants, 14, "Attendants: ", 1)
            plane = self.logic_wrapper.get_plane(voyage.plane)

            self._print_header(f"List Voyage [ID:{voyage_id}]", add_extra_newline=True)
            self._print_list(
                [
                    f"ID:           {voyage.id}",
                    f"Plane:        {plane.name} ({plane.manufacturer} {plane.ty})",
                    *pilot_repr,
                    *attendant_repr,
                    f"Sold Seats:   {voyage.sold_seats}",
                    f"Capacity:     {plane.capacity}",
                    f"From:         {voyage.departure_flight}",
                    f"To:           {voyage.return_flight}",
                    f"Date:         {voyage.departure_date}",
                    f"Return Date:  {voyage.return_date}",
                    f"Status:       {voyage.status}",
                ],
                add_newline_after=True,
            )

    def update_voyage(self):
        self._print_header("Update Voyage", add_extra_newline=True)

        while True:
            try:
                voyage_id = self._prompt(
                    "Enter Voyage ID",
                    opt_instruction="Leave empty to cancel",
                    clear_screen=False,
                )
                voyage_id = int(voyage_id)
            except UICancelException:
                return
            except ValueError:
                self._print_header("List voyage", add_extra_newline=True)
                self._print_centered("ID has to be a number", add_newline_after=True)
                continue

            try:
                voyage = self.logic_wrapper.get_voyage(voyage_id)

                if voyage == None:
                    self._print_header("List Voyage", add_extra_newline=True)
                    self._print_centered(
                        f"Voyage with ID {voyage_id} doesn't exist",
                        add_newline_after=True,
                    )
                    continue

                voyage_fields = [
                    "Seats sold"
                ]

                field_to_update = self._display_selection(
                    voyage_fields, header_title=f"Update voyage with ID [{voyage.id}]"
                )

                match field_to_update:
                    case "Seats sold":
                        voyage.sold_seats = int(self._prompt(
                            "Enter new amount of sold seats",
                            opt_instruction="Leave empty to cancel",
                            validator=self.validate_number,
                        ))
                
                self.logic_wrapper.update_voyage(voyage)

                return
            except UICancelException:
                return

    def cancel_voyage(self):
        self._print_header(message="Cancel a voyage", add_extra_newline=True)

        while True:
            try:
                voyage_id = self._prompt(
                    "Enter Voyage ID",
                    opt_instruction="Leave empty to cancel",
                    clear_screen=False,
                )
                voyage_id = int(voyage_id)
            except UICancelException:
                return
            except ValueError:
                self._print_header("Cancel voyage", add_extra_newline=True)
                self._print_centered("ID has to be a number", add_newline_after=True)
                continue

            try:
                voyage = self.logic_wrapper.get_voyage(voyage_id)

                if voyage == None:
                    self._print_header("Remove voyage", add_extra_newline=True)
                    self._print_centered(
                        f"voyage with id {voyage_id} doesn't exist",
                        add_newline_after=True,
                    )
                    continue

                should_delete = self._display_selection(
                    ["Delete"],
                    header_title=f"Delete voyage {voyage.id} on {voyage.departure_date}?",
                    allow_cancel=False,
                )

                if should_delete == "Delete":
                    self.logic_wrapper.delete_voyage(voyage_id)

                return
            except UICancelException:
                return

    def duplicate_voyage(self):
        self._print_header(message="Duplicate Voyage")
        self._print_header(message="Duplicate Voyage", add_extra_newline=True)
        while True:

            duplicate_voyage_options = [
                "Duplicate voyage once, only new dates",
                "Recurring voyage"
            ]

            duplicate_options = self._display_selection(
                duplicate_voyage_options, header_title="Duplicate Voyages"
            )

            match duplicate_options:
                case "Duplicate voyage once, only new dates":
                    self._print_header(message="Duplicate voyage, new dates", add_extra_newline=True)
                    try:
                        voyage_id = self._prompt(
                            "Enter voyage id",
                            opt_instruction="Leave empty to cancel",
                            clear_screen=False,
                        )
                    except UICancelException:
                        return

                    try:
                        voyage_id = int(voyage_id)
                    except ValueError:
                        self._print_header("Duplicate voyage, new dates", add_extra_newline=True)
                        self._print_centered("ID has to be a number", add_newline_after=True)
                        continue

                    try:
                        """ Duplicate voyage new date only """
                        copy_voyage = self.logic_wrapper.get_voyage(voyage_id)
                        new_voyage = copy_voyage
                        
                        departure_date = self._prompt(
                            "Enter date of voyage (yyyy-mm-dd)",
                            header_title="Create voyage",
                            opt_instruction="Leave empty to cancel",
                            validator=self.validate_date,
                        )
                        return_date = self._prompt(
                            "Enter Return date of voyage (yyyy-mm-dd)",
                            header_title="Create voyage",
                            opt_instruction="Leave empty to cancel",
                            validator=self.validate_date,
                        )

                        new_voyage.pilots = []
                        new_voyage.attendants = []
                        new_voyage.sold_seats = 0
                        new_voyage.departure_date = self.parse_date(departure_date)
                        new_voyage.return_date = self.parse_date(return_date)

                        self.logic_wrapper.create_voyage(
                            int(copy_voyage.plane),
                            int(copy_voyage.destination),
                            new_voyage.departure_date,
                            new_voyage.return_date,
                            copy_voyage.departure_time,
                            copy_voyage.return_departure_time,
                            int(copy_voyage.sold_seats),
                            list(map(int, copy_voyage.flight_attendants)),
                            list(map(int, copy_voyage.pilots)),
                        )

                        self._print_header(
                            "Successfully duplicated voyage", 
                            add_extra_newline=True)
                
                        """Duplicate voyage End only date"""
                    except UICancelException:
                        return
                    
                case "Recurring voyage":
                    # Voyage id to duplicate
                    self._print_header(message="Duplicate voyage, new dates", add_extra_newline=True)
                    try:
                        voyage_id = self._prompt(
                            "Enter voyage id",
                            opt_instruction="Leave empty to cancel",
                            clear_screen=False,
                        )
                    except UICancelException:
                        return

                    try:
                        voyage_id = int(voyage_id)
                    except ValueError:
                        self._print_header("Duplicate voyage, new dates", add_extra_newline=True)
                        self._print_centered("ID has to be a number", add_newline_after=True)
                        continue
                    
                    # Interval how many days between voyages
                    try: 
                        self._print_header("Duplicate voyage, new dates", add_extra_newline=True)
                        voyage_interval = int(self._prompt(
                            "Enter how many days inbetween each voyage",
                            opt_instruction="Leave empty to cancel",
                            clear_screen=True,
                            validator=self.validate_number
                        ))

                        end_date_voyage = self._prompt(
                            "Enter the date of which the reccurance will end",
                            opt_instruction="Leave empty to cancel",
                            clear_screen=True,
                            validator=self.validate_date
                        )

                        end_date_voyage = self.parse_date(end_date_voyage)
                        now = datetime.date.today()
                        print(end_date_voyage)
                        print(type(end_date_voyage))
                        
                        copy_voyage = self.logic_wrapper.get_voyage(voyage_id)
                        time_between_flights = datetime.timedelta(days=voyage_interval)

                        while now < end_date_voyage:
                            new_voyage = deepcopy(copy_voyage)
                           
                            time_between_flights += datetime.timedelta(days=voyage_interval)

                            new_voyage.pilots = []
                            new_voyage.attendants = []
                            new_voyage.sold_seats = 0
                            new_voyage.departure_date += time_between_flights
                            new_voyage.return_date += time_between_flights

                            self.logic_wrapper.create_voyage(
                                int(copy_voyage.plane),
                                int(copy_voyage.destination),
                                new_voyage.departure_date,
                                new_voyage.return_date,
                                copy_voyage.departure_time,
                                copy_voyage.return_departure_time,
                                int(copy_voyage.sold_seats),
                                list(map(int, copy_voyage.flight_attendants)),
                                list(map(int, copy_voyage.pilots)),
                            )

                            now = new_voyage.return_date

                    except UICancelException:
                        return

    def staff_voyage(self):
        self._print_header(message="Staff Voyage", add_extra_newline=True)

        while True:
            try:
                voyage_id = self._prompt(
                    "Enter Voygae ID",
                    opt_instruction="Leave empty to cancel",
                    clear_screen=False,
                )
                voyage_id = int(voyage_id)
            except UICancelException:
                return
            except ValueError:
                self._print_header("Cancel voyage", add_extra_newline=True)
                self._print_centered("ID has to be a number", add_newline_after=True)
                continue

            try:
                voyage = self.logic_wrapper.get_voyage(voyage_id)

                pilots_or_attendants = self._display_selection(
                    ["Pilots", "Flight attendant"], header_title="Staff voyage"
                )

                match pilots_or_attendants:
                    case "Pilots":
                        pilot = (self._prompt(
                            prompt="Enter pilot ID",
                            header_title="Enter ID of pilot",
                            validator= lambda e: self.validate_pilot(e, voyage.plane),
                        ))
                        voyage.pilots.append(pilot)

                        self.logic_wrapper.update_voyage(voyage)

                        assigned_pilot = self.logic_wrapper.get_employee(int(pilot))
                        assigned_pilot.assignments.append(voyage.id)
                        self.logic_wrapper.update_employee(assigned_pilot)

                    case "Flight attendant":
                        attendant = (self._prompt(
                            prompt="Enter ID of flight attendant",
                            header_title="Enter ID of flight attendant",
                            validator=self.validate_flight_attendant,
                        ))
                        voyage.flight_attendants.append(attendant)

                        self.logic_wrapper.update_voyage(voyage)
                        
                        assigned_attendant = self.logic_wrapper.get_employee(int(attendant))
                        assigned_attendant.assignments.append(voyage.id)
                        self.logic_wrapper.update_employee(assigned_attendant)

                return
            except UICancelException:
                return

    def validate_plane(self, inp):
        try:
            plane_id = int(inp)
            plane = self.logic_wrapper.get_plane(plane_id)
            if plane is None:
                return f"Plane with id {plane_id} doesn't exist"
            
            return None
        except ValueError:
            return "ID must be a number"

    def validate_destination(self, inp):
        try:
            destination_id = int(inp)
            if destination_id == 0:
                return "Destination cannot be 0"

            destination = self.logic_wrapper.get_plane(destination_id)
            if destination is None:
                return f"Destination with id {destination} doesn't exist"
            
            return None
        except ValueError:
            return "ID must be a number"

    def validate_date(self, inp):
        if len(inp) != 10:
            return "Invalid date format"
        
        try:
            self.parse_date(inp)
        except:
            return "Invalid date format"

    def validate_time(self, inp):
        if len(inp) != 5:
            return "Invalid date format"
        
        try:
            self.parse_time(inp)
        except:
            return "Invalid date format"

    def validate_flight_attendant(self, inp):
        try:
            employee_id = int(inp)
            if self.logic_wrapper.check_job_position(employee_id, "FlightAttendant"):
                return None
            else:
                return f"Flight attendant with id {employee_id} doesn't exist"
        
        except ValueError:
            return "ID must be a number"

    def validate_pilot(self, inp, plane_id):
        try:
            employee_id = int(inp)
        except ValueError:
            return "ID must be a number"
            
        if self.logic_wrapper.check_job_position(employee_id, "Pilot"):
            if self.logic_wrapper.pilot_has_license(employee_id, plane_id):
                return None
            else:
                return f"Pilot does not have a license to fly this plane"
        else:
            return f"Pilot with id {employee_id} doesn't exist"
    
    def validate_number(self, inp):
        try:
            int(inp)
            return None
        except ValueError:
            return "Input must be a number"

    def parse_date(self, date):
        year, month, day = date.split('-')
        return datetime.date(int(year), int(month), int(day))

    def parse_time(self, date):
        hours, minutes = date.split(':')
        return datetime.time(int(hours), int(minutes))
    
    def format_employee_list(self, employees: list[Employee], padding_len: int, header: int, min_len: int, max_len: int = None) -> str:
        result = []
        for i in range(min_len):
            if max_len is not None and i >= max_len:
                break

            string = " " * padding_len
            if i == 0:
                string = f"{header:<{padding_len}}"

            if i >= len(employees):
                result.append(f"{string}- EMPTY -")
                continue

            employee = self.logic_wrapper.get_employee(employees[i])
            result.append(f"{string}{employee.name}")
        
        return result