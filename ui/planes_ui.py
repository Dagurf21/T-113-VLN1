import datetime
from ui import UIElement, UICancelException
from model import Plane, Employee, PlaneStatus
from logic import LogicWrapper

class PlaneUI(UIElement):
    def __init__(self, user: Employee, logic_wrapper: LogicWrapper):
        self.user = user
        self.logic_wrapper = logic_wrapper

    def show(self):
        while True:
            try:
                option = self._display_selection(
                    [
                        "List planes",
                        "List plane",
                        "Register plane", 
                        "Remove plane", 
                    ],
                    header_title="Planes"
                )
            except UICancelException:
                return

            match option:
                case "List planes":
                    self.display_plane_list()
                    
                case "List plane":
                    self.display_plane()

                case "Register plane":
                    self.register_plane()

                case "Remove plane":
                    self.remove_plane()

    def display_plane_list(self):
        planes = self.logic_wrapper.get_all_planes()
        planes_data = []

        for plane in planes:
            plane_status = self.logic_wrapper.get_plane_status(plane)

            if plane_status == PlaneStatus.InFlight:
                active_flight = self.logic_wrapper.get_plane_active_flight(plane)
                destination = self.logic_wrapper.get_destination(active_flight.destination)
                plane_status = f"{plane_status:<9} -> [{active_flight.flight_number}] {destination.airport:.9}. - arr: {active_flight.arrival_time}"
            elif plane_status == PlaneStatus.InUse:
                active_voyage = self.logic_wrapper.get_plane_active_voyage(plane)
                destination = self.logic_wrapper.get_destination(active_voyage.destination)
                return_flight = self.logic_wrapper.get_flight(active_voyage.return_flight, active_voyage.return_date)
                available = datetime.datetime(
                    active_voyage.return_date.year,
                    active_voyage.return_date.month,
                    active_voyage.return_date.day,
                    hour=return_flight.arrival_time.hour,
                    minute=return_flight.arrival_time.minute,
                )
                plane_status = f"{plane_status:<9} -> {destination.airport} - av: {available}"
                
            
            planes_data.append([
                plane.id,
                plane.name, 
                plane.ty,
                plane.capacity,
                plane_status,
            ])

        self._display_interactive_datalist(
            { "ID": 3, "name": 12, "Type": 8, "Seats": 5, "Status": 54 },
            planes_data
        )
        # Should work, not sure about the spacing

    def display_plane(self):
        self._print_header("List plane", add_extra_newline=True)

        while True:
            try:
                plane_id = self._prompt(
                    "Enter plane id",
                    opt_instruction="Leave empty to cancel",
                    clear_screen=False
                )
            except UICancelException:
                return

            try: 
                plane_id = int(plane_id)
            except ValueError:
                self._print_header("List Plane", add_extra_newline=True)
                self._print_centered("ID has to be a number", add_newline_after=True)
                continue

            plane = self.logic_wrapper.get_plane(plane_id)

            if plane == None:
                self._print_header("List Plane", add_extra_newline=True)
                self._print_centered(f"Plane with ID {plane_id} does not exist", add_newline_after=True)
                continue

            plane_status = self.logic_wrapper.get_plane_status(plane)
            status_list = []

            if plane_status == PlaneStatus.InFlight:
                active_flight = self.logic_wrapper.get_plane_active_flight(plane)
                active_voyage = self.logic_wrapper.get_plane_active_voyage(plane)
                destination = self.logic_wrapper.get_destination(active_flight.destination)
                return_flight = self.logic_wrapper.get_flight(active_voyage.return_flight, active_voyage.return_date)
                available = datetime.datetime(
                    active_voyage.return_date.year,
                    active_voyage.return_date.month,
                    active_voyage.return_date.day,
                    hour=return_flight.arrival_time.hour,
                    minute=return_flight.arrival_time.minute,
                )
                status_list.append(f"Arrives on:     {active_flight.arrival_time}")
                status_list.append(f"Next Available: {available}")

            elif plane_status == PlaneStatus.InUse:
                active_voyage = self.logic_wrapper.get_plane_active_voyage(plane)
                destination = self.logic_wrapper.get_destination(active_voyage.destination)
                return_flight = self.logic_wrapper.get_flight(active_voyage.return_flight, active_voyage.return_date)
                available = datetime.datetime(
                    active_voyage.return_date.year,
                    active_voyage.return_date.month,
                    active_voyage.return_date.day,
                    hour=return_flight.arrival_time.hour,
                    minute=return_flight.arrival_time.minute,
                )
                status_list.append(f"Next Available: {available}")
            
            self._print_header(f"List Plane [id: {plane_id}]", add_extra_newline=True)
            self._print_list([
                f"ID:             {plane.id}",
                f"Name:           {plane.name}",
                f"Type:           {plane.ty}",
                f"Manufacturer:   {plane.manufacturer}",
                f"Capacity:       {plane.capacity}",
                f"Status:         {plane_status}",
                *status_list
            ], add_newline_after=True)

    def register_plane(self):
        try:
            name          = self._prompt("Enter name",            header_title="Register Plane", opt_instruction="Leave empty to cancel")
            plane_type    = self._prompt("Enter type",            header_title="Register Plane", opt_instruction="Leave empty to cancel")
            manufacturer  = self._prompt("Enter manufacturer",    header_title="Register Plane", opt_instruction="Leave empty to cancel")
            capacity      = int(self._prompt("Enter capacity",        header_title="Register Plane", opt_instruction="Leave empty to cancel"))
            #flights       = self._display_prompt("Enter ",            header_title="Register Plane", opt_instruction="Leave empty to cancel")
            # Not sure if we add flights now or later
            # O

            plane = Plane(
                name=name,
                ty=plane_type,
                manufacturer=manufacturer, 
                capacity=capacity
            )
            # Getting error when creating plane needing argument "flights"

            self.logic_wrapper.create_plane(plane)
        except UICancelException:
            return

    def remove_plane(self):
        self._print_header("Remove Plane", add_extra_newline=True)

        while True:
            try:
                try:
                    plane_id = self._prompt("Enter plane ID", opt_instruction="Leave empty to cancel", clear_screen=False)
                    plane_id = int(plane_id)
                except ValueError:
                    self._print_header("Remove Plane", add_extra_newline=True)
                    self._print_centered("ID has to be a number", add_newline_after=True)
                    continue

                plane = self.logic_wrapper.get_plane(plane_id)

                if plane == None:
                    self._print_header("Remove Plane", add_extra_newline=True)
                    self._print_centered(f"Plane with id {plane_id} doesn't exist", add_newline_after=True)
                    continue

                should_delete = self._display_selection(
                    [
                        "Delete"
                    ], 
                    header_title=f"Delete {plane.name} ID: {plane.id}?",
                    allow_cancel=False
                )

                if should_delete == "Delete":
                    self.logic_wrapper.delete_plane(plane_id)
                    
                return
            except UICancelException:
                return

