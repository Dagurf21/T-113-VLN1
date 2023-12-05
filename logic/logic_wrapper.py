# import os
from logic.employee_logic import EmployeeLogic
from logic.flight_route_logic import FlightRouteLogic
from logic.destination_logic import DestinationLogic
from logic.voyage_logic import VoyageLogic
from logic.plane_logic import PlaneLogic

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

    def list_all_employees(self) -> list:  # List(Employee)
        """ """
        return self.employee_logic.list_all_employees()

    def list_employee(self, id):  # Employee
        """ """
        return self.employee_logic.list_employee(id)

    def update_employee(self, id, employee) -> None:
        """ """
        return self.employee_logic.update_employee(id, employee)

    def delete_employee(self, id) -> None:
        """ """
        return self.employee_logic.delete_employee(id)

    def create_flight_route(self, data) -> None:
        """ """
        return self.flight_route_logic.create_flight_route(data)

    def list_all_flight_routes(self) -> list:  # Flight route
        """ """
        return self.flight_route_logic.list_all_flight_routes()

    def list_flight_route(self, id):  # Flight route
        """ """
        return self.flight_route_logic.list_flight_route(id)

    def update_flight_route(self, id, data) -> None:
        """ """
        return self.flight_route_logic.update_flight_route(id)

    def delete_flight_route(self, id) -> None:
        """ """
        return self.flight_route_logic.delete_flight_route(id)

    def assign_pilot(self, id, pilot) -> None:
        """ """
        return self.flight_route_logic.assign_pilot(pilot)

    def create_voyage(self, data) -> None:
        """ """
        return self.voyage_logic.create_voyage(data)

    def list_all_voyages(self) -> list:
        """ """
        return self.voyage_logic.list_all_voyages()

    def list_voyage(self, id) -> list:  # Destination
        """ """
        return self.voyage_logic.list_voyage(id)

    def update_voyage(self, id, voyage) -> None:
        """ """
        return self.voyage_logic.update_voyage(id, voyage)

    def delete_voyage(self, id) -> None:
        """ """
        return self.voyage_logic.delete_voyage(id)

    def create_destination(self, data) -> None:
        """ """
        return self.destination_logic.create_destination(data)

    def list_all_destinations(self) -> list:  # Destination
        """ """
        return self.destination_logic.list_all_destinations()

    def list_destination(self, id) -> list:  # Destination
        """ """
        return self.destination_logic.list_destination(id)

    def update_destination(self, id, destination) -> None:
        """ """
        return self.destination_logic.update_destination(id, destination)

    def delete_destination(self, id) -> None:
        """ """
        return self.destination_logic.delete_destination(id)

    def create_plane(self, data) -> None:
        """ """
        return self.plane_logic.create_plane(data)

    def list_all_planes(self) -> list:  # Plane
        """ """
        return self.plane_logic.list_all_planes()

    def list_plane(self, id):  # Plane
        """ """
        return self.plane_logic.list_plane(id)

    def update_plane(self, id) -> None:
        """ """
        return self.plane_logic.update_plane(id)

    def delete_plane(self, id) -> None:
        """ """
        return self.plane_logic.delete_plane(id)


'''
# Example from T-113-VLN1

from logic.customer_logic import Customer_Logic
from data.data_wrapper import Data_Wrapper

#class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.customer_logic = Customer_Logic(self.data_wrapper)

    def create_customer(self, customer):
        """Takes in a customer object and forwards it to the data layer"""
        return self.customer_logic.create_customer(customer)

    def get_all_customers(self):
        return self.customer_logic.get_all_customers()

    def _employee_logic(self):
        """ """
        return self.employee_logic

    def _flight_route_logic(self):
        """ """
        return self.flight_route_logic

    def _destination_logic(self):
        """ """
        return self.destination_logic

    def _Voyage_logic(self):
        """ """
        return self.voyage_logic

    def _plane_logic(self):
        """ """
        return PlaneLogic
'''
