from model.voyage import Voyage
from validator_logic import Validator


class VoyageLogic:
    """This class handles all the logic for the Voyage class."""

    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
        self.validate = Validator()

    def create_voyage(self, voyage_data) -> None:
        """Takes in a voyage object and forwards it to the data layer"""
        seats_available = voyage.plane.capacity - voyage.seats_sold

        return self.data_wrapper.create_voyage(voyage)

    def list_all_voyages(self) -> list:
        """Returns a list of all voyages"""
        return self.data_wrapper.get_all_voyages()

    def list_voyage(self, id):
        """Returns a voyage object with the given id"""
        return self.data_wrapper.get_voyage(id)

    def update_voyage(self, voyage) -> None:
        """Updates a voyage object with the given id"""
        return self.data_wrapper.update_voyage(voyage)

    def delete_voyage(self, id) -> None:
        """Deletes a voyage object with the given id"""
        return self.data_wrapper.delete_voyage(id)

    def validate_voyage(self, voyage) -> Voyage:
        """Validates a voyage and return a validated
        voyage if possible, else None"""
        are_seats_available = self.validate.seats_available(voyage)
        are_pilots_pilots = self.validate.job_position(voyage.pilots, "Pilot")
        are_attendants_attendants = self.validate.job_position(
            voyage.flight_attendants, "FlightAttendant"
        )


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
