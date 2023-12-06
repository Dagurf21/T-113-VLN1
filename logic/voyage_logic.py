class VoyageLogic:
    """This class handles all the logic for the Voyage class."""

    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def create_voyage(self, data) -> None:
        """Takes in a voyage object and forwards it to the data layer"""
        seats_available = data.plane.capacity - data.seats_sold

        if seats_available <= 0:
            raise ValueError("Plane is FULL (0 available seats)")

        return self.data_wrapper.create_voyage(data)

    def list_all_voyages(self) -> list:
        """Returns a list of all voyages"""
        return self.data_wrapper.get_all_voyages()

    def list_voyage(self, id):
        """Returns a voyage object with the given id"""
        return self.data_wrapper.get_voyage(id)

    def update_voyage(self, voyage) -> None:
        """Updates a voyage object with the given id"""
        return self.data_wrapper.update_voyage(voyage)

    def delete_voyage(self, id) -> None:
        """Deletes a voyage object with the given id"""
        self.data_wrapper.delete_voyage(id)

#Verify:
#
# if country is allowed based on assignment description
#
#
#
