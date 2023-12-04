from data.flight_route_data import FlightRoute_Data
from model.flight_route import FlightRoute


class VoyageLogic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def create_voyage(self, data) -> None:
        self.data_wrapper.create_voyage(data)

    def list_all_voyages(self) -> list:
        return self.data_wrapper.list_all_voyages()

    def list_voyage(self, id):
        return self.data_wrapper.list_voyage(id)

    def update_voyage(self, id) -> None:
        self.data_wrapper.update_voyage(id)

    def delete_voyage(self, id) -> None:
        self.data_wrapper.delete_voyage(id)
