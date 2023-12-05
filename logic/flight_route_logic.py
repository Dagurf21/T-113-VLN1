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
        '''Creates flight route:
                Checks if ID is valid'''

        destination = self.data_wrapper.get_destination(data.id)

        if destination.id == None:
            raise ValueError("Invalid Input")
        
        else:
            self.data_wrapper.create_flight_route(data)

    def list_all_flight_routes(self) -> list: # FlightRoute
        ''' '''
        return self.data_wrapper.get_all_flight_routes
    
    def list_flight_route(self, id): # FlightRoute
        ''' '''
        return self.data_wrapper.get_flight_route(id)
    
    def update_flight_route(self, id) -> None:
        ''' '''
        self.data_wrapper.update_flight_route

    def delete_flight_route(self, id) -> None:
        ''''''
        self.data_wrapper.delete_flight_route(id)
        
    def assign_pilot(self, pilot) -> None:
        ''' '''
        self.data_wrapper
        pass