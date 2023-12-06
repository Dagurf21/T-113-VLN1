class DestinationLogic:
    """This class is the logic layer for the destination class"""

    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_destination(self, destination):
        """Takes in a destination object and forwards it to the data layer"""
        return self.data_wrapper.create_destination(destination)

    def list_all_destinations(self) -> list:  # List of Destinations
        """Returns a list of all destinations"""
        # sorting tomfoolery
        return self.data_wrapper.get_all_destinations()

    def get_destination(self, id):  # Destination
        """Returns a destination object with the given id"""
        destination = self.data_wrapper.get_destination(id)
        return destination

    def update_destination(self, destination) -> None:
        """Updates a destination object with the given id"""
        return self.data_wrapper.update_destination(destination)

    def delete_destination(self, id) -> None:
        """Deletes a destination object with the given id"""
        return self.data_wrapper.delete_destination(id)


# Verify:
#
# if country is allowed based on assignment description
#
#
#
