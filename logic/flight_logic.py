# import os
import datetime
from data.data_wrapper import DataWrapper
from model import Flight
from logic import Validator
from logic import DestinationLogic


class FlightLogic:
    """This is the logic class for flight"""
    def __init__(self, data_wrapper):
        """Initiates flightlogic through data_wrapper"""
        self.data_wrapper = data_wrapper
        self.validator = Validator()
        self.destination_logic = DestinationLogic(data_wrapper)


    def create_flight(self, departure, destination, date, departure_time) -> str:
        """Creates flight, returns flight number"""
        # self.validator.validate_destination(data)
        flight_nr = self.create_flight_nr(destination, departure, date)

        if destination == 0:
            arrival_time = self.calculate_arrival_time(departure_time, departure)
        else:
            arrival_time = self.calculate_arrival_time(departure_time, destination)

        self.data_wrapper.create_flight(
            Flight(
                flight_number = flight_nr,
                departure = departure,
                destination = destination,
                date = date,
                departure_time = departure_time,
                arrival_time = arrival_time,
            )
        )
        
        return flight_nr


    def create_flight_nr(self, destination, departure, date) -> str:
        """Creates a flight number and returns it"""
        # If destination is rvk
        if destination == 0:
            destination_id = departure
        else:
            destination_id = destination

        flight_nr = f"NA0{destination_id}{self.get_same_date_flights(destination_id, date)}"

        return flight_nr


    def get_same_date_flights(self, destination_id, date) -> int:
        """Returns the amount of flights with the same date and destination"""
        all_flights = self.get_all_flight()

        flights_within = 0

        date = f"{date}"
        
        for flight in all_flights:
            # If flights are same destination and date
            print(type(flight.date))
            if flight.destination == 0:
                if flight.departure == destination_id and flight.date == date:
                    flights_within += 1
            else:
                if flight.destination == destination_id and flight.date == date:
                    flights_within += 1

        return flights_within


    def flights_going_to(self, destination) -> list[Flight]:  # With specific destination
        """Finds all flights with a specific destination"""
        all_flights = self.data_wrapper.get_all_flights

        flights_dest = [
            flight for flight in all_flights if flight.flight_nr[2:-1] == str(destination)
        ]

        return flights_dest
    
    
    def calculate_arrival_time(self, departure_time, destination_id) -> datetime:
        """Calculates the arrival time of a flight
        by adding the travel time from Destination to the departure time"""

        destination = self.destination_logic.get_destination(destination_id)
        hours, minutes, seconds = f"{departure_time}".split(":")
        arrival_time = datetime.timedelta(hours = int(hours), minutes = int(minutes)) + datetime.timedelta(minutes = destination.flight_time)

        return arrival_time


    def add_staff_to_flights():
        """Alows you to add staff to a flight after creating it"""

        raise NotImplementedError()


    def get_all_flight(self) -> list[Flight]:
        """Gets list of all flight from data_wrapper and forwards list of flight"""
        return self.data_wrapper.get_all_flights()


    def get_flight(self, flight_nr):  # Flight
        """Gets a specific flight route with a specific ID"""
        flight_list = self.get_all_flight()

        for flight in flight_list:
            if flight.flight_number == flight_nr:
                return flight
        
        return None


    def update_flight(self, id, flight) -> None:
        """Updates flight through data_wrapper"""
        flight.id = id

        self.data_wrapper.update_flight(flight)


    def assign_pilot(self, pilot, flight) -> None:
        """Assigns a pilot to a specific flight"""

        if self.validator.pilot_validator(self.data_wrapper):
            self.data_wrapper.assign_pilot(pilot)

        else:
            return  # raise Error eða none?
