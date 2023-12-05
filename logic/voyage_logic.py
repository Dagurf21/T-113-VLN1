from data.flight_route_data import FlightRoute_Data
from model.flight_route import FlightRoute


class VoyageLogic:
    """This class handles all the logic for the Voyage class."""
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def create_voyage(self, data) -> None:
        """Takes in a voyage object and forwards it to the data layer"""
        self.data_wrapper.create_voyage(data)

    def list_all_voyages(self) -> list:
        """Returns a list of all voyages"""
        return self.data_wrapper.get_all_voyages()

    def list_voyage(self, id):
        """Returns a voyage object with the given id"""
        return self.data_wrapper.get_voyage(id)

    def update_voyage(self, id) -> None:
        """Updates a voyage object with the given id"""
        self.data_wrapper.update_voyage(id)

    def delete_voyage(self, id) -> None:
        """Deletes a voyage object with the given id"""
        self.data_wrapper.delete_voyage(id)
