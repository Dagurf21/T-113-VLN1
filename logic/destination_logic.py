from data.data_wrapper import Data_Wrapper
from model.destination import Destination


class DestinationLogic:
    """This class is the logic layer for the destination class"""

    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_destination(self, destination):
        """Takes in a destination object and forwards it to the data layer"""
        self.data_wrapper.create_destination(destination)

    def list_all_destinations(self) -> list:  # List of Destinations
        """Returns a list of all destinations"""
        return self.data_wrapper.list_all_destinations()

    def list_destinations(self, id):  # Destination
        """Returns a destination object with the given id"""
        return self.data_wrapper.list_destination(id)

    def update_destination(self, id) -> None:
        """Updates a destination object with the given id"""
        self.data_wrapper.update_destination(id)

    def delete_destination(self, id) -> None:
        """Deletes a destination object with the given id"""
        self.data_wrapper.delete_destination(id)
