from model import Voyage, VoyageStatus
from logic import Validator, FlightLogic, PlaneLogic
import datetime


class VoyageLogic:
    """This class handles all the logic for the Voyage class."""

    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
        self.validate = Validator()
        self.flight_logic = FlightLogic(data_connection)
        self.plane_logic = PlaneLogic(data_connection)

    def create_voyage(
        self,
        plane_id: int,
        destination_id: int,
        date: datetime.date,
        return_departure_date: datetime.date,
        departure_time: datetime.time,
        return_departure_time: datetime.time,
        sold_seats: int,
        flight_attendants: list[int],
        pilots: list[int],
    ) -> None:
        """Takes in a voyage object and forwards it to the data layer"""

        departure_flight = self.flight_logic.create_flight(
            0, destination_id, date, departure_time
        )

        arrival_flight = self.flight_logic.create_flight(
            destination_id, 0, return_departure_date, return_departure_time
        )

        new_voyage = self.data_wrapper.create_voyage(
            Voyage(
                destination=destination_id,
                sold_seats=sold_seats,
                plane=plane_id,
                pilots=pilots,
                flight_attendants=flight_attendants,
                departure_time=departure_time,
                departure_flight=departure_flight,
                return_departure_time=return_departure_time,
                return_flight=arrival_flight,
                departure_date=date,
                return_date=return_departure_date,
                status=VoyageStatus.NotStarted,
            )
        )

        plane = self.plane_logic.get_plane(plane_id)
        plane.voyages.append(new_voyage)
        self.plane_logic.update_plane(plane)

    def get_all_voyages(self) -> list:
        """Returns a list of all voyages"""

        all_voyages = self.data_wrapper.get_all_voyages()
        now = datetime.datetime.now()
        now_time = datetime.time(hour=now.hour, minute=now.minute)

        for voyage in all_voyages:
            # Status options: Finished, Landed abroad, In the Air, Not started, Cancelled
            departure_flight = self.flight_logic.get_flight(
                voyage.departure_flight, voyage.departure_date
            )
            arrival_flight = self.flight_logic.get_flight(
                voyage.return_flight, voyage.departure_date
            )

            if voyage.status == VoyageStatus.Cancelled:
                pass

            # If the flight date has not been reached yet
            elif voyage.departure_date > now.date():
                voyage.status = VoyageStatus.NotStarted

            # If the flight is today
            elif voyage.departure_date == now.date():
                # If the departure time has been reached
                if voyage.departure_time >= now_time:
                    # If the flight has not arrived at it's destination
                    if now_time < departure_flight.arrival_time:
                        voyage.status = VoyageStatus.InTheAir

                    # If the time is past the arrival time abroad
                    # and not reached the return flights departure time
                    elif (
                        departure_flight.arrival_time
                        <= now_time
                        < arrival_flight.departure_time
                    ):
                        voyage.status = VoyageStatus.LandedAbroad

                    # If the time is past the return flight departure time
                    # and not past its arrival time
                    elif (
                        arrival_flight.departure_time
                        <= now_time
                        < arrival_flight.arrival_time
                    ):
                        voyage.status = VoyageStatus.InTheAir

                    else:
                        voyage.status = VoyageStatus.Finished

                else:
                    voyage.status = VoyageStatus.NotStarted

            else:
                voyage.status = VoyageStatus.Finished

        return all_voyages

    def get_voyage(self, voyage_id):
        """Returns a voyage object with the given id"""
        voyage_list = self.get_all_voyages()

        for voyage in voyage_list:
            if voyage.id == voyage_id:
                return voyage

        return None
    
    def staff_voyage(self,):
        ''' '''
        raise NotImplementedError

    def get_voyage_by_date(self, date) -> list[Voyage]:
        '''Filters out all voyages by given date'''

        all_voyages = self.get_all_voyages
        voyage_on_date = []

        for voyage in all_voyages:
            
            if voyage.date == date:
                voyage_on_date.append(voyage)
            
            else:
                pass

        return voyage_on_date

    def update_voyage(self, voyage) -> None:
        """Updates a voyage object with the given id"""
        voyage_to_update = self.get_voyage(voyage.id)

        if voyage_to_update is None:
            return

        voyage_to_update.sold_seats = voyage.sold_seats
        voyage_to_update.pilots = voyage.pilots
        voyage_to_update.flight_attendants = voyage.flight_attendants

        return self.data_wrapper.update_voyage(voyage_to_update)

    def delete_voyage(self, id) -> None:
        """Deletes a voyage object with the given id"""
        return self.data_wrapper.cancel_voyage(id)

    def validate_status(self, voyage) -> None:
        """Validates the status of the given voyage"""
        validated_voyage = self.validate.status(voyage)
        return self.update_voyage(validated_voyage)

    def validate_departure_time(
        self, date: datetime.date, departure_time: datetime.time
    ) -> bool:
        """Returns True if no other voyages are departing at the same date and time"""
        all_voyages = self.get_all_voyages()

        for voyage in all_voyages:
            if (
                date == voyage.departure_date
                and departure_time == voyage.departure_time
            ):
                return False

        return True
    
    def validate_return_departure_time(
        self, date: datetime.date, departure_time: datetime.time
    ) -> bool:
        """Returns True if no other voyages are departing at the same date and time"""
        all_voyages = self.get_all_voyages()

        for voyage in all_voyages:
            if (
                date == voyage.return_date
                and departure_time == voyage.return_departure_time
            ):
                return False

        return True
