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

    def create_flight(self, data: Flight) -> None:
        """Creates flight: Checks if ID is valid"""

        available_destinations = self.data_wrapper.get_all_destinations()

        dest = self.data_wrapper.get_destination(data.id)

        destination = data.destination
        departure = data.destination

        if dest.id == None:
            # flightnumber_validator(data)
            self.data_wrapper.create_flight(data)

        else:
            raise ValueError("Invalid Input")

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
