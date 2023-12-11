from model import Voyage
from logic import Validator
from logic import FlightLogic
from model import Flight
import datetime


class VoyageLogic:
    """This class handles all the logic for the Voyage class."""

    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
        self.validate = Validator()
        self.flight_logic = FlightLogic(data_connection)
        

    def create_voyage(self, data: str) -> None:
        """Takes in a voyage object and forwards it to the data layer"""
        # flight_data = Flight(date=data.date,destination=data.destination)
        # create_flight(flight_data)
        plane, destination, date, return_date, departure_time, arrival_departure_time, sold_seats, flight_attendants, pilots = self.cleanup_data(data)
        departure_flight = self.flight_logic.create_flight(departure = 0,destination = destination, date = date, departure_time = departure_time)
        arrival_flight = self.flight_logic.create_flight(departure = destination, destination = 0, date = return_date, departure_time = arrival_departure_time)
        # TODO return date
        self.data_wrapper.create_voyage(
            Voyage(
                destination = destination,
                sold_seats = sold_seats,
                plane = plane,
                pilots = pilots,
                flight_attendants = flight_attendants,
                departure_time = departure_time,
                departure_flight = departure_flight,
                arrival_departure_time = arrival_departure_time,
                arrival_flight = arrival_flight,
                date = date,
                return_date = return_date,
                status = "Not started",
            )
        )


    def cleanup_data(self, data):
        """"""
        plane, destination, date, return_date, departure_time, arrival_departure_time, sold_seats, flight_attendants, pilots = data.split(";")
        plane = int(plane)
        destination = int(destination)
        
        year, month, day = self.split_date(date)
        date = datetime.date(year = year, month = month, day = day)

        year, month, day = self.split_date(return_date)
        return_date = datetime.date(year = year, month = month, day = day)

        hour, minutes = self.split_time(departure_time)
        departure_time = datetime.time(hour = hour, minute = minutes)

        hour, minutes = self.split_time(arrival_departure_time)
        arrival_departure_time = datetime.time(hour = hour, minute = minutes)

        sold_seats = int(sold_seats)
        flight_attendants_list = flight_attendants.split()
        pilots_list = pilots.split()

        return plane, destination, date, return_date, departure_time, arrival_departure_time, sold_seats, flight_attendants_list, pilots_list


    def split_date(self, date):
        """"""
        year, month, day = date.split("-")

        return int(year), int(month), int(day)


    def split_time(self, time):
        """"""
        hour, minutes = time.split(":")

        return int(hour), int(minutes)


    def get_all_voyages(self) -> list:
        """Returns a list of all voyages"""

        all_voyages = self.data_wrapper.get_all_voyages()
        now = datetime.datetime.now

        for Voyage in all_voyages:
            
            if Voyage.date == now:
                Voyage.status = "IN AIR"
            
            elif Voyage.date > now:
                Voyage.status = ""
            
            else:
                Voyage.status = ""
            

        return all_voyages


    def get_voyage(self, voyage_id):
        """Returns a voyage object with the given id"""
        voyage_list = self.get_all_voyages()

        for voyage in voyage_list:
            if voyage.id == voyage_id:
                return voyage

        return None

    def update_voyage(self, voyage) -> None:
        """Updates a voyage object with the given id"""
        return self.data_wrapper.update_voyage(voyage)

    def delete_voyage(self, id) -> None:
        """Deletes a voyage object with the given id"""
        return self.data_wrapper.delete_voyage(id)


# Verify:
#
#####################if country is allowed based on assignment description (duh) WE handle it in flight class
#
# job positions
#
# Date time validation
#
# Valid status?
#
#
#
#
#
