class destination_logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_destination(self, destination):
        self.destination = destination

    def list_all_destinations(self) -> list[Destination]:
        return self.data_wrapper.list_all_destinations()

    def list_destinations(self, id) -> Destination:
        return self.data_wrapper.list_destination(id)
    
    def update_destination(self, id) -> None:
        pass

    def delete_destination(self, id) -> None:
