import data.data_wrapper as data_wrapper
import model.destination as destination

class Destination_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_destination(self, destination):
        self.data_wrapper.create_destination(destination)

    def list_all_destinations(self) -> list:  # List of Destinations
        return self.data_wrapper.list_all_destinations()

    def list_destinations(self, id):  # Destination
        return self.data_wrapper.list_destination(id)

    def update_destination(self, id) -> None:
        self.data_wrapper.update_destination(id)

    def delete_destination(self, id) -> None:
        self.data_wrapper.delete_destination(id)
