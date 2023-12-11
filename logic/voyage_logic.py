from model import Voyage
from logic import Validator
from logic import flight_logic
from model import Flight


class VoyageLogic:
    """This class handles all the logic for the Voyage class."""

    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
        self.validate = Validator()

    def create_voyage(self, data) -> None:
        """Takes in a voyage object and forwards it to the data layer"""
        # flight_data = Flight(date=data.date,destination=data.destination)
        # create_flight(flight_data)
        departure_flight = flight_logic.create_flight(0, data.destination, data)
        arrival_flight = flight_logic.create_flight(data.destination, 0, data)
        # TODO return date
        self.data_wrapper.create_voyage(
            Voyage(
                destination=data.destination,
                sold_seats=0,
                plane=data.plane,
                departure_flight=departure_flight,
                arrival_flight=arrival_flight,
                date=data.date,
                return_date=data.return_date,
                status="Not started",
            )
        )

    def get_all_voyages(self) -> list:
        """Returns a list of all voyages"""
        return self.data_wrapper.get_all_voyages()

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
