#import os
from logic.employee_logic import EmployeeLogic
from logic.flight_route_logic import FlightRouteLogic
from logic.destination_logic import DestinationLogic
from logic.voyage_logic import VoyageLogic
from logic.plane_logic import PlaneLogic

from data.data_wrapper import DataWrapper

class LogicWrapper(object):
    
    def __init__(self):
        """Constructor for LogicWrapper"""
        self.data_wrapper = DataWrapper()
        self.employee_logic = EmployeeLogic(self.data_wrapper)
        self.flight_route_logic = FlightRouteLogic(self.data_wrapper)
        self.destination_logic = DestinationLogic(self.data_wrapper)
        self.voyage_logic = VoyageLogic(self.data_wrapper)
        self.plane_logic = PlaneLogic(self.data_wrapper)

    def _employee_logic(self):
        ''' '''


    def _flight_route_logic(self):
        ''' '''
        pass

    def _destination_logic(self):
        ''' '''
        pass

    def _Voyage_logic(self):
        ''' '''
        pass

    def _plane_logic(self):
        ''' '''
        pass

    def create_employee(self) -> None:
        ''' '''
        pass

    def list_all_employees(self) -> list: # Employee
        ''''''
        pass

    def list_employee(self,id):
        ''' '''
        pass

    def update_employee(self,id, data) -> None:
        ''' '''
        pass

    def delete_employee(self,id) -> None:
        ''' '''
        pass

    def create_flight_route(self, data) -> None:
        ''' '''
        pass

    def list_all_flight_routes(self) -> list: # Flight route
        ''' '''
        return []

    def list_flight_route(self, id):
        ''' '''
        pass

    def update_flight_route(self, id) -> None:
        ''' '''
        pass

    def delete_flight_route(self, id) -> None:
        ''' '''
        pass

    def assign_pilot(self, pilot) -> None:
        ''' '''
        pass

    def create_voyage(self, data) -> None:
        ''' '''
        pass
    
    def list_all_voyages(self) -> list:
        ''' '''
        return []

    def list_voyage(self, id) -> list: # Destination
        ''' '''
        return

    def update_voyage(self, id) -> None:
        ''' '''
        pass

    def delete_voyage(self,id) -> None:
        ''' '''
        pass

    def create_destination(self, data) -> None:
        ''' '''
        pass
    
    def list_all_destinations(self) -> list: # Destination
        ''' '''
        return []

    def list_destination(self, id) -> list: # Destination
        ''' '''
        return

    def update_destination(self, id) -> None:
        ''' '''
        pass

    def delete_destination(self, id) -> None:
        ''' '''
        pass
    
    def create_plane(self, data) -> None:
        ''' '''
        pass
    
    def list_all_planes(self) -> list: # Plane
        ''' '''
        return []

    def list_plane(self, id): # Plane
        ''' '''
        return

    def update_plane(self, id) -> None:
        ''' '''
        pass

    def delete_plane(self, id) -> None:
        ''' '''
        pass









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
'''