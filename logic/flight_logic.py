# import os
import datetime
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
        if self.destination_logic.get_destination(departure) is None or self.destination_logic.get_destination(destination) is None:
            return

        flight_nr = self.create_flight_nr(destination, departure, date)

        if destination == 0:
            arrival_time = self.calculate_arrival_time(date, departure_time, departure)
        else:
            arrival_time = self.calculate_arrival_time(date, departure_time, destination)

        self.data_wrapper.create_flight(
            Flight(
                flight_number = flight_nr,
                departure = departure,
                destination = destination,
                date = date,
                departure_time = departure_time,
                arrival_time = arrival_time.time(),
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

        for flight in all_flights:
            # If flights are same destination and date
            if flight.destination == 0:
                if flight.departure == destination_id and flight.date == date:
                    flights_within += 1
            else:
                if flight.destination == destination_id and flight.date == date:
                    flights_within += 1

        return flights_within


    def flights_going_to(self, destination_id: int) -> list[Flight]:  # With specific destination
        """Finds all flights with a specific destination"""
        
        if self.destination_logic.get_destination(destination_id) is None:
            return []

        flights = []
        for flight in self.get_all_flight():
            if flight.departure == destination_id or flight.destination == destination_id:
                flights.append(flight)

        return flights
    
    
    def calculate_arrival_time(self, departure_date: datetime.date, departure_time: datetime.time, destination_id: int) -> datetime.datetime:
        """Calculates the arrival time of a flight
        by adding the travel time from Destination to the departure time"""

        destination = self.destination_logic.get_destination(destination_id)
        departure = datetime.datetime(
            departure_date.year,
            departure_date.month,
            departure_date.day,
            hour=departure_time.hour,
            minute=departure_time.minute
        )

        arrival_time = departure + datetime.timedelta(minutes = destination.flight_time)

        return arrival_time


    def get_all_flight(self) -> list[Flight]:
        """Gets list of all flight from data_wrapper and forwards list of flight"""
        return self.data_wrapper.get_all_flights()


    def get_flight(self, flight_nr: str, date: datetime.date):  # Flight
        """Gets a specific flight route with a specific ID"""
        flight_list = self.get_all_flight()

        for flight in flight_list:
            if flight.flight_number == flight_nr and flight.date == date:
                return flight
        
        return None


    def update_flight(self, flight_number: str, date: datetime.date, flight: Flight) -> None:
        """Updates flight through data_wrapper"""

        existing_flight = self.get_flight(flight_number, date)
        existing_flight.departure_time = flight.departure_time
        existing_flight.arrival_time = flight.arrival_time

        self.data_wrapper.update_flight(flight)
