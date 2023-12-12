from model import Voyage, VoyageStatus
from logic import Validator, FlightLogic
import datetime


class VoyageLogic:
    """This class handles all the logic for the Voyage class."""

    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
        self.validate = Validator()
        self.flight_logic = FlightLogic(data_connection)

    def create_voyage(self, plane_id: int, destination_id: int, date: datetime, return_departure_date: datetime, departure_time: datetime, return_departure_time: datetime, sold_seats: int, flight_attendants: list[int], pilots: list[int]) -> None:
        """Takes in a voyage object and forwards it to the data layer"""
        # flight_data = Flight(date=data.date,destination=data.destination)
        # create_flight(flight_data)
        departure_flight = self.flight_logic.create_flight(0, destination_id, date, departure_time)
        arrival_flight = self.flight_logic.create_flight(destination_id, 0, return_departure_date, return_departure_time)
        # TODO return date
        self.data_wrapper.create_voyage(
            Voyage(
                destination = destination_id,
                sold_seats = sold_seats,
                plane = plane_id,
                pilots = pilots,
                flight_attendants = flight_attendants,
                departure_time = departure_time,
                departure_flight = departure_flight,
                arrival_departure_time = return_departure_time,
                arrival_flight = arrival_flight,
                date = date,
                return_date = return_departure_date,
                status = VoyageStatus.NotStarted,
            )
        )

    def get_all_voyages(self) -> list:
        """Returns a list of all voyages"""

        all_voyages = self.data_wrapper.get_all_voyages()
        now = datetime.now()
        current_time = datetime.time(hour = now.hour, minute = now.minute, second = now.second)
        now = datetime.date(year = now.year, month = now.month, day = now.day)

        for Voyage in all_voyages:
            # Status options: Finished, Landed abroad, In the Air, Not started, Cancelled
            departure_flight = self.flight_logic.get_flight(Voyage.departure_flight)
            arrival_flight = self.flight_logic.get_flight(Voyage.arrival_flight)
            
            if Voyage.status == VoyageStatus.Cancelled:
                pass
            
            # If the flight date has not been reached yet
            elif Voyage.date < now:
                Voyage.status = VoyageStatus.NotStarted
            
            # If the flight is today
            elif Voyage.date == now:
                
                # If the departure time has been reached
                if Voyage.departure_time <= current_time:
                    
                    # If the flight has not arrived at it's destination
                    if current_time < departure_flight.arrival_time:
                        Voyage.status = VoyageStatus.InTheAir
                    
                    # If the time is past the arrival time abroad
                    # and not reached the return flights departure time
                    elif departure_flight.arrival_time <= current_time < arrival_flight.departure_time:
                        Voyage.status = VoyageStatus.LandedAbroad
                    
                    # If the time is past the return flight departure time
                    # and not past its arrival time
                    elif arrival_flight.departure_time <= current_time < arrival_flight.arrival_time:
                        Voyage.status = VoyageStatus.InTheAir
                    
                    else:
                        Voyage.status = VoyageStatus.Finished
                
                else: 
                    Voyage.status = VoyageStatus.NotStarted
            
            else:
                Voyage.status = VoyageStatus.Finished
            
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
        return self.data_wrapper.cancel_voyage(id)


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
