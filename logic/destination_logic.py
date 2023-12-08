from logic.logic_utilities import Validator


class DestinationLogic:
    """This class is the logic layer for the destination class"""

    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        self.validate = Validator()

    def create_destination(self, destination_data):
        """Takes in a destination object and forwards it to the data layer"""
        return self.data_wrapper.create_destination(destination)

    def list_all_destinations(self) -> list:  # List of Destinations
        """Returns a list of all destinations"""
        # sorting tomfoolery
        return self.data_wrapper.get_all_destinations()

    def get_destination(self, search_id):  # Destination
        """Returns a destination object with the given id"""
        destination_list = self.data_wrapper.get_destination(id)

        for destination in destination_list:
            if destination.id == search_id:
                return destination
        return None

    def update_destination(self, destination_data) -> None:
        """Updates a destination object with the given id"""
        return self.data_wrapper.update_destination(destination_data)

    def delete_destination(self, destination_id) -> None:
        """Deletes a destination object with the given id"""
        return self.data_wrapper.delete_destination(destination_id)


# Verify:
#
# if country is allowed based on assignment description (DING!!)
#
# Flighttime?Distance?
#
# Emergency number
#
#
