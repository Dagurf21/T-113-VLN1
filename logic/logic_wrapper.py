# import os
from logic.employee_logic import EmployeeLogic
from logic.flight_route_logic import FlightRouteLogic
from logic.destination_logic import DestinationLogic
from logic.voyage_logic import VoyageLogic
from logic.plane_logic import PlaneLogic

from model.destination import Destination
from model.employee import Employee
from model.flight_route import FlightRoute
from model.flight_attendant import FlightAttendant
from model.flight_manager import FlightManager
from model.manager import Manager
from model.pilot import Pilot
from model.plane import Plane
from model.voyage import Voyage

from data.data_wrapper import DataWrapper


class LogicWrapper(object):
    """This is the logic wrapper class. It is used to call the logic layer classes"""

    def __init__(self):
        """Constructor for LogicWrapper"""
        self.data_wrapper = DataWrapper()
        self.employee_logic = EmployeeLogic(self.data_wrapper)
        self.flight_route_logic = FlightRouteLogic(self.data_wrapper)
        self.destination_logic = DestinationLogic(self.data_wrapper)
        self.voyage_logic = VoyageLogic(self.data_wrapper)
        self.plane_logic = PlaneLogic(self.data_wrapper)

    def create_employee(self, employee) -> None:
        """Takes in a employee object and forwards it to the create_employee function"""
        return self.employee_logic.create_employee(employee)

    def list_all_employees(self) -> list[Employee]:
        """For wards list of employees from logic"""
        return self.employee_logic.list_all_employees()

    def list_employee(self, id) -> Employee:
        """Returns a employee with input ID"""
        return self.employee_logic.list_employee(id)

    def update_employee(self, employee) -> None:
        """Updates info about a employee"""
        return self.employee_logic.update_employee(employee)

    def delete_employee(self, id) -> None:
        """Erases an employee from the record/ via ID"""
        return self.employee_logic.delete_employee(id)

    def create_flight_route(self, data) -> None:
        """Creates an flight route"""
        return self.flight_route_logic.create_flight_route(data)

    def list_all_flight_routes(self) -> list[FlightRoute]:  # Flight route
        """Returns a list of all flight routes"""
        return self.flight_route_logic.list_all_flight_routes()

    def list_flight_route(self, id) -> FlightRoute:  # Flight route
        """Returns a specific flight route/ via ID"""
        return self.flight_route_logic.list_flight_route(id)

    def update_flight_route(self, id, data) -> None:
        """Updates info on flight routes"""
        return self.flight_route_logic.update_flight_route(id, data)

    def delete_flight_route(self, id) -> None:
        """Erases an flight route"""
        return self.flight_route_logic.delete_flight_route(id)

    def assign_pilot(self, id, pilot) -> None:
        """Assigns pilot to a flight route"""
        return self.flight_route_logic.assign_pilot(id,pilot)

    def create_voyage(self, data) -> None:
        """Creates a voyage"""
        return self.voyage_logic.create_voyage(data)

    def list_all_voyages(self) -> list:
        """Returns a list of all current voyages"""
        return self.voyage_logic.list_all_voyages()

    def list_voyage(self, id) -> list[Destination]:
        """Returns a voyage/ via ID"""
        return self.voyage_logic.list_voyage(id)

    def update_voyage(self, voyage) -> None:
        """Updates info on voyage"""
        return self.voyage_logic.update_voyage(voyage)

    def delete_voyage(self, id) -> None:
        """Erases voyage/ via ID"""
        return self.voyage_logic.delete_voyage(id)

    def create_destination(self, data) -> None:
        """Creates a new destination"""
        return self.destination_logic.create_destination(data)

    def list_all_destinations(self) -> list[Destination]:
        """Returns a list of all destinations"""
        return self.destination_logic.list_all_destinations()

    def list_destination(self, id) -> list[Destination]:
        """Returns a Destination/ via ID"""
        return self.destination_logic.list_destination(id)

    def update_destination(self, id, destination) -> None:
        """Updates information about a destination"""
        return self.destination_logic.update_destination(id, destination)

    def delete_destination(self, id) -> None:
        """Erases a destination"""
        return self.destination_logic.delete_destination(id)

    def create_plane(self, data) -> None:
        """Creates a plane in the system"""
        return self.plane_logic.create_plane(data)

    def list_all_planes(self) -> list[Plane]:
        """Returns a list of all planes"""
        return self.plane_logic.list_all_planes()

    def list_plane(self, id) -> Plane:
        """Returns a plane/ via ID"""
        return self.plane_logic.list_plane(id)

    def update_plane(self, id) -> None:
        """updates information on plane"""
        return self.plane_logic.update_plane(id)

    def delete_plane(self, id) -> None:
        """Erases plane from the data"""
        return self.plane_logic.delete_plane(id)