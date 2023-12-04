class Destination_Logic:
    def __init__(self, data_connection):
        id: int
        country: str
        airport: str
        distance_km: int
        flight_time: int
        representative: str
        emergency_number: str
        pass

    def create_destination(self, destination):
        self.destination = destination

    def list_all_destinations(self) -> list:  # List of Destinations
        return self.data_wrapper.list_all_destinations()

    def list_destinations(self, id):  # Destination
        return self.data_wrapper.list_destination(id)

    def update_destination(self, id) -> None:
        pass

    def delete_destination(self, id) -> None:
        pass
