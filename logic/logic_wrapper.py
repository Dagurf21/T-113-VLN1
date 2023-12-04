
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

    def list_all_employees(self) -> list[]:
        pass

    def list_employee(self,id):
        pass

    def update_employee(self,id, data) -> None:
        pass

    def delete_employee(self,id) -> None:
        pass

    def create_flight_route(self, data) ->:
        pass

    def list_all_flight_routes(self) -> list:
        pass

    def list_flight_route(self, id):
        pass

    def update_flight_route(self, id) -> None:
        pass

    def delete_flight_route(self, id): void
+ assign_pilot(pilot): void
+ create_voyage(data): void
+ list_all_voyages(): list[Voyage..*]
+ list_voyage(id): Destination
+ update_voyage(id): void
+ delete_voyage(iid): void
+ create_destination(data): void
+ list_all_destinations(): list[Destination..*]
+ list_destination(id): Destination
+ update_destination(id): void
+ delete_destination(iid): void
+ create_plane(data): void
+ list_all_planes(): list[Plane...*]
+ list_plane(id): Plane
+ update_plane(id): void
+ delete_plane(iid): void









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