from logic.logic_utilities import Validator
from model.destination import Destination
from copy import deepcopy


class DestinationLogic:
    """This class is the logic layer for the destination class"""

    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.validate = Validator()

    def create_destination(self, destination_data):
        """Takes in a destination object and forwards it to the data layer"""
        if self.validate_destination(destination_data):
            return self.data_wrapper.create_destination(destination_data)
        else:
            return None

    def get_all_destinations(self) -> list["Destination"]:
        """Returns a list of all destinations"""
        return self.data_wrapper.get_all_destinations()

    def get_destination(self, search_id) -> "Destination":
        """Returns a destination object with the given id"""
        destination_list = self.get_all_destinations()

        for destination in destination_list:
            if destination.id == search_id:
                return destination

        return None

    def update_destination(self, destination: Destination) -> None:
        """Updates a destination object with the given id"""

        change_destination = self.get_destination(destination.id)

        if change_destination is None:
            return

        destination.country = change_destination.country
        destination.airport = change_destination.airport
        destination.distance_km = change_destination.distance_km
        destination.flight_time = change_destination.flight_time

        return self.data_wrapper.update_destination(destination)

    def delete_destination(self, destination_id) -> None:
        """Deletes a destination object with the given id"""
        return self.data_wrapper.delete_destination(destination_id)

    def validate_destination(self, destination) -> None:
        """Verifies a destination, if it is invalid nothing happens"""
        is_distance_valid = self.validate.distance_km(destination.distance_km)
        is_time_valid = self.validate.flight_time(destination.flight_time)

        return is_distance_valid and is_time_valid


# Verify:
#
# if country is allowed based on assignment description (DING!!)
#
# Flighttime?Distance?
#
# Emergency number
#
#
