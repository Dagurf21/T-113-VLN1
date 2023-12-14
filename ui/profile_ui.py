import datetime
from ui import UIElement
from model import Employee, Pilot, Manager, FlightAttendant, FlightManager, Voyage, VoyageStatus, Destination, Flight
from logic import LogicWrapper
from colorama import Fore

class ProfileUI(UIElement):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper

    def show(self):
        self._print_header(
            message="My Profile",
            add_extra_newline=True
        )

        while True:
            table = [
                f"Id:      {self.user.id}",
                f"Name:    {self.user.name}",
                f"Email:   {self.user.email}",
                f"SSN:     {self.user.ssn}",
                f"Mobile:  {self.user.mobile_phone}",
                f"Home:    {self.user.home_phone}"
            ]
            options = ["q: return"]

            if isinstance(self.user, Manager):
                table.append(f"Work:    {self.user.work_phone}")
            if isinstance(self.user, FlightManager):
                table.append(f"Work:    {self.user.work_phone}")
            if isinstance(self.user, Pilot):
                table.append(f"Assign:  {', '.join(self.user.assignments)}")
                table.append(f"License: {self.user.license}")
                options.append("a: assignments")
            if isinstance(self.user, FlightAttendant):
                table.append(f"Assign:  {self.user.assignments}")
                options.append("a: assignments")

            self._print_header(f"My Profile", add_extra_newline=True)
            self._print_list(table, add_newline_after=True)

            self._print_centered(" - ".join(options), add_newline_after=True)

            c = self._getkey()
            match c:
                case "a":
                    if not isinstance(self.user, Pilot) and not isinstance(self.user, FlightAttendant):
                        continue

                    self.list_assigned_voyages_this_week()
                case "q":
                    break
            
    def list_assigned_voyages_this_week(self):
        today = datetime.date.today()
        next_week = today + datetime.timedelta(weeks=1)

        voyages = []
        for voyage_id in self.user.assignments:
            voyage: Voyage = self.logic_wrapper.get_voyage(voyage_id)

            if next_week >= voyage.departure_date >= today or next_week >= voyage.return_date >= today:
                voyages.append(voyage)

        voyage_data = []
        for voyage in voyages:
            voyage_data.append(
                [
                    voyage.id,
                    voyage.departure_flight,
                    voyage.return_flight,
                    voyage.sold_seats,
                    voyage.departure_date,
                    voyage.return_date,
                    voyage.status,
                ]
            )

        self._display_interactive_datalist(
            {
                "id": 3,
                "From": 6,
                "DEST": 6,
                "Seats": 5,
                "Date": 10,
                "Return date": 11,
                "Status": 15,
            },
            voyage_data,
            title="Voyages",
        )
