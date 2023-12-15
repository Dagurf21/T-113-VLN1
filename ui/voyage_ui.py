from ui import UIElement, UICancelException
from model import Voyage, Employee
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
                        "Unstaff voyage",
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

                case "Unstaff voyage":
                    self.unstaff_voyage()

    def create_voyage(self):
        try:
            destination = int(
                self._prompt(
                    "Enter destination ID of voyage",
                    header_title="Create voyage",
                    opt_instruction="Leave empty to cancel",
                    validator=self.validate_destination,
                )
            )
            date = self.parse_date(
                self._prompt(
                    "Enter date of voyage (yyyy-mm-dd)",
                    header_title="Create voyage",
                    opt_instruction="Leave empty to cancel",
                    validator=self.validate_date,
                )
            )
            departure_time = self.parse_time(
                self._prompt(
                    "Enter time of departure (hh:mm)",
                    header_title="Create voyage",
                    opt_instruction="Leave empty to cancel",
                    validator=lambda e: self.validate_departure_time(date, e),
                )
            )
            return_date = self.parse_date(
                self._prompt(
                    "Enter Return date of voyage (yyyy-mm-dd)",
                    header_title="Create voyage",
                    opt_instruction="Leave empty to cancel",
                    validator=lambda i: self.validate_date_after(date, i),
                )
            )
            return_departure_time = self.parse_time(
                self._prompt(
                    "Enter departure time of arrival flight (hh:mm)",
                    header_title="Create voyage",
                    opt_instruction="Leave empty to cancel",
                    validator=lambda i: self.validate_return_departure_time(
                        return_date, date, departure_time, i
                    ),
                )
            )
            plane = int(
                self._prompt(
                    "Enter plane ID",
                    header_title="Create voyage",
                    opt_instruction="Leave empty to cancel",
                    validator=lambda i: self.validate_plane_available(
                        date, departure_time, return_date, return_departure_time, i
                    ),
                )
            )
            sold_seats = self._prompt(
                "Enter the amount of sold seats",
                header_title="Create voyage",
                opt_instruction="Leave empty to cancel",
                validator=lambda e: self.validate_seats_sold_by_plane(plane, e),
            )
            flight_attendants = self._prompt_list(
                "Enter flight attendant ID",
                header_title="Create voyage",
                validator=lambda i: self.validate_attendant_to_assign(
                    date, return_date, i
                ),
                element_display=self.format_employee,
            )
            pilots = self._prompt_list(
                "Enter lead pilot ID's",
                header_title="Create voyage",
                validator=lambda i: self.validate_pilot_to_assign(
                    date, return_date, plane, i
                ),
                element_display=self.format_employee,
            )

            self.logic_wrapper.create_voyage(
                plane,
                destination,
                date,
                return_date,
                departure_time,
                return_departure_time,
                int(sold_seats),
                list(map(int, flight_attendants)),
                list(map(int, pilots)),
            )

        except UICancelException:
            return

    def list_voyages(self):
        while True:
            voyages: list[Voyage] = self.logic_wrapper.get_all_voyages()
            voyages.sort(key=lambda e: e.departure_date)
            try:
                option = self._display_selection(
                    [
                        "All",
                        "On day",
                        "In week",
                    ],
                    header_title="List Voyages [Filter]",
                    include_back=True,
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
                            validator=self.validate_date,
                        )
                        date = self.parse_date(date)
                        voyages = [
                            voyage
                            for voyage in voyages
                            if voyage.departure_date == date
                        ]

                    case "In week":
                        date = self._prompt(
                            "Specity first day of week (yyyy-mm-dd)",
                            opt_instruction="Leave empty to cancel",
                            header_title="List Voyages on day",
                            validator=self.validate_date,
                        )
                        date = self.parse_date(date)
                        end_date = date + datetime.timedelta(weeks=1)
                        voyages = [
                            voyage
                            for voyage in voyages
                            if date <= voyage.departure_date <= end_date
                        ]

                    case "Back":
                        return
            except UICancelException:
                continue

            voyage_data = []

            for voyage in voyages:
                plane = self.logic_wrapper.get_plane(voyage.plane)

                if len(voyage.pilots) == 2 and len(voyage.flight_attendants) > 1:
                    manned = "Full"
                elif len(voyage.pilots) > 0 or len(voyage.flight_attendants) > 0:
                    manned = "Partial"
                else:
                    manned = "Unmanned"

                dest = self.logic_wrapper.get_destination(voyage.destination)

                voyage_data.append(
                    [
                        voyage.id,
                        f"-> {dest.airport}",
                        f"{voyage.sold_seats:<3} / {plane.capacity:<3}",
                        f"{voyage.departure_date} @ {voyage.departure_time}",
                        f"{voyage.return_date} @ {voyage.departure_time}",
                        manned,
                        voyage.status,
                        voyage.departure_flight,
                        voyage.return_flight,
                    ]
                )

            self._display_interactive_datalist(
                {
                    "id": 3,
                    "Dest": 8,
                    "Seats": 9,
                    "Date": 19,
                    "Return date": 19,
                    "Manned": 8,
                    "Status": 13,
                    "Dep.": 6,
                    "Ret.": 6,
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
            attendant_repr = self.format_employee_list(
                voyage.flight_attendants, 14, "Attendants: ", 1
            )
            plane = self.logic_wrapper.get_plane(voyage.plane)

            destination = self.logic_wrapper.get_destination(voyage.destination)

            self._print_header(f"List Voyage [ID:{voyage_id}]", add_extra_newline=True)
            self._print_list(
                [
                    f"ID:           {voyage.id}",
                    f"Plane:        {plane.name} ({plane.manufacturer} {plane.ty})",
                    *pilot_repr,
                    *attendant_repr,
                    f"Sold Seats:   {voyage.sold_seats}",
                    f"Capacity:     {plane.capacity}",
                    f"To:           {destination.country} ({destination.airport})",
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

                voyage_fields = ["Seats sold"]

                field_to_update = self._display_selection(
                    voyage_fields, header_title=f"Update voyage with ID [{voyage.id}]"
                )

                match field_to_update:
                    case "Seats sold":
                        voyage.sold_seats = int(
                            self._prompt(
                                "Enter new amount of sold seats",
                                opt_instruction="Leave empty to cancel",
                                validator=lambda e: self.validate_seats_sold(voyage, e),
                            )
                        )

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
                if voyage is None:
                    self._print_header("Staff voyage", add_extra_newline=True)
                    self._print_centered(f"Voyage with id '{voyage_id}' doesn't exist", add_newline_after=True)
                    continue

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
            try:
                duplicate_voyage_options = [
                    "Duplicate voyage once, only new dates",
                    "Recurring voyage",
                ]

                duplicate_options = self._display_selection(
                    duplicate_voyage_options, header_title="Duplicate Voyages"
                )
            except UICancelException:
                return

            match duplicate_options:
                case "Duplicate voyage once, only new dates":
                    self._print_header(
                        message="Duplicate voyage, new dates", add_extra_newline=True
                    )
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
                        self._print_header(
                            "Duplicate voyage, new dates", add_extra_newline=True
                        )
                        self._print_centered(
                            "ID has to be a number", add_newline_after=True
                        )
                        continue

                    try:
                        """Duplicate voyage new date only"""
                        copy_voyage = self.logic_wrapper.get_voyage(voyage_id)
                        if copy_voyage is None:
                            self._print_header("Staff voyage", add_extra_newline=True)
                            self._print_centered(f"Voyage with id '{voyage_id}' doesn't exist", add_newline_after=True)
                            continue

                        new_voyage = copy_voyage

                        departure_date = self.parse_date(self._prompt(
                            "Enter date of voyage (yyyy-mm-dd)",
                            header_title="Create voyage",
                            opt_instruction="Leave empty to cancel",
                            validator=lambda i: self.validate_duplicate_voyage_date_departure(
                                copy_voyage, i
                            ),
                        ))
                        return_date = self.parse_date(self._prompt(
                            "Enter Return date of voyage (yyyy-mm-dd)",
                            header_title="Create voyage",
                            opt_instruction="Leave empty to cancel",
                            validator=lambda i: self.validate_duplicate_voyage_date_return(
                                departure_date, copy_voyage, i
                            ),
                        ))

                        new_voyage.pilots = []
                        new_voyage.flight_attendants = []
                        new_voyage.sold_seats = 0
                        new_voyage.departure_date = departure_date
                        new_voyage.return_date = return_date

                        self.logic_wrapper.create_voyage(
                            int(copy_voyage.plane),
                            int(copy_voyage.destination),
                            new_voyage.departure_date,
                            new_voyage.return_date,
                            copy_voyage.departure_time,
                            copy_voyage.return_departure_time,
                            0,
                            [],
                            [],
                        )

                        self._print_header(
                            "Successfully duplicated voyage", add_extra_newline=True
                        )

                        """Duplicate voyage End only date"""
                    except UICancelException:
                        return

                case "Recurring voyage":
                    # Voyage id to duplicate
                    self._print_header(
                        message="Duplicate voyage, new dates", add_extra_newline=True
                    )
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
                        self._print_header(
                            "Duplicate voyage, new dates", add_extra_newline=True
                        )
                        self._print_centered(
                            "ID has to be a number", add_newline_after=True
                        )
                        continue

                    copy_voyage = self.logic_wrapper.get_voyage(voyage_id)
                    if copy_voyage is None:
                        self._print_header("Staff voyage", add_extra_newline=True)
                        self._print_centered(f"Voyage with id '{voyage_id}' doesn't exist", add_newline_after=True)
                        continue

                    start_date_voyage = self._prompt(
                        "Enter the date of which the reccurance will start (yyyy-mm-dd)",
                        opt_instruction="Leave empty to cancel",
                        clear_screen=True,
                        validator=lambda i: self.validate_date(i),
                    )

                    start_date_voyage = self.parse_date(start_date_voyage)

                    # Interval how many days between voyages
                    try:
                        self._print_header(
                            "Duplicate voyage, new dates", add_extra_newline=True
                        )
                        voyage_interval = int(
                            self._prompt(
                                "Enter how many days inbetween each voyage",
                                opt_instruction="Leave empty to cancel",
                                clear_screen=True,
                                validator=self.validate_number,
                            )
                        )

                        time_between_flights = datetime.timedelta(days=voyage_interval)

                        end_date_voyage = self._prompt(
                            "Enter the date of which the reccurance will end (yyyy-mm-dd)",
                            opt_instruction="Leave empty to cancel",
                            clear_screen=True,
                            validator=lambda i: self.validate_duplicate_voyage_date_recurring(
                                copy_voyage, start_date_voyage, time_between_flights, i
                            ),
                        )

                        end_date_voyage = self.parse_date(end_date_voyage)
                        time_between_departure_and_arrival = (
                            copy_voyage.return_date - copy_voyage.departure_date
                        )

                        while start_date_voyage < end_date_voyage:
                            new_voyage = deepcopy(copy_voyage)
                            new_voyage.pilots = []
                            new_voyage.flight_attendants = []
                            new_voyage.sold_seats = 0
                            new_voyage.departure_date = start_date_voyage
                            new_voyage.return_date = (
                                start_date_voyage + time_between_departure_and_arrival
                            )

                            self.logic_wrapper.create_voyage(
                                int(copy_voyage.plane),
                                int(copy_voyage.destination),
                                new_voyage.departure_date,
                                new_voyage.return_date,
                                copy_voyage.departure_time,
                                copy_voyage.return_departure_time,
                                0,
                                [],
                                [],
                            )
                            start_date_voyage += time_between_flights

                    except UICancelException:
                        return

    def staff_voyage(self):
        self._print_header(message="Staff Voyage", add_extra_newline=True)

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
                self._print_header("Staff voyage", add_extra_newline=True)
                self._print_centered("ID has to be a number", add_newline_after=True)
                continue

            try:
                voyage = self.logic_wrapper.get_voyage(voyage_id)
                if voyage is None:
                    self._print_header("Staff voyage", add_extra_newline=True)
                    self._print_centered(f"Voyage with id '{voyage_id}' doesn't exist", add_newline_after=True)
                    continue

                pilots_or_attendants = self._display_selection(
                    ["Pilots", "Flight attendant"], header_title="Staff voyage"
                )

                match pilots_or_attendants:
                    case "Pilots":
                        pilot = self._prompt(
                            prompt="Enter pilot ID",
                            header_title="Enter ID of pilot",
                            validator=lambda e: self.validate_assign_pilot(voyage, e),
                        )
                        self.logic_wrapper.staff_voyage_pilot(voyage_id, int(pilot))

                    case "Flight attendant":
                        attendant = self._prompt(
                            prompt="Enter ID of flight attendant",
                            header_title="Enter ID of flight attendant",
                            validator=lambda e: self.validate_assign_flight_attendant(
                                voyage, e
                            ),
                        )
                        self.logic_wrapper.staff_voyage_attendant(
                            voyage_id, int(attendant)
                        )

                return
            except UICancelException:
                return

    def unstaff_voyage(self):
        self._print_header(message="Unstaff Voyage", add_extra_newline=True)

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
                self._print_header("Unstaff voyage", add_extra_newline=True)
                self._print_centered("ID has to be a number", add_newline_after=True)
                continue

            try:
                voyage = self.logic_wrapper.get_voyage(voyage_id)
                if voyage is None:
                    self._print_header("Staff voyage", add_extra_newline=True)
                    self._print_centered(f"Voyage with id '{voyage_id}' doesn't exist", add_newline_after=True)
                    continue

                pilots_or_attendants = self._display_selection(
                    ["Pilots", "Flight attendant"], header_title="Staff voyage"
                )

                match pilots_or_attendants:
                    case "Pilots":
                        employee_data = []
                        for pilot_id in voyage.pilots:
                            pilot = self.logic_wrapper.get_employee(pilot_id)
                            employee_data.append(
                                [pilot.id, pilot.name, pilot.license, pilot.email]
                            )

                        self._display_interactive_datalist(
                            headers={"id": 3, "name": 20, "license": 10, "email": 20},
                            data=employee_data,
                            title="Currently assigned pilots",
                            return_msg="continue",
                        )

                        pilot = self._prompt(
                            prompt="Enter ID of pilot to unassign",
                            header_title="Enter ID of pilot",
                            opt_instruction="Leave empty to cancel",
                            validator=lambda e: self.validate_unassign_pilot(voyage, e),
                        )
                        self.logic_wrapper.unstaff_voyage_pilot(voyage_id, int(pilot))

                    case "Flight attendant":
                        employee_data = []
                        for attendant_id in voyage.flight_attendants:
                            attendant = self.logic_wrapper.get_employee(attendant_id)
                            employee_data.append(
                                [attendant.id, attendant.name, attendant.email]
                            )

                        self._display_interactive_datalist(
                            headers={"id": 3, "name": 20, "email": 20},
                            data=employee_data,
                            title="Currently assigned flight attendants",
                            return_msg="continue",
                        )

                        attendant = self._prompt(
                            prompt="Enter ID of flight attendant to unassign",
                            header_title="Enter ID of flight attendant",
                            opt_instruction="Leave empty to cancel",
                            validator=lambda e: self.validate_unassign_flight_attendant(
                                voyage, e
                            ),
                        )
                        self.logic_wrapper.unstaff_voyage_attendant(
                            voyage_id, int(attendant)
                        )

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

    def validate_date_after(self, after_date: datetime.date, inp: str):
        err = self.validate_date(inp)
        if err is not None:
            return err

        date = self.parse_date(inp)
        if date < after_date:
            return f"Date must be after {after_date}"

        return None

    def validate_duplicate_voyage_date_departure(self, voyage: Voyage, inp: str):
        error = self.validate_date(inp)
        if error is not None:
            return error

        date = self.parse_date(inp)
        if self.logic_wrapper.validate_departure_time(
            date, voyage.departure_time
        ) and self.logic_wrapper.validate_departure_time(date, voyage.departure_time):
            return None

        return (
            "Duplicate voyage conflicts with another voyage on the new departure date"
        )

    def validate_duplicate_voyage_date_return(self, departure_date: datetime.date, voyage: Voyage, inp: str):
        error = self.validate_date(inp)
        if error is not None:
            return error

        date = self.parse_date(inp)

        if date < departure_date:
            return "End date must be after the start date"

        if self.logic_wrapper.validate_departure_time(
            date, voyage.return_departure_time
        ) and self.logic_wrapper.validate_departure_time(
            date, voyage.return_departure_time
        ):
            return None

        return "Duplicate voyage conflicts with another voyage on the new return date"

    def validate_duplicate_voyage_date_recurring(
        self,
        voyage: Voyage,
        start_date: datetime.date,
        interval: datetime.timedelta,
        inp: str,
    ):
        error = self.validate_date(inp)
        if error is not None:
            return error

        end_date = self.parse_date(inp)
        date = start_date

        if end_date < start_date:
            return "End date must be after the start date"

        dates = []
        time_between_dep_and_ret = voyage.return_date - voyage.departure_date
        plane = self.logic_wrapper.get_plane(voyage.plane)

        while date <= end_date:
            dep = self.logic_wrapper.make_datetime(date, voyage.departure_time)
            ret = self.logic_wrapper.make_datetime(
                date + time_between_dep_and_ret, voyage.return_departure_time
            )

            if not self.logic_wrapper.validate_departure_time(
                date, voyage.departure_time
            ) or not self.logic_wrapper.validate_departure_time(
                date, voyage.return_departure_time
            ):
                return "A duplicate voyage conflicts with another voyage"

            for potential_overlap_date in dates:
                if dep == potential_overlap_date:
                    return f"The recurring voyage overlaps itself on {dep}"
                if ret == potential_overlap_date:
                    return f"The recurring voyage overlaps itself on {ret}"

            if not self.logic_wrapper.validate_plane_availability(plane, dep):
                return f"The assigned plane is not available on {dep}"
            if not self.logic_wrapper.validate_plane_availability(plane, ret):
                return f"The assigned plane is not available on {ret}"

            dates.append(dep)
            dates.append(ret)

            date += interval
            continue

    def validate_departure_time(self, date: datetime.date, inp):
        err = self.validate_time(inp)
        if err is not None:
            return err

        time = self.parse_time(inp)

        if not self.logic_wrapper.validate_departure_time(date, time):
            return "Departure time conflicts with another voyage"

        return None

    def validate_return_departure_time(
        self,
        return_date: datetime.date,
        departure_date: datetime.date,
        departure_time: datetime.time,
        inp: str,
    ):
        err = self.validate_time(inp)
        if err is not None:
            return err

        time = self.parse_time(inp)

        if not self.logic_wrapper.validate_departure_time(return_date, time):
            return "Return departure time conflicts with another voyage"

        if return_date == departure_date and time <= departure_time:
            return "Return departure time cannot be before the departure time"

        return None

    def validate_time(self, inp: str):
        try:
            self.parse_time(inp)
        except:
            return "Invalid time format"

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
            plane_id = int(plane_id)
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
            num = int(inp)
            if num < 0:
                return "Number must be positive"

            return None
        except ValueError:
            return "Input must be a number"

    def validate_pilot_to_assign(
        self,
        departure_date: datetime.date,
        return_date: datetime.date,
        plane_id: int,
        pilot_id: str,
    ):
        err = self.validate_pilot(pilot_id, plane_id)
        if err is not None:
            return err

        if self.logic_wrapper.is_working(
            int(pilot_id), departure_date
        ) or self.logic_wrapper.is_working(int(pilot_id), return_date):
            return "Pilot already assined that day"

        return None

    def validate_attendant_to_assign(
        self,
        departure_date: datetime.date,
        return_date: datetime.date,
        attendant_id: str,
    ):
        err = self.validate_flight_attendant(attendant_id)
        if err is not None:
            return err

        if self.logic_wrapper.is_working(
            int(attendant_id), departure_date
        ) or self.logic_wrapper.is_working(int(attendant_id), return_date):
            return "Attendant already assined that day"

        return None

    def validate_assign_pilot(self, voyage: Voyage, pilot_id: str):
        err = self.validate_pilot(pilot_id, voyage.plane)
        if err is not None:
            return err

        if int(pilot_id) in voyage.pilots:
            return "Pilot already assigned"

        self.logic_wrapper.get_employee(int(pilot_id))

        if self.logic_wrapper.is_working(pilot_id, voyage.departure_date):
            return "Pilot is already working on the departure date"

        if self.logic_wrapper.is_working(pilot_id, voyage.return_date):
            return "Pilot is already working on the return date"

        return None

    def validate_assign_flight_attendant(self, voyage: Voyage, attendant_id: str):
        err = self.validate_flight_attendant(attendant_id)
        if err is not None:
            return err

        if int(attendant_id) in voyage.flight_attendants:
            return "Attendant already assigned"

        attendant = self.logic_wrapper.get_employee(int(attendant_id))

        if self.logic_wrapper.is_working(attendant_id, voyage.departure_date):
            return "Attendant is already working on the departure date"

        if self.logic_wrapper.is_working(attendant_id, voyage.return_date):
            return "Attendant is already working on the return date"

        return None

    def validate_unassign_pilot(self, voyage: Voyage, pilot_id: str):
        err = self.validate_pilot(pilot_id, voyage.plane)
        if err is not None:
            return err

        if int(pilot_id) not in voyage.pilots:
            return "Pilot not assigned"

        return None

    def validate_unassign_flight_attendant(self, voyage: Voyage, attendant_id: str):
        err = self.validate_flight_attendant(attendant_id)
        if err is not None:
            return err

        if int(attendant_id) not in voyage.flight_attendants:
            return "Attendant not assigned"

        return None

    def validate_seats_sold(self, voyage: Voyage, seats_sold: int):
        err = self.validate_number(seats_sold)
        if err is not None:
            return err

        plane = self.logic_wrapper.get_plane(voyage.plane)
        plane_capacity = int(plane.capacity)
        seats_sold = int(seats_sold)

        if seats_sold > plane_capacity:
            return f"The planes maximum capacity is {plane.capacity}"

        else:
            return None

    def validate_seats_sold_by_plane(self, plane_id: str, seats_sold: int):
        err = self.validate_plane(plane_id)
        if err is not None:
            return err

        err = self.validate_number(seats_sold)
        if err is not None:
            return err

        plane = self.logic_wrapper.get_plane(int(plane_id))
        plane_capacity = plane.capacity
        seats_sold = int(seats_sold)

        if seats_sold > plane_capacity:
            return f"The planes maximum capacity is {plane_capacity}"
        else:
            return None

    def validate_voyage(self, inp):
        err = self.validate_number(inp)
        if err is not None:
            return err

        voyage = self.logic_wrapper.get_voyage(int(inp))
        if voyage is not None:
            return None

        return f"Voyage with id '{inp}' doesn't exist"

    def validate_plane_available(
        self,
        departure_date: datetime.date,
        departure_time: datetime.time,
        return_date: datetime.date,
        return_time: datetime.time,
        inp,
    ):
        err = self.validate_plane(inp)
        if err is not None:
            return err

        plane = self.logic_wrapper.get_plane(int(inp))
        departure = self.logic_wrapper.make_datetime(departure_date, departure_time)
        return_departure = self.logic_wrapper.make_datetime(return_date, return_time)

        if self.logic_wrapper.validate_plane_availability(
            plane, departure
        ) and self.logic_wrapper.validate_plane_availability(plane, return_departure):
            return None

        return "Plane is unavailable during that time"

    def parse_date(self, date):
        year, month, day = date.split("-")
        return datetime.date(int(year), int(month), int(day))

    def parse_time(self, date):
        hours, minutes = date.split(":")
        return datetime.time(int(hours), int(minutes))

    def format_employee_list(
        self,
        employees: list[Employee],
        padding_len: int,
        header: int,
        min_len: int,
        max_len: int = None,
    ) -> str:
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

    def format_employee(self, employee_id: str) -> str:
        employee = self.logic_wrapper.get_employee(int(employee_id))
        return f"{employee.name}"
