# import os
import datetime

from data.data_wrapper import DataWrapper
from model import Flight
from logic import Validator


class FlightLogic:
    """This is the logic class for flight"""

    def __init__(self, data_wrapper):
        """Initiates flightlogic through data_wrapper"""
        self.data_wrapper = data_wrapper
        self.validator = Validator()


    def create_flight(self, departure, destination, data) -> str:
        """Creates flight, returns flight number"""
        #self.validator.validate_destination(data)
        flight_nr = self.create_flight_nr(destination)
        arrival_time = self.calculate_arrival_time(data.departure_time, destination)
        self.data_wrapper.create_flight(Flight(flight_number = flight_nr, departure = departure, destination = destination, date = data.date, departure_time = data.departure_time, arrival_time = arrival_time))
        return flight_nr
    

    def create_flight_nr(self, destination_id) -> str:
        """Creates a flight number and returns it"""
        flight_nr = f"NA0{destination_id}{nr_flight}"
        # TODO finna út seinustu töluna fyrir nr

    def flights_going_to(self, destination, flights=self.data_wrapper.get_all_flights):
        ''' '''
        
        flights_dest = [flight for flight in flights if flight.flight_nr[2:-1] == str(destination)]

        return flights_dest

    def flights_within(self,start_day,end_day,day) -> list[Flight]:
        '''finds flights between start_day and end_day'''
        
        all_flights = self.data_wrapper.get_all_destinations
            
        flights_within = [flight for flight in all_flights if day < end_day and day > start_day]

        return flights_within

    def calculate_arrival_time(self, departure, destination_id) -> datetime:
        """Calculates the arrival time of a flight
        by adding the travel time from Destination to the departure time"""
        
        detination = self.data_wrapper.get_destination(destination_id)

        arrival_time = departure.deltatime(destination.time)

        return arrival_time


    def get_all_flight(self) -> list[Flight]:
        """Gets list of all flight from data_wrapper and forwards list of flight"""
        return self.data_wrapper.get_all_flight

    def get_flight(self, id):  # Flight
        """Gets a specific flight route with a specific ID"""
        return self.data_wrapper.get_flight(id)

    def update_flight(self, id, flight) -> None:
        """Updates flight through data_wrapper"""
        flight.id = id

        self.data_wrapper.update_flight(flight)

    def delete_flight(self, id, flight) -> None:
        """Deletes flight through data_wrapper"""

        if id == self.data_wrapper.get_flight(id):
            self.data_wrapper.delete_flight(id)

        else:
            raise ValueError("404 invalid ID")

    def assign_pilot(self, pilot, flight) -> None:
        """Assigns a pilot to a specific flight"""

        if self.validator.pilot_validator(self.data_wrapper):
            self.data_wrapper.assign_pilot(pilot)

        else:
            return  # raise Error eða none?
