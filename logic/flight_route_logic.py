#import os
from data.data_wrapper import DataWrapper
from model.flight_route import FlightRoute

class FlightRouteLogic():
    '''This is the logic class for flight route'''

    def __init__ (self, data_wrapper):
        '''Initiates flightroutelogic through data_wrapper'''
        self.data_wrapper = data_wrapper

    def create_flight_route(self, data: FlightRoute) -> None:
        '''Creates flight route:
                Checks if ID is valid'''

        destination = self.data_wrapper.get_destination(data.id)

        if destination.id == None:
            self.data_wrapper.create_flight_route(data)
        
        else:
            raise ValueError("Invalid Input")

    def list_all_flight_routes(self) -> list[FlightRoute]:
        '''Gets list of all flight_routes from data_wrapper and forwards list of flight_routes'''
        return self.data_wrapper.get_all_flight_routes
    
    def list_flight_route(self, id): # FlightRoute
        '''Gets a specific flight route with a specific ID'''
        return self.data_wrapper.get_flight_route(id)
    
    def update_flight_route(self, id, FlightRoute) -> None:
        '''Updates flightroute through data_wrapper'''
        FlightRoute.id = id

        self.data_wrapper.update_flight_route(id, data)

    def delete_flight_route(self, id) -> None:
        '''Deletes flight route through data_wrapper'''
        self.data_wrapper.delete_flight_route(id)
        
    def assign_pilot(self, pilot) -> None:
        '''Assigns a pilot to a specific flight route'''
        self.data_wrapper.assign_pilot(pilot)