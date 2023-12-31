import datetime
from ui import UIElement, UICancelException
from model import Destination, Employee
from logic import LogicWrapper

class DestinationUI(UIElement):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper

    def show(self):
        while True:
            try:
                option = self._display_selection(
                    [
                        "List destinations",
                        "List destination",
                        "Register destination",
                        "Update destination",
                        "Remove destination",
                    ],
                    header_title="Destinations"
                )
            except UICancelException:
                return

            match option:
                case "List destinations":
                    self.list_destinations()
                    self._print_header(message="Completed Successfully") # Not sure, may change

                case "List destination":
                    self.list_destination()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                
                case "Register destination":
                    self.register_destination()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                
                case "Update destination":
                    self.update_destination()
                    self._print_header(message="Completed Successfully") # Not sure, may change
                
                case "Remove destination": # Remove destination
                    self.remove_destination()
                    self._print_header(message="Completed Successfully") # Not sure, may change

    def list_destinations(self):
        destinations = self.logic_wrapper.get_all_destinations()
        destination_data = []

        for destination in destinations:
            destination_data.append([
                destination.id,
                destination.country,
                destination.airport,
                f"{destination.distance_km}KM",
                destination.flight_time,
                destination.representative,
                destination.emergency_number,
            ])

        self._display_interactive_datalist(
            { "id": 3, "country": 8, "airp.": 5, "dist.": 7, "time": 5, "representetive": 14, "e. phone": 8 }, 
            destination_data,
            title="Destinations",
        )
    
    def list_destination(self):
        self._print_header(
            message="List Destination",
            add_extra_newline=True
        )

        while True:
            try:
                destination_id = self._prompt(
                    "Enter destination id",
                    opt_instruction="Leave empty to cancel",
                    clear_screen=False
                )
            except UICancelException:
                return

            try:
                destination_id = int(destination_id)
            except ValueError:
                self._print_header("List Destination", add_extra_newline=True)
                self._print_centered("Id has to be a number", add_newline_after=True)
                continue
                
            destination = self.logic_wrapper.get_destination(destination_id)

            if destination == None:
                self._print_header("List Destination", add_extra_newline=True)
                self._print_centered(f"Destination with id {destination_id} doesn't exist", add_newline_after=True)
                continue

            self._print_header(f"List Destination [id:{destination.id}]", add_extra_newline=True)
            self._print_list([
                f"Id:             {destination.id}",
                f"Country:        {destination.country}",
                f"Airport:        {destination.airport}",
                f"Distance:       {destination.distance_km}",
                f"Flight Time:    {destination.flight_time}KM",
                f"Representative: {destination.representative}",
                f"Emerg. Number:  {destination.emergency_number}"
            ], add_newline_after=True)

    def register_destination(self):
        try:
            country          = self._prompt("Enter country",             header_title="Register Destination", opt_instruction="Leave empty to cancel")
            airport          = self._prompt("Enter airport",             header_title="Register Destination", opt_instruction="Leave empty to cancel", validator=self.validate_airport)
            distance_km      = self._prompt("Enter distance (km)",       header_title="Register Destination", opt_instruction="Leave empty to cancel", validator=self.validate_number)
            flight_time      = self._prompt("Enter flight time (00:00)", header_title="Register Destination", opt_instruction="Leave empty to cancel", validator=self.validate_time_delta)
            representative   = self._prompt("Enter representative name", header_title="Register Destination", opt_instruction="Leave empty to cancel")
            emergency_number = self._prompt("Enter emergency number",    header_title="Register Destination", opt_instruction="Leave empty to cancel", validator=self.validate_phone_number)

            destination = Destination(
                country=country,
                airport=airport,
                distance_km=distance_km,
                flight_time=int(self.parse_time_delta(flight_time).total_seconds() // 60),
                representative=representative,
                emergency_number=emergency_number
            )

            self.logic_wrapper.create_destination(destination)

        except UICancelException:
            return
    
    def update_destination(self):
        self._print_header(
            "Update Destination",
            add_extra_newline=True
        )

        while True:
            try:
                destination_id = self._prompt(
                    "Enter destination id",
                    opt_instruction="Leave empty to cancel",
                    clear_screen=False
                )
                destination_id = int(destination_id)
            except UICancelException:
                return
            except ValueError:
                self._print_header("List Destination", add_extra_newline=True)
                self._print_centered("Id has to be a number", add_newline_after=True)
                continue
                
            try:
                destination = self.logic_wrapper.get_destination(destination_id)

                if destination == None:
                    self._print_header("List Destination", add_extra_newline=True)
                    self._print_centered(f"Destination with id {destination_id} doesn't exist", add_newline_after=True)
                    continue

                destination_fields = [
                    "Representative",
                    "Emergency Number"
                ]

                # Add options depending on the destination type
                field_to_update = self._display_selection(
                    destination_fields,
                    header_title=f"Update Destination [{destination.airport} ({destination.country})]"
                )

                match field_to_update:
                    case "Representative": # Representative
                        destination.representative = self._prompt(
                            "Enter new representative",
                            opt_instruction="Leave empty to cancel"
                        )
                    case "Emergency Number": # Emergency Number
                        destination.emergency_number = self._prompt(
                            "Enter new emergency number",
                            opt_instruction="Leave empty to cancel",
                            validator=self.validate_phone_number
                        )

                self.logic_wrapper.update_destination(destination)

                return
            except UICancelException:
                return

    def remove_destination(self):
        self._print_header("Remove Destination", add_extra_newline=True)

        while True:
            try:
                destination_id = self._prompt("Enter destination id", opt_instruction="Leave empty to cancel", clear_screen=False)
                destination_id = int(destination_id)
            except UICancelException:
                return
            except ValueError:
                self._print_header("Remove Destination", add_extra_newline=True)
                self._print_centered("Id has to be a number", add_newline_after=True)
                continue
                
            try:
                destination = self.logic_wrapper.get_destination(destination_id)

                if destination == None:
                    self._print_header("Remove Destination", add_extra_newline=True)
                    self._print_centered(f"Destination with id {destination_id} doesn't exist", add_newline_after=True)
                    continue

                should_delete = self._display_selection(
                    [
                        "Delete"
                    ],
                    header_title=f"Delete {destination.airport} ({destination.country})?",
                    allow_cancel=False
                )

                if should_delete == "Delete":
                    self.logic_wrapper.delete_destination(destination_id)
    
                return
            except UICancelException:
                return
    
    def validate_airport(self, inp):
        destinations = self.logic_wrapper.get_all_destinations()
        for destination in destinations:
            if destination.airport == inp:
                return "Cannot have duplicate voyage"
        
        return None

    def validate_time_delta(self, inp):
        if len(inp) != 5:
            return "Invalid date format"
        
        try:
            self.parse_time_delta(inp)
        except:
            return "Invalid date format"

    def validate_phone_number(self, inp):
        if self.logic_wrapper.validate_phone_number(inp):
            return None

        return "Invalid phone number"

    def validate_number(self, inp):
        try:
            int(inp)
            return None
        except ValueError:
            return "Input must be a number"

    def parse_time_delta(self, date) -> datetime.timedelta:
        hours, minutes = date.split(':')
        return datetime.timedelta(hours=int(hours), minutes=int(minutes))

