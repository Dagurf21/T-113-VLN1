#import os
from data.data_wrapper import DataWrapper
from model.flight import Flight

class FlightLogic():
    '''This is the logic class for flight'''

    def __init__ (self, data_wrapper):
        '''Initiates flightlogic through data_wrapper'''
        self.data_wrapper = data_wrapper

    def create_flight(self, data: FlightRoute) -> None:
        '''Creates flight:
                Checks if ID is valid'''
        
        

        destination = self.data_wrapper.get_destination(data.id)

        if destination.id == None:
            self.data_wrapper.create_flight(data)
        
        else:
            raise ValueError("Invalid Input")

    def list_all_flight(self) -> list[Flight]:
        '''Gets list of all flight from data_wrapper and forwards list of flight'''
        return self.data_wrapper.get_all_flight
    
    def list_flight(self, id): # Flight
        '''Gets a specific flight route with a specific ID'''
        return self.data_wrapper.get_flight(id)
    
    def update_flight(self, id, flight) -> None:
        '''Updates flight through data_wrapper'''
        flight.id = id

        self.data_wrapper.update_flight(flight)

    def delete_flight(self, id, flight) -> None:
        '''Deletes flight through data_wrapper'''
        
        if id == self.data_wrapper.get_flight(id):
            self.data_wrapper.delete_flight(id)
        
        else:
            raise ValueError("404 invalid ID")

    def assign_pilot(self, pilot, flight) -> None:
        '''Assigns a pilot to a specific flight'''

        #if flight_route.pilot != 
        self.data_wrapper.assign_pilot(pilot)