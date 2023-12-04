#import os
from data.data_wrapper import Data_Wrapper

class Flight_route_logic(Data_Wrapper):

    def __init__ (self):

        self.id: int
        self.flight_number: str
        self.departure: str # Destination
        self.destination: str # Destination
        self.departure_time: str
        self.arrival_time: str

        pass

    def create_flight_route(self, data) -> None:
        
        pass

    def list_all_flight_routes(self) -> list: # FlightRoute
        return

    def list_flight_route(self, id): # FlightRoute
        return
    
    def update_flight_route(self, id) -> None:
        pass 

    def delete_flight_route(self, id) -> None:
        pass

    def assign_pilot(self, pilot) -> None:
        pass