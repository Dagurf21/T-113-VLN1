#import os
from data.data_wrapper import DataWrapper
from model.flight_route import FlightRoute

class FlightRouteLogic():
    ''' '''

    def __init__ (self):
        ''' '''

        self.data_wrapper = DataWrapper()
        self.flight_route = FlightRoute()

    def create_flight_route(self, data: FlightRoute) -> None:
        ''' '''

        destination = self.data_wrapper.get_destination

        if destination.id == None:
            return
        
        else:
            self.data_wrapper.create_flight_route(data)

    def list_all_flight_routes(self) -> list: # FlightRoute
        ''' '''
        return

    def list_flight_route(self, id): # FlightRoute
        ''' '''
        return
    
    def update_flight_route(self, id) -> None:
        ''' '''
        pass 

    def delete_flight_route(self, id) -> None:
        ''' '''
        pass

    def assign_pilot(self, pilot) -> None:
        ''' '''
        pass