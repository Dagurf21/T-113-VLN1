from data.data_wrapper import DataWrapper
from model.destination import Destination


class DestinationLogic:
    """This class is the logic layer for the destination class"""

    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_destination(self, destination):
        """Takes in a destination object and forwards it to the data layer"""
        return self.data_wrapper.create_destination(destination)

    def list_all_destinations(self) -> list:  # List of Destinations
        """Returns a list of all destinations"""
        return self.data_wrapper.get_all_destinations()

    def list_destination(self, id):  # Destination
        """Returns a destination object with the given id"""
        destination_list = self.data_wrapper.get_destination(id)
        # sorting tomfoolery
        return destination_list

    def update_destination(self, id, destination) -> None:
        """Updates a destination object with the given id"""
        destination.id = id
        return self.data_wrapper.update_destination(destination)

    def delete_destination(self, id) -> None:
        """Deletes a destination object with the given id"""
        self.data_wrapper.delete_destination(id)
