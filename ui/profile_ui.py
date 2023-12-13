from ui import UIElement, UICancelException
from model import Employee, Pilot, Manager, FlightAttendant, FlightManager, Voyage, Destination, Flight
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

            if isinstance(self.user, Manager):
                table.append(f"Work:    {self.user.work_phone}")
            if isinstance(self.user, FlightManager):
                table.append(f"Work:    {self.user.work_phone}")
            if isinstance(self.user, Pilot):
                table.append(f"Assign:  {', '.join(self.user.assignments)}")
                table.append(f"License: {self.user.license}")
            if isinstance(self.user, FlightAttendant):
                table.append(f"Assign:  {self.user.assignments}")

            self._print_header(f"My Profile", add_extra_newline=True)
            self._print_list(table, add_newline_after=True)

            
            
    def get_voyages_in_this_week():
        pass