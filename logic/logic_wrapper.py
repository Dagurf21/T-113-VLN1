
class Logic_Wrapper(object):
    
    def __init__(self):
        pass

    def _employee_logic(self):
        pass

    def _flight_route_logic(self):
        pass

    def _destination_logic(self):
        pass

    def _Voyage_logic(self):
        pass

    def _plane_logic(self):
        pass

    def create_employee(self) -> None:
        pass

    def list_all_employees(self) -> list: # Employee
        pass

    def list_employee(self,id):
        pass

    def update_employee(self,id, data) -> None:
        pass

    def delete_employee(self,id) -> None:
        pass

    def create_flight_route(self, data) -> None:
        pass

    def list_all_flight_routes(self) -> list: # Flight route
        return []

    def list_flight_route(self, id):
        pass

    def update_flight_route(self, id) -> None:
        pass

    def delete_flight_route(self, id) -> None:
        pass

    def assign_pilot(self, pilot) -> None:
        pass

    def create_voyage(self, data) -> None:
        pass
    
    def list_all_voyages(self) -> list:
        return []

    def list_voyage(self, id) -> : # Destination
        return

    def update_voyage(self, id) -> None:
        pass

    def delete_voyage(self,id) -> None:
        pass

    def create_destination(self, data) -> None:
        pass
    
    def list_all_destinations(self) -> list: # Destination
        return []

    def list_destination(self, id) -> : # Destination
        return

    def update_destination(self, id) -> None:
        pass

    def delete_destination(self, id) -> None:
        pass
    
    def create_plane(self, data) -> None:
        pass
    
    def list_all_planes(self) -> list: # Plane
        return []

    def list_plane(self, id): # Plane
        return

    def update_plane(self, id) -> None:
        pass

    def delete_plane(self, id) -> None:
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